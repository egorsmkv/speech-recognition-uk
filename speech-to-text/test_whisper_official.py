import torch
import whisper
import re
import numpy as np
import os
import scipy.io.wavfile as wavfile

from tempfile import NamedTemporaryFile
from datasets import load_metric, load_from_disk


cache_file_test = 'cv10_clean.data'
ds = load_from_disk(cache_file_test)

model = whisper.load_model("medium")

def only_uk_sentence(v):
    char_set_lower = 'а, б, в, г, ґ, д, е, є, ж, з, и, і, ї, й, к, л, м, н, о, п, р, с, т, у, ф, х, ц, ч, ш, щ, ь, ю, я'.replace(',','').replace(' ', '')
    char_set_upper = char_set_lower.upper()
    char_set = char_set_lower + char_set_upper
    char_set = char_set + '—,!?' + "'" + ' '

    return all((True if x in char_set else False for x in v))


def map_to_pred(batch):
    tmp_files = []

    for speech in batch["speech"]:
        with NamedTemporaryFile(suffix='.wav', delete=False) as tmp:
            wavfile.write(tmp.name, 16000, np.array(speech))
            tmp_files.append(tmp.name)

    results = []
    for idx, t in enumerate(tmp_files):
        result = model.transcribe(t, language='uk')

        results.append(result["text"])

    batch["predicted"] = [it.replace('’', "'").strip().lower().replace(',','').replace('.','').replace('?','').replace('!','') for it in results]
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

    for tf in tmp_files:
        os.unlink(tf)

    return batch


result = ds.map(map_to_pred, batched=True, batch_size=10, remove_columns=list(ds.features.keys()))

wer = load_metric("wer.py")
cer = load_metric("cer.py")

predictions = [x.upper() for x in result["predicted"]]
references = [x.upper() for x in result["target"]]

print(f"WER: {round(wer.compute(predictions=predictions, references=references), 4)}")
print(f"CER: {round(cer.compute(predictions=predictions, references=references), 4)}")
