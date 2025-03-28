# 🇺🇦 Speech Recognition & Synthesis for Ukrainian

## Overview

This repository collects links to models, datasets, and tools for Ukrainian **Speech-to-Text** and **Text-to-Speech**.

## Speech-UK initiative

We have datasets/models/**leaderboards** on Hugging Face, check it out:

- https://huggingface.co/speech-uk

## Community

[![Discord](https://img.shields.io/discord/1199769227192713226?label=&logo=discord&logoColor=white&color=7289DA&style=flat-square)](https://bit.ly/discord-uds)

- Discord: https://bit.ly/discord-uds
- Speech Recognition: https://t.me/speech_recognition_uk
- Speech Synthesis: https://t.me/speech_synthesis_uk

## 🎤 Speech-to-Text

### 📦 Implementations

<details><summary>wav2vec2-bert</summary>
<p>
  
  - 600M params: https://huggingface.co/Yehor/w2v-bert-uk-v2.1 (demo: https://huggingface.co/spaces/Yehor/w2v-bert-uk-v2.1-demo)
  - 600M params: https://huggingface.co/Yehor/w2v-bert-uk (demo: https://huggingface.co/spaces/Yehor/w2v-bert-uk-demo)
    
</p>
</details>


<details><summary>wav2vec2</summary>
<p>
  
- 300M params (with language model based on Wikipedia texts): https://huggingface.co/Yehor/w2v-xls-r-uk
- 300M params: https://huggingface.co/robinhad/wav2vec2-xls-r-300m-uk
- 1B params: https://huggingface.co/arampacha/wav2vec2-xls-r-1b-uk

You can check demos out here: https://github.com/egorsmkv/wav2vec2-uk-demo
  
  </p>
</details>

<details><summary>HuBERT</summary>
<p>
  
- hubert-uk: https://huggingface.co/Yehor/hubert-uk
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


- FastConformer Hybrid Transducer-CTC Large P&C: https://huggingface.co/nvidia/stt_ua_fastconformer_hybrid_large_pc
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


<details><summary>Conformer-CTC</summary>
<p>

- https://huggingface.co/taras-sereda/uk-pods-conformer
  
  </p>
</details>

<details><summary>Whisper</summary>
<p>

- official whisper: https://github.com/openai/whisper
- whisper (small, fine-tuned for Ukrainian): https://github.com/egorsmkv/whisper-ukrainian
- whisper (large, fine-tuned for Ukrainian): https://huggingface.co/arampacha/whisper-large-uk-2
- https://huggingface.co/mitchelldehaven/whisper-medium-uk
- https://huggingface.co/mitchelldehaven/whisper-large-v2-uk

Quantized variants:

- https://huggingface.co/Yehor/whisper-large-v2-quantized-uk
- https://huggingface.co/Yehor/whisper-large-v3-turbo-quantized-uk

Lite Whisper:

- https://huggingface.co/collections/efficient-speech/lite-whisper-67c0fa0e01cef6d4b9a1ab5d

</p>
</details>

<details><summary>OWSM, OWSM-CTC, and OWLS</summary>
<p>

- https://huggingface.co/espnet/owsm_v3.2
- https://huggingface.co/espnet/owsm_ctc_v3.2_ft_1B
- https://huggingface.co/espnet/owls_025B_180K

</p>
</details>

<details><summary>Flashlight</summary>
<p>

- Flashlight Conformer: https://huggingface.co/Yehor/flashlight-uk

</p>
</details>

<details><summary>MMS</summary>
<p>
  
- mms-1b-fl102: https://huggingface.co/facebook/mms-1b-fl102
</p>
</details>

<details><summary>data2vec</summary>
<p>
  
- data2vec-large: https://huggingface.co/robinhad/data2vec-large-uk
</p>
</details>

<details><summary>VOSK</summary>
<p>

Models: https://huggingface.co/Yehor/vosk-uk

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

### 📊 Benchmarks

This benchmark uses [Common Voice 10 test split](https://github.com/egorsmkv/cv10-uk-testset-clean).

- **WER**: Word Error Rate
- **CER**: Character Error Rate

#### `wav2vec2-bert`

| Model | WER | CER | Accuracy (words) |
|-------|-----|-----|------------|
| Yehor/w2v-bert-uk (FP16) | 6.6% | 1.34% | 93.4% |
| Yehor/w2v-bert-uk-v2.1 (FP16) | 17.34% | 3.33% | 82.66% |

#### `wav2vec2`

| Model | WER | CER | Accuracy (words) |
|-------|-----|-----|------------|
| Yehor/w2v-xls-r-uk | 20.24% | 3.64% | 79.76% |
| robinhad/wav2vec2-xls-r-300m-uk | 27.36% | 5.37% | 72.64% |
| arampacha/wav2vec2-xls-r-1b-uk | 16.52% | 2.93% | 83.48% |

#### `HuBERT`

| Model | WER | CER | Accuracy (words) |
|-------|-----|-----|-------------|
| Yehor/hubert-uk (FP16) | 37.07% | 6.87% | 62.93% |


#### `Citrinet`

| Model | WER | CER | Accuracy (words) |
|-------|-----|-----|------------|
| nvidia/stt_uk_citrinet_1024_gamma_0_25 | 4.32% | 0.94% | 95.68% |
| neongeckocom/stt_uk_citrinet_512_gamma_0_25 | 7.46% | 1.6% | 92.54% |

#### `ContextNet`

| Model | WER | CER | Accuracy (words) |
|-------|-----|-----|------------|
| theodotus/stt_uk_contextnet_512 | 6.69% | 1.45% | 93.31% |

#### `FastConformer P&C`

This model supports text punctuation and capitalization

| Model | WER | CER | Accuracy (words) |
|-------|-----|-----|------------|
| nvidia/stt_ua_fastconformer_hybrid_large_pc | 4.52% | 1% | 95.48% |
| theodotus/stt_ua_fastconformer_hybrid_large_pc | 4% | 1.02% | 96% |

#### `Squeezeformer`

| Model | WER | CER | Accuracy (words) |
|-------|-----|-----|------------|
| theodotus/stt_uk_squeezeformer_ctc_xs | 10.78% | 2.29% | 89.22% |
| theodotus/stt_uk_squeezeformer_ctc_sm | 8.2% | 1.75% | 91.8% |
| theodotus/stt_uk_squeezeformer_ctc_ml | 5.91% | 1.26% | 94.09% |

#### `Conformer-CTC`

| Model | WER | CER | Accuracy (words) |
|-------|-----|-----|------------|
| taras-sereda/uk-pods-conformer | 6.75% | 1.41% | 93.25% |

#### `Whisper`

| Model | WER | CER | Accuracy (words) |
|-------|-----|-----|------------|
| tiny | 63.08% | 18.59% | 36.92% |
| base | 52.1% | 14.08% | 47.9% |
| small | 30.57% | 7.64% | 69.43% |
| medium | 18.73% | 4.4% | 81.27% |
| large (v1) | 16.42% | 3.93% | 83.58% |
| large (v2) | 13.72% | 3.18% | 86.28% |
| large (v3) | 20.53% | 5.28% | 79.478% |
| turbo | 22.83% | 7.05% | 77.17% |

Quantized versions:

| Model | WER | CER | Accuracy (words) |
|-------|-----|-----|------------|
| Yehor/whisper-large-v2-quantized-uk | 14.95% | 4.23% | 85.05% |
| Yehor/whisper-large-v3-turbo-quantized-uk | 12.75% | 3.25% | 87.25% |
| efficient-speech/lite-whisper-large-v3-turbo | 42.89% | 12.59% | 57.11% |
| efficient-speech/lite-whisper-large-v3-turbo-acc | 17.79% | 4.34% | 82.21% |

If you want to fine-tune a Whisper model on own data, then use this repository: https://github.com/egorsmkv/whisper-ukrainian

#### `Flashlight`

| Model | WER | CER | Accuracy (words) |
|-------|-----|-----|------------|
| Flashlight Conformer | 19.15% | 2.44% | 80.85% |

#### `data2vec`

| Model | WER | CER | Accuracy (words) |
|-------|-----|-----|------------|
| robinhad/data2vec-large-uk | 31.17% | 7.31% | 68.83% |

#### `VOSK`

| Model | WER | CER | Accuracy (words) |
|-------|-----|-----|------------|
| v3 | 53.25% | 38.78% | 46.75% |

#### `m-ctc-t`

| Model | WER | CER | Accuracy (words) |
|-------|-----|-----|------------|
| speechbrain/m-ctc-t-large | 57% | 10.94% | 43% |

#### `DeepSpeech`

| Model | WER | CER | Accuracy (words) |
|-------|-----|-----|------------|
| v0.5 | 70.25% | 20.09% | 29.75% |


### 📖 Development

- [How to train own model using Kaldi][1]
- How to train a KenLM model based on Ukrainian Wikipedia data: https://github.com/egorsmkv/ukwiki-kenlm
- Export a traced JIT version of wav2vec2 models: https://github.com/egorsmkv/wav2vec2-jit

### 📚 Datasets

#### Compiled dataset: ~1200 hours

- Dataset: https://nx16725.your-storageshare.de/s/cAbcBeXtdz7znDN, use [Wget](https://www.gnu.org/software/wget) to download, downloading in a browser has speed limitations, or use [torrent file][8]

#### Voice of America: ~390 hours

- Dataset: https://huggingface.co/datasets/speech-uk/voice-of-america

#### FLEURS

- Ukrainian subset: https://huggingface.co/datasets/google/fleurs/viewer/uk_ua/train

#### Ukrainian broadcast: ~300 hours

- Ukrainian broadcast speech: https://huggingface.co/datasets/Yehor/broadcast-speech-uk

#### YODAS2: ~400 hours

- Ukrainian subsets:
  - https://huggingface.co/datasets/espnet/yodas2/tree/main/data/uk000
  - https://huggingface.co/datasets/espnet/yodas2/tree/main/data/uk100

#### Ukrainian podcasts

- https://huggingface.co/datasets/taras-sereda/uk-pods

#### Cleaned Common Voice 10 (test set)

- Repository: https://github.com/egorsmkv/cv10-uk-testset-clean

#### Noised Common Voice 10

- Transcriptions: https://www.dropbox.com/s/ohj3y2cq8f4207a/transcriptions.zip?dl=0
- Audio files: https://www.dropbox.com/s/v8crgclt9opbrv1/data.zip?dl=0

#### Other

- ASR Corpus created using a Telegram bot for Ukrainian: https://huggingface.co/datasets/Yehor/tg-voices-uk
- Speech Dataset with Ukrainian: https://www.caito.de/2019/01/the-m-ailabs-speech-dataset/
- Mozilla Common Voice has the Ukrainian dataset: https://commonvoice.mozilla.org/uk/datasets
- M-AILABS Ukrainian Corpus  Ukrainian: http://www.caito.de/data/Training/stt_tts/uk_UK.tgz
- Espreso TV subset: https://blog.gdeltproject.org/visual-explorer-quick-workflow-for-downloading-belarusian-russian-ukrainian-transcripts-translations/
- VoxForge Repository: http://www.repository.voxforge1.org/downloads/uk/Trunk/

### ⭐ Related works

#### Language models

- Ukrainian LMs: https://huggingface.co/Yehor/kenlm-uk

#### Inverse Text Normalization

- WFST for Ukrainian Inverse Text Normalization: https://github.com/lociko/ukraine_itn_wfst

#### Text Enhancement

- Punctuation and capitalization model: https://huggingface.co/dchaplinsky/punctuation_uk_bert (demo: https://huggingface.co/spaces/Yehor/punctuation-uk)

#### Aligners

- NeMo Forced Aligner: https://github.com/NVIDIA/NeMo/tree/main/tools/nemo_forced_aligner
- Aligner for wav2vec2-bert models: https://github.com/egorsmkv/w2v2-bert-aligner
- Aligner based on FasterWhisper (mostly for TTS): https://github.com/patriotyk/narizaka
- Aligner based on Kaldi: https://github.com/proger/uk

#### Other

- A space to calculate ASR metrics: https://huggingface.co/spaces/Yehor/evaluate-asr-outputs
- A space to see ASR outputs: https://huggingface.co/spaces/Yehor/see-asr-outputs

## 📢 Text-to-Speech

Test sentence with stresses:

```
К+ам'ян+ець-Под+ільський - м+істо в Хмельн+ицькій +області Укра+їни, ц+ентр Кам'ян+ець-Под+ільської міськ+ої об'+єднаної територі+альної гром+ади +і Кам'ян+ець-Под+ільського рай+ону.
```

Without stresses:

```
Кам'янець-Подільський - місто в Хмельницькій області України, центр Кам'янець-Подільської міської об'єднаної територіальної громади і Кам'янець-Подільського району.
```

### 📦 Implementations

<details><summary>StyleTTS2</summary>
<p>

- [StyleTTS2 demo & the code](https://huggingface.co/spaces/patriotyk/styletts2-ukrainian)

</p>
</details>

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

<details><summary>FastPitch</summary>
<p>

- NVIDIA FastPitch: https://huggingface.co/theodotus/tts_uk_fastpitch
  
</p>
</details>

<details><summary>Balacoon TTS</summary>
<p>

 - [Balacoon TTS](https://huggingface.co/spaces/balacoon/tts), voices of Lada, Tetiana and Mykyta. [Blog post](https://balacoon.com/blog/uk_release/) on model release.

https://github.com/clementruhm/speech-recognition-uk/assets/87281103/a13493ce-a5e5-4880-8b72-42b02feeee50

</p>
</details>

<details><summary>MMS</summary>
<p>

- https://huggingface.co/facebook/mms-tts-ukr

</p>
</details>


### 📚 Datasets

- **Open Text-to-Speech voices for 🇺🇦 Ukrainian**: https://huggingface.co/datasets/Yehor/opentts-uk
  - [Voice LADA][2], female
  - [Voice TETIANA][3], female
  - [Voice KATERYNA][4], female
  - [Voice MYKYTA][5], male
  - [Voice OLEKSA][6], male

### ⭐ Related works

#### Accentors

- https://github.com/NeonBohdan/ukrainian-accentor-transformer
- https://github.com/lang-uk/ukrainian-word-stress
- https://github.com/egorsmkv/ukrainian-accentor

#### Grapheme-to-Phoneme

ipa-uk:
  - https://github.com/lang-uk/ipa-uk
  - https://github.com/patriotyk/ipa-uk

Charsiu G2P:
  - https://huggingface.co/charsiu/g2p_multilingual_byT5_tiny_16_layers_100
  - https://huggingface.co/charsiu/g2p_multilingual_byT5_small_100
  - https://huggingface.co/charsiu/g2p_multilingual_mT5_small

Other:
  - https://github.com/dmort27/epitran
  - https://montreal-forced-aligner.readthedocs.io/en/v1.0/pretrained_models.html
  - https://huggingface.co/darkproger/ukpron

#### Misc

- Tool to make high quality text to speech (TTS) corpus from audio + text books: https://github.com/patriotyk/narizaka
- A model to do Text Normalization: https://huggingface.co/skypro1111/mbart-large-50-verbalization
- Audio Aesthetics for opentts-uk: https://huggingface.co/datasets/Yehor/opentts-uk-aesthetics

[1]: https://github.com/egorsmkv/speech-recognition-uk/tree/master/speech-to-text/vosk-model-creation
[2]: https://huggingface.co/datasets/speech-uk/opentts-lada
[3]: https://huggingface.co/datasets/speech-uk/opentts-tetiana
[4]: https://huggingface.co/datasets/speech-uk/opentts-kateryna
[5]: https://huggingface.co/datasets/speech-uk/opentts-mykyta
[6]: https://huggingface.co/datasets/speech-uk/opentts-oleksa
[8]: https://academictorrents.com/details/fcf8bb60c59e9eb583df003d54ed61776650beb8
