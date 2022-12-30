import os
import glob
import json
import wave
import time
import subprocess
from vosk import Model, KaldiRecognizer
from tempfile import NamedTemporaryFile
import scipy.io.wavfile as wavfile
import numpy as np

MODEL_PATH = os.getcwd() + '/vosk/uk_v3/model'
RATE = 8000 * 2  # hz
CHUNK = 1024 * 4
FFMPEG_PATH='/usr/bin/ffmpeg'

from transformers import Wav2Vec2Processor, Wav2Vec2ForCTC
from datasets import load_dataset, load_metric, load_from_disk

csv_test_file = '/home/yehor/Desktop/CV7-test/cv10_clean.csv'
cache_folder = f"cv10_clean.data"

def recognizer():
    return KaldiRecognizer(Model(MODEL_PATH), RATE)

def recognize_file(rec, file_path):
    res = ''
    res_part = ''

    wf = wave.open(file_path, 'rb')

    data = wf.readframes(CHUNK)

    while len(data) > 0:
        data = wf.readframes(CHUNK)

        if rec.AcceptWaveform(data):
            result = json.loads(rec.Result())
            if len(result['text']) > 0:
                res = result['text']
        else:
            result = json.loads(rec.PartialResult())
            if len(result['partial']) > 0:
                res_part = result['partial']

    wf.close()

    os.unlink(file_path)

    if len(res) > 0:
        return res
    
    return res_part

s = time.time()
print('Loading Model')

r = recognizer()

print('Loaded Model')
print(time.time() - s, 'secs')


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
    tmp_files = []

    for speech in batch["speech"]:
        with NamedTemporaryFile(suffix='.wav', delete=True) as tmp, NamedTemporaryFile(suffix='.wav', delete=False) as tmp2:
            wavfile.write(tmp.name, 16000, np.array(speech))

            output = subprocess.Popen([FFMPEG_PATH, '-i', tmp.name, '-f', 'wav', '-acodec', 'pcm_s16le', '-y', tmp2.name], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
            output.communicate()

            tmp_files.append(tmp2.name)

    predicted = []

    for tp in tmp_files:
        x = recognize_file(r, tp)
        predicted.append(x)

    batch["predicted"] = predicted
    batch["target"] = [ it.strip() for it in batch["text"] ]

    print(batch["predicted"])
    print(batch["target"])

    return batch


result = ds.map(map_to_pred, batched=True, batch_size=100, remove_columns=list(ds.features.keys()))

wer = load_metric("wer.py")
cer = load_metric("cer.py")

predictions = [x.upper() for x in result["predicted"]]
references = [x.upper() for x in result["target"]]

print(f"WER: {round(wer.compute(predictions=predictions, references=references), 4)}")
print(f"CER: {round(cer.compute(predictions=predictions, references=references), 4)}")
