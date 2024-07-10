# Speech Recognition for Ukrainian 🇺🇦

The goal of this repository is to collect information and datasets for Ukrainian automatic speech recognition aka speech-to-text.

Also, this repository contains information about Ukrainian speech synthesis aka text-to-speech.

- **Join our Discord server** - https://discord.gg/nmUCXz55 - where we're talking about AI
- Join our Speech Recognition Group in Telegram: https://t.me/speech_recognition_uk
- Join our Speech Synthesis Group in Telegram: https://t.me/speech_synthesis_uk

Or you can [start a discussion](https://github.com/egorsmkv/speech-recognition-uk/discussions/new).

## Donate

You can support our work by donation:

- via Monobank: https://send.monobank.ua/jar/3Saxixsdua
- on Patreon: https://www.patreon.com/yehor_smoliakov

# 🎤 Speech-to-Text

## 💡 Implementations

<details><summary>wav2vec2-bert</summary>
<p>
  
  - 600M params: https://huggingface.co/Yehor/w2v-bert-2.0-uk
    
</p>
</details>


<details><summary>wav2vec2</summary>
<p>
  
- 1B params (with language model based on small portion of data): https://huggingface.co/Yehor/wav2vec2-xls-r-1b-uk-with-lm
- 1B params (with language model based on News texts): https://huggingface.co/Yehor/wav2vec2-xls-r-1b-uk-with-news-lm
- 1B params (with binary language model based on News texts): https://huggingface.co/Yehor/wav2vec2-xls-r-1b-uk-with-binary-news-lm
- 1B params (with language model: OSCAR): https://huggingface.co/arampacha/wav2vec2-xls-r-1b-uk
- 1B params (with language model: OSCAR): https://huggingface.co/arampacha/wav2vec2-xls-r-1b-uk-cv
- 300M params (with language model based on small portion of data): https://huggingface.co/Yehor/wav2vec2-xls-r-300m-uk-with-lm
- 300M params (but without language model): https://huggingface.co/robinhad/wav2vec2-xls-r-300m-uk
- 300M params (with language model based on small portion of data): https://huggingface.co/Yehor/wav2vec2-xls-r-300m-uk-with-small-lm
- 300M params (with language model based on small portion of data) and noised data: https://huggingface.co/Yehor/wav2vec2-xls-r-300m-uk-with-small-lm-noisy
- 300M params (with language model based on News texts): https://huggingface.co/Yehor/wav2vec2-xls-r-300m-uk-with-news-lm
- 300M params (with language model based on Wikipedia texts): https://huggingface.co/Yehor/wav2vec2-xls-r-300m-uk-with-wiki-lm
- 90M params (with language model based on small portion of data): https://huggingface.co/Yehor/wav2vec2-xls-r-base-uk-with-small-lm
- 90M params (with language model based on small portion of data): https://huggingface.co/Yehor/wav2vec2-xls-r-base-uk-with-cv-lm
- ONNX model (1B and 300M models): https://github.com/egorsmkv/ukrainian-onnx-model

You can check demos out here: https://github.com/egorsmkv/wav2vec2-uk-demo
  
  </p>
</details>

<details><summary>data2vec</summary>
<p>
  
- data2vec-large: https://huggingface.co/robinhad/data2vec-large-uk
</p>
</details>

<details><summary>Citrinet</summary>
<p>
  
- NVIDIA Streaming Citrinet 1024 (uk): https://huggingface.co/nvidia/stt_uk_citrinet_1024_gamma_0_25
- NVIDIA Streaming Citrinet 512 (uk): https://huggingface.co/neongeckocom/stt_uk_citrinet_512_gamma_0_25

</p>
</details>

<details><summary>ContextNet</summary>
<p>
  
- NVIDIA Streaming ContextNet 512 (uk): https://huggingface.co/theodotus/stt_uk_contextnet_512
  
  </p>
</details>

<details><summary>FastConformer</summary>
<p>

- FastConformer Hybrid Transducer-CTC Large P&C: https://huggingface.co/theodotus/stt_ua_fastconformer_hybrid_large_pc
    - Demo: https://huggingface.co/spaces/theodotus/asr-uk-punctuation-capitalization
  
  </p>
</details>

<details><summary>Squeezeformer</summary>
<p>

- Squeezeformer-CTC ML: https://huggingface.co/theodotus/stt_uk_squeezeformer_ctc_ml
    - Demo 1: https://huggingface.co/spaces/theodotus/streaming-asr-uk
    - Demo 2: https://huggingface.co/spaces/theodotus/buffered-asr-uk
- Squeezeformer-CTC SM: https://huggingface.co/theodotus/stt_uk_squeezeformer_ctc_sm
- Squeezeformer-CTC XS: https://huggingface.co/theodotus/stt_uk_squeezeformer_ctc_xs
  
  </p>
</details>

<details><summary>VOSK</summary>
<p>
  
- VOSK v3 nano (with dynamic graph): https://drive.google.com/file/d/1Pwlxmtz7SPPm1DThBPM3u66nH6-Dsb1n/view?usp=sharing (73 mb)
- VOSK v3 small (with dynamic graph): https://drive.google.com/file/d/1Zkambkw2hfpLbMmpq2AR04-I7nhyjqtd/view?usp=sharing (133 mb)
- VOSK v3 (with dynamic graph): https://drive.google.com/file/d/12AdVn-EWFwEJXLzNvM0OB-utSNf7nJ4Q/view?usp=sharing (345 mb)
- VOSK v3: https://drive.google.com/file/d/17umTgQuvvWyUiCJXET1OZ3kWNfywPjW2/view?usp=sharing (343 mb)
- VOSK v2: https://drive.google.com/file/d/1MdlN3JWUe8bpCR9A0irEr-Icc1WiPgZs/view?usp=sharing (339 mb, demo code: https://github.com/egorsmkv/vosk-ukrainian-demo)
- VOSK v1: https://drive.google.com/file/d/1nzpXRd4Gtdi0YVxCFYzqtKKtw_tPZQfK/view?usp=sharing (87 mb, an old model with less trained data)

**Note**: VOSK models are [licensed under **Apache License 2.0**](https://github.com/igorsitdikov/vosk-api/blob/master/COPYING).

</p>
</details>

<details><summary>DeepSpeech</summary>
<p>

- [DeepSpeech](https://github.com/mozilla/DeepSpeech) using transfer learning from English model: https://github.com/robinhad/voice-recognition-ua
  - v0.5: https://github.com/robinhad/voice-recognition-ua/releases/tag/v0.5 (1230+ hours)
  - v0.4: https://github.com/robinhad/voice-recognition-ua/releases/tag/v0.4 (1230 hours)
  - v0.3: https://github.com/robinhad/voice-recognition-ua/releases/tag/v0.3 (751 hours)

</p>
</details>

<details><summary>M-CTC-T</summary>
<p>

- m-ctc-t-large: https://huggingface.co/speechbrain/m-ctc-t-large

</p>
</details>

<details><summary>whisper</summary>
<p>

- whisper: https://github.com/openai/whisper
- whisper (small, fine-tuned for Ukrainian): https://github.com/egorsmkv/whisper-ukrainian
- whisper (large, fine-tuned for Ukrainian): https://huggingface.co/arampacha/whisper-large-uk-2

</p>
</details>


<details><summary>Flashlight</summary>
<p>

- Flashlight Conformer: https://github.com/egorsmkv/flashlight-ukrainian

</p>
</details>

## 📊 Benchmarks

This benchmark uses [Common Voice 10 test split](https://github.com/egorsmkv/cv10-uk-testset-clean).

### `wav2vec2-bert`

| Model | WER | CER | Accuracy, % | WER<sup>+LM</sup> | CER<sup>+LM</sup> | Accuracy<sup>+LM</sup>, % |
|-------|-----|-----|------------|------------------|-----|------------|
| Yehor/w2v-bert-2.0-uk | 0.0727 | 0.0151 | 92.73% | 0.0655 | 0.0139 | 93.45% |

### `wav2vec2`

| Model | WER | CER | Accuracy, % | WER<sup>+LM</sup> | CER<sup>+LM</sup> | Accuracy<sup>+LM</sup>, % |
|-------|-----|-----|------------|------------------|-----|------------|
| Yehor/wav2vec2-xls-r-1b-uk-with-lm | 0.1807 | 0.0317 | 81.93% | 0.1193 | 0.0218 | 88.07% |
| Yehor/wav2vec2-xls-r-1b-uk-with-binary-news-lm | 0.1807 | 0.0317 | 81.93% | 0.0997 | 0.0191 | 90.03% |
| Yehor/wav2vec2-xls-r-300m-uk-with-lm | 0.2906 | 0.0548 | 70.94% | 0.172 | 0.0355 | 82.8% |
| Yehor/wav2vec2-xls-r-300m-uk-with-news-lm | 0.2027 | 0.0365 | 79.73% | 0.0929 | 0.019 | 90.71% |
| Yehor/wav2vec2-xls-r-300m-uk-with-wiki-lm | 0.2027 | 0.0365 | 79.73% | 0.1045 | 0.0208 | 89.55% |
| Yehor/wav2vec2-xls-r-base-uk-with-small-lm | 0.4441 | 0.0975 | 55.59% | 0.2878 | 0.0711 | 71.22% |
| robinhad/wav2vec2-xls-r-300m-uk | 0.2736 | 0.0537 | 72.64% | - | - | - |
| arampacha/wav2vec2-xls-r-1b-uk | 0.1652 | 0.0293 | 83.48% | 0.0945 | 0.0175 | 90.55% |

### `Citrinet`

[lm-4gram-500k](https://huggingface.co/Yehor/kenlm-ukrainian/tree/main/news/lm-4gram-500k) is used as the LM

| Model | WER | CER | Accuracy, % | WER<sup>+LM</sup> | CER<sup>+LM</sup> | Accuracy<sup>+LM</sup>, % |
|-------|-----|-----|------------|------------------|-----|------------|
| nvidia/stt_uk_citrinet_1024_gamma_0_25 | 0.0432 | 0.0094 | 95.68% | 0.0352 | 0.0079 | 96.48% |
| neongeckocom/stt_uk_citrinet_512_gamma_0_25 | 0.0746 | 0.016 | 92.54% | 0.0563 | 0.0128 | 94.37% |

### `ContextNet`

| Model | WER | CER | Accuracy, % |
|-------|-----|-----|------------|
| theodotus/stt_uk_contextnet_512 | 0.0669 | 0.0145 | 93.31% |

### `FastConformer P&C`

This model supports text punctuation and capitalization

| Model | WER | CER | Accuracy, % | WER<sup>+P&C</sup> | CER<sup>+P&C</sup> | Accuracy<sup>+P&C</sup>, % |
|-------|-----|-----|------------|------------------|-----|------------|
| theodotus/stt_ua_fastconformer_hybrid_large_pc | 0.0400 | 0.0102 | 96.00% | 0.0710 | 0.0167 | 92.90% |

### `Squeezeformer`

[lm-4gram-500k](https://huggingface.co/Yehor/kenlm-ukrainian/tree/main/news/lm-4gram-500k) is used as the LM

| Model | WER | CER | Accuracy, % | WER<sup>+LM</sup> | CER<sup>+LM</sup> | Accuracy<sup>+LM</sup>, % |
|-------|-----|-----|------------|------------------|-----|------------|
| theodotus/stt_uk_squeezeformer_ctc_xs | 0.1078 | 0.0229 | 89.22% | 0.0777 | 0.0174 | 92.23% |
| theodotus/stt_uk_squeezeformer_ctc_sm | 0.082 | 0.0175 | 91.8% | 0.0605 | 0.0142 | 93.95% |
| theodotus/stt_uk_squeezeformer_ctc_ml | 0.0591 | 0.0126 | 94.09% | 0.0451 | 0.0105 | 95.49% |

### `Flashlight`

[lm-4gram-500k](https://huggingface.co/Yehor/kenlm-ukrainian/tree/main/news/lm-4gram-500k) is used as the LM

| Model | WER | CER | Accuracy, % | WER<sup>+LM</sup> | CER<sup>+LM</sup> | Accuracy<sup>+LM</sup>, % |
|-------|-----|-----|------------|------------------|-----|------------|
| Flashlight Conformer | 0.1915 | 0.0244 | 80.85% | 0.0907 | 0.0198 | 90.93% |

### `data2vec`

| Model | WER | CER | Accuracy, % |
|-------|-----|-----|------------|
| robinhad/data2vec-large-uk | 0.3117 | 0.0731 | 68.83% |

### `VOSK`

| Model | WER | CER | Accuracy, % |
|-------|-----|-----|------------|
| v3 | 0.5325 | 0.3878 | 46.75% |

### `m-ctc-t`

| Model | WER | CER | Accuracy, % |
|-------|-----|-----|------------|
| speechbrain/m-ctc-t-large | 0.57 | 0.1094 | 43% |

### `whisper`

| Model | WER | CER | Accuracy, % |
|-------|-----|-----|------------|
| tiny | 0.6308 | 0.1859 | 36.92% |
| base | 0.521 | 0.1408 | 47.9% |
| small | 0.3057 | 0.0764 | 69.43% |
| medium | 0.1873 | 0.044 | 81.27% |
| large (v1) | 0.1642 | 0.0393 | 83.58% |
| large (v2) | 0.1372 | 0.0318 | 86.28% |

Fine-tuned version for Ukrainian:

| Model | WER | CER | Accuracy, % |
|-------|-----|-----|------------|
| small | 0.2704 | 0.0565 | 72.96% |
| large | 0.2482 | 0.055 | 75.18% |

If you want to fine-tune a Whisper model on own data, then use this repository: https://github.com/egorsmkv/whisper-ukrainian

### `DeepSpeech`

| Model | WER | CER | Accuracy, % |
|-------|-----|-----|------------|
| v0.5 | 0.7025 | 0.2009 | 29.75% |


## 📖 Development

- How to train own model using Kaldi (in Russian): https://github.com/egorsmkv/speech-recognition-uk/blob/master/vosk-model-creation/INSTRUCTION.md
- How to train a KenLM model based on Ukrainian Wikipedia data: https://github.com/egorsmkv/ukwiki-kenlm
- Export a traced JIT version of wav2vec2 models: https://github.com/egorsmkv/wav2vec2-jit

## 📚 Datasets

### Compiled dataset from different open sources + Companies + Community = 188.31GB / ~1200 hours 💪

- Storage Share powered by Nextcloud: https://nx16725.your-storageshare.de/s/cAbcBeXtdz7znDN (use [Wget](https://www.gnu.org/software/wget) to download, downloading in a browser has speed limitations)
- Torrent file: https://academictorrents.com/details/fcf8bb60c59e9eb583df003d54ed61776650beb8 (188.31 GB)

### Voice of America (398 hours)

- Storage Share powered by Nextcloud: https://nx16725.your-storageshare.de/s/f4NYHXdEw2ykZKa

### Companies

- Mozilla Common Voice has the Ukrainian dataset: https://commonvoice.mozilla.org/uk/datasets
- M-AILABS Ukrainian Corpus  Ukrainian: http://www.caito.de/data/Training/stt_tts/uk_UK.tgz

### Cleaned Common Voice 10 (test set)

- Repository: https://github.com/egorsmkv/cv10-uk-testset-clean

### Noised Common Voice 10

- Transcriptions: https://www.dropbox.com/s/ohj3y2cq8f4207a/transcriptions.zip?dl=0
- Audio files: https://www.dropbox.com/s/v8crgclt9opbrv1/data.zip?dl=0

### Community

- VoxForge Repository: http://www.repository.voxforge1.org/downloads/uk/Trunk/

### Other

- ASR Corpus created using a Telegram bot for Ukrainian: https://github.com/egorsmkv/asr-tg-bot-corpus
- Speech Dataset with Ukrainian: https://www.caito.de/2019/01/the-m-ailabs-speech-dataset/

## ⭐ Related works

### Language models

- Ukrainian LMs: https://huggingface.co/Yehor/kenlm-ukrainian

### Inverse Text Normalization:

- WFST for Ukrainian Inverse Text Normalization: https://github.com/lociko/ukraine_itn_wfst

### Text Enhancement

- Punctuation and capitalization model: https://huggingface.co/dchaplinsky/punctuation_uk_bert

# 📢 Text-to-Speech

Test sentence with stresses:

```
К+ам'ян+ець-Под+ільський - м+істо в Хмельн+ицькій +області Укра+їни, ц+ентр Кам'ян+ець-Под+ільської міськ+ої об'+єднаної територі+альної гром+ади +і Кам'ян+ець-Под+ільського рай+ону.
```

Without stresses:

```
Кам'янець-Подільський - місто в Хмельницькій області України, центр Кам'янець-Подільської міської об'єднаної територіальної громади і Кам'янець-Подільського району.
```

## 💡 Implementations


<details><summary>P-Flow TTS</summary>
<p>

- [P-Flow TTS](https://huggingface.co/spaces/patriotyk/pflowtts_ukr_demo)

https://github.com/egorsmkv/speech-recognition-uk/assets/7875085/18cfc074-f8a1-4842-90b6-9503d0bb7250

</p>
</details>

<details><summary>RAD-TTS</summary>
<p>

- [RAD-TTS](https://github.com/egorsmkv/ukrainian-radtts), the voice "Lada"
- [RAD-TTS with three voices](https://github.com/egorsmkv/radtts-uk), voices of Lada, Tetiana, and Mykyta

https://user-images.githubusercontent.com/7875085/206881140-bf8c09e7-5553-43d9-8807-065c36b2904b.mp4
  
</p>
</details>


<details><summary>Coqui TTS</summary>
<p>

- v1.0.0 using M-AILABS dataset: https://github.com/robinhad/ukrainian-tts/releases/tag/v1.0.0 (200,000 steps)

- v2.0.0 using Mykyta/Olena dataset: https://github.com/robinhad/ukrainian-tts/releases/tag/v2.0.0 (140,000 steps)

https://user-images.githubusercontent.com/5759207/167480982-275d8ca0-571f-4d21-b8d7-3776b3091956.mp4

</p>
</details>

<details><summary>Neon TTS</summary>
<p>

 - [Coqui TTS](https://github.com/coqui-ai/TTS) model implemented in the [Neon Coqui TTS Python Plugin](https://pypi.org/project/neon-tts-plugin-coqui/). An interactive demo is available [on huggingface](https://huggingface.co/spaces/neongeckocom/neon-tts-plugin-coqui). This model and others can be downloaded [from huggingface](https://huggingface.co/neongeckocom) and more information can be found at [neon.ai](https://neon.ai/languages)

https://user-images.githubusercontent.com/96498856/170762023-d4b3f6d7-d756-4cb7-89de-dc50e9049b96.mp4

</p>
</details>

<details><summary>Balacoon TTS</summary>
<p>

 - [Balacoon TTS](https://huggingface.co/spaces/balacoon/tts), voices of Lada, Tetiana and Mykyta. [Blog post](https://balacoon.com/blog/uk_release/) on model release.

https://github.com/clementruhm/speech-recognition-uk/assets/87281103/a13493ce-a5e5-4880-8b72-42b02feeee50

</p>
</details>


## 📚 Datasets

- Voice "LADA", female: https://github.com/egorsmkv/ukrainian-tts-datasets/tree/main/lada
- Voice "TETIANA", female: https://github.com/egorsmkv/ukrainian-tts-datasets/tree/main/tetiana
- Voice "KATERYNA", female: https://github.com/egorsmkv/ukrainian-tts-datasets/tree/main/kateryna
- Voice "MYKYTA", male: https://github.com/egorsmkv/ukrainian-tts-datasets/tree/main/mykyta
- Voice "OLEKSA", male: https://github.com/egorsmkv/ukrainian-tts-datasets/tree/main/oleksa

## ⭐ Related works

### Accentors

- https://github.com/NeonBohdan/ukrainian-accentor-transformer
- https://github.com/lang-uk/ukrainian-word-stress
- https://github.com/egorsmkv/ukrainian-accentor

### Misc

- Tool to make high quality text to speech (TTS) corpus from audio + text books: https://github.com/patriotyk/narizaka
- A model to do Text Normalization: https://huggingface.co/skypro1111/mbart-large-50-verbalization
