"""
pip install -U evaluate torch openai-whisper
"""

import csv

import whisper
import evaluate

# Config
model_name = 'tiny'
batch_size = 20
sampling_rate = 16_000
device = 'cuda' # or cpu
testset_file = './cv10_clean.csv'

# Load the test dataset
with open(testset_file) as f:
    samples = list(csv.DictReader(f))

# Load the model
asr_model = whisper.load_model(model_name)
whisper_options = whisper.DecodingOptions(fp16=False, language='uk', beam_size=1, without_timestamps=True)

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

    # Transcribe the audio file
    predictions = []
    for path in paths:
        audio = whisper.load_audio(path)
        audio = whisper.pad_or_trim(audio)
        mel = whisper.log_mel_spectrogram(audio).to(device)
        result = whisper.decode(asr_model, mel, whisper_options)

        denormalized = result.text.replace('’', "'").strip().lower().replace(',', '').replace('.', '').replace('?', '').replace('!', '')

        predictions.append(denormalized)

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
