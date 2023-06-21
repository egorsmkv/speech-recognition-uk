"""
pip install -U evaluate torch soundfile transformers
"""

import csv

import torch
import soundfile as sf
import evaluate
from transformers import Wav2Vec2ProcessorWithLM, Wav2Vec2ForCTC

# Config
model_name = 'Yehor/wav2vec2-xls-r-base-uk-with-small-lm'
device = 'cuda' # or cpu
sampling_rate = 16_000

# sample
test_files = ['audio.wav']
references = ['вання сполучені штати надважливий стратегічний партнер однак є різниця штати мають спеціальний закон який передбачає якщо китай нападе на тайвань американські військові мають його захищати']

# Load the model
asr_model = Wav2Vec2ForCTC.from_pretrained(model_name).to(device)
processor = Wav2Vec2ProcessorWithLM.from_pretrained(model_name)

# Temporary variables
predictions_all = []
references_all = []

# Extract audio
audio_inputs = []
for path in test_files:
    audio_input, _ = sf.read(path)
    audio_inputs.append(audio_input)

# Transcribe the audio
features = processor(audio_inputs, sampling_rate=sampling_rate, padding=True, return_tensors='pt')
input_values = features.input_values.to(device)
attention_mask = features.attention_mask.to(device)

with torch.no_grad():
    logits = asr_model(input_values, attention_mask=attention_mask).logits

predictions = processor.batch_decode(logits.cpu().numpy()).text

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
