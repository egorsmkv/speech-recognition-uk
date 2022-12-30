import torch
import os
import zipfile
import torchaudio
from glob import glob
import numpy as np
import scipy.io.wavfile as wavfile

from tempfile import NamedTemporaryFile
from datasets import load_metric, load_from_disk

cache_file_test = 'cv10_clean.data'
ds = load_from_disk(cache_file_test)

device = torch.device('cuda')  # gpu also works, but our models are fast enough for CPU
model, decoder, utils = torch.hub.load(repo_or_dir='snakers4/silero-models',
                                       model='silero_stt',
                                       language='ua', # also available 'de', 'es'
                                       device=device)
(read_batch, split_into_batches,
 read_audio, prepare_model_input) = utils  # see function signature for details

def map_to_pred(batch):
    tmp_files = []

    for speech in batch["speech"]:
        with NamedTemporaryFile(suffix='.wav', delete=False) as tmp:
            wavfile.write(tmp.name, 16000, np.array(speech))
            tmp_files.append(tmp.name)

    batches = split_into_batches(tmp_files, batch_size=len(tmp_files))
    input = prepare_model_input(read_batch(batches[0]), device=device)

    output = model(input)
    results = []
    for example in output:
        r = decoder(example.cpu())
        results.append(r)

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
