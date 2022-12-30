import torch
import torchaudio
import os
import time
import re
import re

from transformers import MCTCTForCTC, MCTCTProcessor
from datasets import load_dataset, load_metric, load_from_disk

csv_test_file = '/home/yehor/Desktop/CV7-test/cv10_clean.csv'
cache_folder = f"cv10_clean.data"
model_name = 'speechbrain/m-ctc-t-large'

device = "cuda"

s = time.time()
print('Loading Model')
model = MCTCTForCTC.from_pretrained(model_name).to(device)
processor = MCTCTProcessor.from_pretrained(model_name)

print('Loaded Model')
print(time.time() - s, 'secs')
print(f'Evaluation: {model_name}')

def only_uk_sentence(v):
    char_set_lower = 'а, б, в, г, ґ, д, е, є, ж, з, и, і, ї, й, к, л, м, н, о, п, р, с, т, у, ф, х, ц, ч, ш, щ, ь, ю, я'.replace(',','').replace(' ', '')
    char_set_upper = char_set_lower.upper()
    char_set = char_set_lower + char_set_upper
    char_set = char_set + '—,!?' + "'" + ' '

    return all((True if x in char_set else False for x in v))


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
    # feature extraction
    input_features = processor(batch["speech"], sampling_rate=16000, padding=True, return_tensors="pt").input_features

    # retrieve logits
    with torch.no_grad():
        logits = model(input_features.to(device)).logits

    # take argmax and decode
    predicted_ids = torch.argmax(logits, dim=-1)
    predicted = processor.batch_decode(predicted_ids)

    batch["predicted"] = [it.lower() for it in predicted]
    batch["target"] = [ it.strip() for it in batch["text"] ]

    checked_preds = []
    checked_gt = []

    for idx, pred in enumerate(batch["predicted"]):
        has_num = bool(re.search(r'\d', pred))
        only_uk = only_uk_sentence(pred)

        if not has_num and only_uk:
            checked_preds.append(pred)
            checked_gt.append(batch["target"][idx])

    batch["predicted"] = checked_preds
    batch["target"] = checked_gt

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
