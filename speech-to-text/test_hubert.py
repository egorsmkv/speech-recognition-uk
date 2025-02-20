import csv

import torch
import torchaudio
import numpy as np
import evaluate

from transformers import HubertForCTC, Wav2Vec2Processor

batch_size = 1
device = "cuda:0"  # cuda:0, or cpu
torch_dtype = torch.float16
sampling_rate = 16_000

model_name = "Yehor/hubert-uk"
testset_file = "examples.csv"

# Load the test dataset
with open(testset_file) as f:
    samples = list(csv.DictReader(f))

# Load the model
asr_model = HubertForCTC.from_pretrained(
    model_name,
    device_map=device,
    torch_dtype=torch_dtype,
    # attn_implementation="flash_attention_2",
)
processor = Wav2Vec2Processor.from_pretrained(model_name)


# A func to make batches
def make_batches(iterable, n=1):
    lx = len(iterable)
    for ndx in range(0, lx, n):
        yield iterable[ndx : min(ndx + n, lx)]


predictions_all = []
references_all = []

# Batched inference
for batch in make_batches(samples, batch_size):
    paths = [it["path"] for it in batch]
    references = [it["text"] for it in batch]

    # Extract audio features
    audio_inputs = []
    for path in paths:
        audio_input, sampling_rate = torchaudio.load(path, backend="sox")
        audio_input = audio_input.squeeze(0).numpy()

        audio_inputs.append(audio_input)

    # Transcribe
    inputs = processor(audio_inputs, sampling_rate=16_000, padding=True).input_values

    features = torch.tensor(np.array(inputs), dtype=torch_dtype).to(device)

    with torch.inference_mode():
        logits = asr_model(features).logits

    predicted_ids = torch.argmax(logits, dim=-1)
    predictions = processor.batch_decode(predicted_ids)

    # Log outputs
    print("---")
    print("Predictions:")
    print(predictions)
    print("References:")
    print(references)
    print("---")

    # Add predictions and references
    predictions_all.extend(predictions)
    references_all.extend(references)

# Load evaluators
wer = evaluate.load("wer")
cer = evaluate.load("cer")

# Evaluate
wer_value = round(
    wer.compute(predictions=predictions_all, references=references_all), 4
)
cer_value = round(
    cer.compute(predictions=predictions_all, references=references_all), 4
)

# Print results
print("Final:")
print(f"WER: {wer_value} | CER: {cer_value}")
