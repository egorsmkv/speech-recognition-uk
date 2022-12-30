import torch
import nemo.collections.asr as nemo_asr
import numpy as np
import os
import scipy.io.wavfile as wavfile

from tempfile import NamedTemporaryFile
from datasets import load_metric, load_from_disk

asr_model = nemo_asr.models.EncDecCTCModel.from_pretrained("theodotus/stt_uk_squeezeformer_ctc_ml", map_location=torch.device('cuda'))

cache_file_test = 'cv10_clean.data'
ds = load_from_disk(cache_file_test)


def map_to_pred(batch):
    tmp_files = []

    for speech in batch["speech"]:
        with NamedTemporaryFile(suffix='.wav', delete=False) as tmp:
            wavfile.write(tmp.name, 16000, np.array(speech))
            tmp_files.append(tmp.name)

    results = asr_model.transcribe(tmp_files)
    
    # results = results[0]

    batch["predicted"] = [it.replace('’', "'") for it in results]
    batch["target"] = [ it.strip() for it in batch["text"] ]

    print(batch["predicted"])
    print(batch["target"])

    for tf in tmp_files:
        os.unlink(tf)

    return batch


result = ds.map(map_to_pred, batched=True, batch_size=100, remove_columns=list(ds.features.keys()))

wer = load_metric("wer.py")
cer = load_metric("cer.py")

predictions = [x.upper() for x in result["predicted"]]
references = [x.upper() for x in result["target"]]

print(f"WER: {round(wer.compute(predictions=predictions, references=references), 4)}")
print(f"CER: {round(cer.compute(predictions=predictions, references=references), 4)}")
