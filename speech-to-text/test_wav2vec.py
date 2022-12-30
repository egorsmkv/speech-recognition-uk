import torch
import torchaudio
import os
import time
import re

from transformers import Wav2Vec2Processor, Wav2Vec2ForCTC
from datasets import load_dataset, load_metric, load_from_disk

csv_test_file = '/home/yehor/Desktop/CV7-test/cv10_clean.csv'
cache_folder = f"cv10_clean.data"
model_name = '/home/yehor/Desktop/CV7-test/wav2vec2-xls-r-300m-uk-with-news-lm'

device = "cuda"

s = time.time()
print('Loading Model')
model = Wav2Vec2ForCTC.from_pretrained(model_name).to(device)
processor = Wav2Vec2Processor.from_pretrained(model_name)

print('Loaded Model')
print(time.time() - s, 'secs')
print(f'Evaluation: {model_name}')


def map_to_array(batch):
    path = batch["path"]
    speech, sampling_rate = torchaudio.load(path)
    if sampling_rate != 16_000:
        resampler = torchaudio.transforms.Resample(orig_freq=sampling_rate, new_freq=16_000)
        batch["speech"] = resampler.forward(speech.squeeze(0)).numpy()
    else:
        batch["speech"] = speech.squeeze(0).numpy()
    batch["lengths"] = len(batch["speech"])

    return batch

if os.path.isdir(cache_folder):
    ds = load_from_disk(cache_folder)
else:
    ds = load_dataset('csv', data_files=csv_test_file)['train']
    ds = ds.map(map_to_array, keep_in_memory=False, num_proc=5)
    ds.save_to_disk(cache_folder)


def map_to_pred(batch):
    features = processor(batch["speech"], sampling_rate=16000, padding=True, return_tensors="pt")
    input_values = features.input_values.to(device)
    attention_mask = features.attention_mask.to(device)
    with torch.no_grad():
        logits = model(input_values, attention_mask=attention_mask).logits
    predicted_ids = torch.argmax(logits, dim=-1)
    predicted = processor.batch_decode(predicted_ids)
    
    batch["predicted"] = predicted
    batch["target"] = [ it.strip() for it in batch["text"] ]

    print(batch["predicted"])
    print(batch["target"])

    return batch


result = ds.map(map_to_pred, batched=True, batch_size=5, remove_columns=list(ds.features.keys()))

wer = load_metric("wer.py")
cer = load_metric("cer.py")

predictions = [x.upper() for x in result["predicted"]]
references = [x.upper() for x in result["target"]]

print(f"WER: {round(wer.compute(predictions=predictions, references=references), 4)}")
print(f"CER: {round(cer.compute(predictions=predictions, references=references), 4)}")
