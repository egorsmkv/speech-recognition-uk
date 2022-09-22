# Speech Recognition for Ukrainian 🇺🇦

The goal of this repository is to collect information and datasets for automatic speech recognition (speech-to-text) in Ukrainian.

Also, this repository contains information about speech synthesis (text-to-speech) for Ukrainian.

- **Join our Speech Recognition Group in Telegram**: https://t.me/speech_recognition_uk
- **Join our Speech Synthesis Group in Telegram**: https://t.me/speech_synthesis_uk

## Donate

You can support our work by donation:

- via Monobank: https://send.monobank.ua/jar/3Saxixsdua
- on Patreon: https://www.patreon.com/yehor_smoliakov

# 🎤 Speech-to-Text

## 💡 Implementations

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
- NVIDIA Streaming Citrinet 512 (uk): https://huggingface.co/NeonBohdan/stt_uk_citrinet_512_gamma_0_25
    - Demo 1: https://huggingface.co/spaces/theodotus/streaming-asr-uk
    - Demo 2: https://huggingface.co/spaces/theodotus/buffered-asr-uk
</p>
</details>

<details><summary>ContextNet</summary>
<p>
  
- NVIDIA Streaming ContextNet 512 (uk): https://huggingface.co/theodotus/stt_uk_contextnet_512
  
  </p>
</details>

<details><summary>Squeezeformer</summary>
<p>
  
- Squeezeformer-CTC XS: https://huggingface.co/theodotus/stt_uk_squeezeformer_ctc_xs
  
  </p>
</details>

<details><summary>Silero</summary>
<p>

- Silero Models ([link](https://github.com/snakers4/silero-models)), a `ua_v3` xxsmall model, see provided colab notebooks and examples, some performance benchmarks [here](https://github.com/snakers4/silero-models/wiki/Performance-Benchmarks#speed-benchmarks), full optimized / quantized model is ~30MB w/o major quality loss
- Silero v1: https://github.com/snakers4/silero-models (demo code: https://github.com/egorsmkv/ua-silero-demo, also there is a demo as a Telegram bot: https://t.me/ukr_stt_bot)

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

</p>
</details>

## 📊 Benchmarks

This benchmark uses Common Voice 7 test split.

| Model | WER | CER | Quality, % |
|-------|-----|-----|------------|
| Yehor/wav2vec2-xls-r-1b-uk-with-lm | 0.1245 | 0.0244 | 87.55% |
| Yehor/wav2vec2-xls-r-1b-uk-with-binary-news-lm | 0.1142 | 0.0229 | **88.58%** |
| Yehor/wav2vec2-xls-r-300m-uk-with-lm | 0.1751 | 0.0394 | 82.49% |
| Yehor/wav2vec2-xls-r-300m-uk-with-news-lm | 0.118 | 0.0251 | 88.2% |
| Yehor/wav2vec2-xls-r-300m-uk-with-small-lm | 0.0706 | 0.0169 | **92.94%** |
| Yehor/wav2vec2-xls-r-300m-uk-with-wiki-lm | 0.1283 | 0.0267 | 87.17% |
| Yehor/wav2vec2-xls-r-base-uk-with-small-lm | 0.303 | 0.0818 | 69.7% |
| Yehor/wav2vec2-xls-r-base-uk-with-cv-lm | 0.13 | 0.0418 | 87% |
| nvidia/stt_uk_citrinet_1024_gamma_0_25 | 0.0517 | 0.0115 | **94.83%** |
| NeonBohdan/stt_uk_citrinet_512_gamma_0_25 | 0.0828 | 0.0187 | **91.72%** |
| theodotus/stt_uk_contextnet_512 | 0.0875 | 0.0199 | 91.25% |
| theodotus/stt_uk_squeezeformer_ctc_xs | 0.2184 | 0.0511 | 78.16% |
| arampacha/wav2vec2-xls-r-1b-uk | 0.1214 | 0.0244 | 87.86% |
| robinhad/wav2vec2-xls-r-300m-uk | 0.3111 | 0.0655 | 68.89% |
| robinhad/data2vec-large-uk | 0.3549 | 0.0859 | 64.51% |
| speechbrain/m-ctc-t-large | 0.603 | 0.1391 | 39.7% |
| VOSK v3 | 0.2537 | 0.0916 | 74.63% |
| Silero v3 | 0.2318 | - | 76.82% |

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

### Noised Common Voice 10

- Transcriptions: https://www.dropbox.com/s/ohj3y2cq8f4207a/transcriptions.zip?dl=0
- Audio files: https://www.dropbox.com/s/v8crgclt9opbrv1/data.zip?dl=0

### Community

- VoxForge Repository: http://www.repository.voxforge1.org/downloads/uk/Trunk/

### Other

- Speech Dataset with Ukrainian: https://www.caito.de/2019/01/the-m-ailabs-speech-dataset/

## ⭐ Related works

### Language models

- Ukrainian LMs: https://huggingface.co/Yehor/kenlm-ukrainian

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

<details><summary>Silero TTS</summary>
<p>

- [Silero TTS](https://github.com/snakers4/silero-models#text-to-speech), the voice "Mykyta"

https://user-images.githubusercontent.com/5759207/153086535-cfd923f4-e82a-496b-936c-e927589605af.mp4
  
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

## 📚 Datasets

- Voice "LADA", female: https://github.com/egorsmkv/ukrainian-tts-datasets/tree/main/lada

## ⭐ Related works

### Accentors

- https://github.com/lang-uk/ukrainian-word-stress
- https://github.com/egorsmkv/ukrainian-accentor
