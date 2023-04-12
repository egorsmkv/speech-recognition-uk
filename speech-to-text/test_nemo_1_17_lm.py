"""
pip install -U evaluate
"""

import torch
import nemo.collections.asr as nemo_asr
from evaluate import load

# Config
model_name = 'theodotus/stt_uk_squeezeformer_ctc_ml'
batch_size = 20

# Load the test dataset
samples = []
with open('./cv10_clean.csv') as f:
    rows = f.readlines()
    for idx, sample in enumerate(rows):
        if idx == 0:
            continue
        data = sample.strip().split(',')
        samples.append({'path': data[0], 'text': data[1]})

# Load the model
asr_model = nemo_asr.models.EncDecCTCModel.from_pretrained(model_name, map_location=torch.device('cuda'))

# Disable decoding strategy for the model
asr_model.change_decoding_strategy(None)

# Configure the pyctcdecode strategy
decoding_cfg = asr_model.cfg.decoding
decoding_cfg.strategy = 'pyctcdecode'
decoding_cfg.beam.beam_size = 128
decoding_cfg.beam.return_best_hypothesis = True
decoding_cfg.beam.beam_alpha = 0.5
decoding_cfg.beam.beam_beta = 1.5
decoding_cfg.beam.kenlm_path = 'lm.binary'

decoding_cfg.beam.pyctcdecode_cfg.beam_prune_logp = -10.0
decoding_cfg.beam.pyctcdecode_cfg.token_min_logp = -5.0

# decoding_cfg.beam.pyctcdecode_cfg.hotwords = []
# decoding_cfg.beam.pyctcdecode_cfg.hotword_weight = 10.0

# Use the pyctcdecode strategy
asr_model.change_decoding_strategy(decoding_cfg)

# A util function to make batches
def make_batches(iterable, n=1):
    l = len(iterable)
    for ndx in range(0, l, n):
        yield iterable[ndx:min(ndx + n, l)]

# Load evaluators
wer = load('wer')
cer = load('cer')

# Temporary variables
predictions_all = []
references_all = []

# Inference in the batched mode
for batch in make_batches(samples, batch_size):
    batch_paths = [it['path'] for it in batch]
    batch_target = [it['text'] for it in batch]

    # Transcribe the audio files
    predictions = asr_model.transcribe(paths2audio_files=batch_paths, batch_size=batch_size)

    # Transform the utterances
    predictions = [it.upper() for it in predictions]
    references = [it.upper() for it in batch_target]

    print('---')
    print('Predictions:')
    print(predictions)
    print('References:')
    print(references)
    print('---')

    # Add predictions and references
    predictions_all.extend(predictions)
    references_all.extend(references)

# Evaluate
final_wer_value = round(wer.compute(predictions=predictions_all, references=references_all), 4)
final_cer_value = round(cer.compute(predictions=predictions_all, references=references_all), 4)

# Print results
print('---')
print('Final:')
print(f'WER: {final_wer_value} | CER: {final_cer_value}')
