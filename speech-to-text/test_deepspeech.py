import torch
from stt import Model
import numpy as np
import os
import wave
import subprocess
import scipy.io.wavfile as wavfile

from tempfile import NamedTemporaryFile
from datasets import load_metric, load_from_disk

FFMPEG_PATH='/usr/bin/ffmpeg'

use_scorer = False

ds_model = Model("deepspeech/uk.tflite")
if use_scorer:
    ds_model.enableExternalScorer("deepspeech/kenlm.scorer")

cache_file_test = 'cv10_clean.data'
ds = load_from_disk(cache_file_test)


def map_to_pred(batch):
    results = []
    tmp_files = []

    for speech in batch["speech"]:
        with NamedTemporaryFile(suffix='.wav', delete=True) as tmp, NamedTemporaryFile(suffix='.wav', delete=False) as tmp2:
            wavfile.write(tmp.name, 16000, np.array(speech))

            output = subprocess.Popen([FFMPEG_PATH, '-i', tmp.name, '-f', 'wav', '-acodec', 'pcm_s16le', '-y', tmp2.name], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
            output.communicate()

            tmp_files.append(tmp2.name)

    for tmp_file in tmp_files:
        fin = wave.open(tmp_file, 'rb')
        speech = np.frombuffer(fin.readframes(fin.getnframes()), np.int16)
        fin.close()

        r = ds_model.stt(speech)

        results.append(r)

    batch["predicted"] = results
    batch["target"] = [ it.strip() for it in batch["text"] ]

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
