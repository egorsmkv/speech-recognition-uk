"""
pip install -U evaluate torch soundfile transformers
"""

import csv

import torch
import soundfile as sf
import evaluate
from transformers import Wav2Vec2Processor, Wav2Vec2ForCTC

# Config
model_name = 'Yehor/wav2vec2-xls-r-base-uk-with-small-lm'
batch_size = 20
device = 'cuda' # or cpu
sampling_rate = 16_000
testset_file = './cv10_clean.csv'

# Load the test dataset
with open(testset_file) as f:
    samples = list(csv.DictReader(f))

# Load the model
asr_model = Wav2Vec2ForCTC.from_pretrained(model_name).to(device)
processor = Wav2Vec2Processor.from_pretrained(model_name)

# A util function to make batches
def make_batches(iterable, n=1):
    l = len(iterable)
    for ndx in range(0, l, n):
        yield iterable[ndx:min(ndx + n, l)]

# Temporary variables
predictions_all = []
references_all = []

# Inference in the batched mode
for batch in make_batches(samples, batch_size):
    paths = [it['path'] for it in batch]
    references = [it['text'] for it in batch]

    # Extract audio
    audio_inputs = []
    for path in paths:
        audio_input, _ = sf.read(path)
        audio_inputs.append(audio_input)

    # Transcribe the audio
    features = processor(audio_inputs, sampling_rate=sampling_rate, padding=True, return_tensors='pt')
    input_values = features.input_values.to(device)
    attention_mask = features.attention_mask.to(device)

    with torch.no_grad():
        logits = asr_model(input_values, attention_mask=attention_mask).logits

    predicted_ids = torch.argmax(logits, dim=-1)
    predictions = processor.batch_decode(predicted_ids)

    # Log outputs
    print('---')
    print('Predictions:')
    print(predictions)
    print('References:')
    print(references)
    print('---')

    # Add predictions and references
    predictions_all.extend(predictions)
    references_all.extend(references)

# Load evaluators
wer = evaluate.load('wer')
cer = evaluate.load('cer')

# Evaluate
wer_value = round(wer.compute(predictions=predictions_all, references=references_all), 4)
cer_value = round(cer.compute(predictions=predictions_all, references=references_all), 4)

# Print results
print('Final:')
print(f'WER: {wer_value} | CER: {cer_value}')
