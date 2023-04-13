"""
pip install -U evaluate torch soundfile transformers
"""

import csv

import torch
import evaluate
import soundfile as sf
from transformers import WhisperForConditionalGeneration, WhisperProcessor

# Config
model_name = 'Yehor/whisper-small-ukrainian'
batch_size = 20
sampling_rate = 16_000
device = 'cuda' # or cpu
testset_file = './cv10_clean.csv'

# Load the test dataset
with open(testset_file) as f:
    samples = list(csv.DictReader(f))

# Load the model
asr_model = WhisperForConditionalGeneration.from_pretrained(model_name).to(device)
processor = WhisperProcessor.from_pretrained(model_name)

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
    input_features = processor(audio_inputs, sampling_rate=sampling_rate, return_tensors='pt').input_features.to(device)

    with torch.no_grad():
        generated_ids = asr_model.generate(inputs=input_features, max_length=448)

    transcription = processor.batch_decode(generated_ids, normalize=True, skip_special_tokens=True)
    predictions = [processor.tokenizer._normalize(it) for it in transcription]

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
