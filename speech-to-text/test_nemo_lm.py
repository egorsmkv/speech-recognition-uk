"""
pip install -U evaluate torch nemo-toolkit[all]
"""

import csv

import torch
import evaluate
import nemo.collections.asr as nemo_asr

# Config
model_name = 'theodotus/stt_uk_squeezeformer_ctc_ml'
batch_size = 20
device = 'cuda' # or cpu
kenlm_path = 'lm.binary'
lm_beam_size = 128
lm_beam_alpha = 0.5
lm_beam_beta = 1.5
testset_file = './cv10_clean.csv'

# Load the test dataset
with open(testset_file) as f:
    samples = list(csv.DictReader(f))

# Load the model
asr_model = nemo_asr.models.EncDecCTCModel.from_pretrained(model_name, map_location=torch.device(device))

# Disable decoding strategy for the model
asr_model.change_decoding_strategy(None)

# Configure the pyctcdecode strategy
decoding_cfg = asr_model.cfg.decoding
decoding_cfg.strategy = 'pyctcdecode'
decoding_cfg.beam.beam_size = lm_beam_size
decoding_cfg.beam.return_best_hypothesis = True
decoding_cfg.beam.beam_alpha = lm_beam_alpha
decoding_cfg.beam.beam_beta = lm_beam_beta
decoding_cfg.beam.kenlm_path = kenlm_path

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

# Temporary variables
predictions_all = []
references_all = []

# Inference in the batched mode
for batch in make_batches(samples, batch_size):
    paths = [it['path'] for it in batch]
    references = [it['text'] for it in batch]

    # Transcribe the audio files
    predictions = asr_model.transcribe(paths2audio_files=paths, batch_size=batch_size)

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
