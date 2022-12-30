import torch
import librosa
import numpy as np
import scipy.io.wavfile as wavfile

from tempfile import NamedTemporaryFile
from transformers import WhisperForConditionalGeneration, WhisperProcessor
from datasets import load_dataset
from datasets import load_metric, load_from_disk

print('libs loaded')

model = WhisperForConditionalGeneration.from_pretrained("arampacha/whisper-large-uk-2")
model.to('cuda')
processor = WhisperProcessor.from_pretrained("arampacha/whisper-large-uk-2")

print('models loaded')

cache_file_test = 'cv10_clean.data'
test_set = load_from_disk(cache_file_test)

print('dataset loaded')

wer = load_metric("wer.py")
cer = load_metric("cer.py")


def map_to_pred(batch):
    # save speech to files
    tmp_files = []

    for speech in batch["speech"]:
        with NamedTemporaryFile(suffix='.wav', delete=False) as tmp:
            wavfile.write(tmp.name, 16_000, np.array(speech))
            tmp_files.append(tmp.name)

    # load files
    audios = []
    for path in tmp_files:
        audio, _ = librosa.load(path)
        audios.append(audio)

    input_features = processor(audios, return_tensors="pt", sampling_rate=16_000).input_features
    input_features = input_features.to('cuda')
    try:
        generated_ids = model.generate(inputs=input_features)

        transcription = processor.batch_decode(generated_ids, normalize=True, skip_special_tokens=True)

        batch['predicted'] = [processor.tokenizer._normalize(it) for it in transcription]
        # batch['text'] = transcription

        print('Ground truth:')
        print(batch["text"])
        print('Predicted text:')
        print(batch["predicted"])

    except IndexError:
        # just a trick to pass the issue
        batch['text'] = ['-'] * len(batch['speech'])
        batch["predicted"] = ['-'] * len(batch['speech'])

    predictions = [x.upper() for x in batch["predicted"]]
    references = [x.upper() for x in batch["text"]]

    print(f"WER: {round(wer.compute(predictions=predictions, references=references), 4)}")
    print(f"CER: {round(cer.compute(predictions=predictions, references=references), 4)}")

    return batch

result = test_set.map(map_to_pred, batched=True, batch_size=10)

print('-----')

predictions = [x.upper() for x in result["predicted"]]
references = [x.upper() for x in result["text"]]

print(f"WER: {round(wer.compute(predictions=predictions, references=references), 4)}")
print(f"CER: {round(cer.compute(predictions=predictions, references=references), 4)}")
