#!/bin/bash

# Change this location to somewhere where you want to put the data.
data=./corpus/

. ./cmd.sh
. ./path.sh

stage=0
. utils/parse_options.sh

set -euo pipefail

mkdir -p $data

if [ $stage -le 0 ]; then
 # utils/fix_data_dir.sh data/ukraine

 # utils/subset_data_dir.sh --first data/ukraine 20000 data/dev_clean_2
 # n=$[`cat data/ukraine/text | wc -l` - 20000]
 # utils/subset_data_dir.sh --last data/ukraine $n data/train_clean_5

  for part in dev_clean_2 train_clean_5; do
    utils/fix_data_dir.sh data/$part
    utils/utt2spk_to_spk2utt.pl data/$part/utt2spk > data/$part/spk2utt || exit 1
    utils/validate_data_dir.sh --no-feats data/$part
  done
fi

if [ $stage -le 1 ]; then

  local/prepare_dict.sh --stage 3 --nj 4 --cmd "$train_cmd" \
    data/local/lm data/local/lm data/local/dict_nosp

  utils/prepare_lang.sh data/local/dict_nosp \
    "<UNK>" data/local/lang_tmp_nosp data/lang_nosp

  local/format_lms.sh --src-dir data/lang_nosp data/local/lm
  # Create ConstArpaLm format language model for full 3-gram and 4-gram LMs
  utils/build_const_arpa_lm.sh data/local/lm/lm_tglarge.arpa.gz \
    data/lang_nosp data/lang_nosp_test_tglarge
fi

if [ $stage -le 2 ]; then
  mfccdir=mfcc
  # spread the mfccs over various machines, as this data-set is quite large.

 for part in dev_clean_2 train_clean_5; do
   utils/fix_data_dir.sh data/$part
   steps/make_mfcc.sh --cmd "$train_cmd" --nj 4 data/$part exp/make_mfcc/$part $mfccdir
   steps/compute_cmvn_stats.sh data/$part exp/make_mfcc/$part $mfccdir
 done

 for part in dev_clean_2 train_clean_5; do
   utils/fix_data_dir.sh data/$part
 done
  # Get the shortest 500 utterances first because those are more likely
  # to have accurate alignments.
  utils/subset_data_dir.sh --shortest data/train_clean_5 15000 data/train_500short
fi

# train a monophone system
if [ $stage -le 3 ]; then
  # TODO(galv): Is this too many jobs for a smaller dataset?
  steps/train_mono.sh --boost-silence 1.25 --nj 4 --cmd "$train_cmd" \
    data/train_500short data/lang_nosp exp/mono

  steps/align_si.sh --boost-silence 1.25 --nj 4 --cmd "$train_cmd" \
    data/train_clean_5 data/lang_nosp exp/mono exp/mono_ali_train_clean_5
    echo "step completed"
fi

# train a first delta + delta-delta triphone system on all utterances
if [ $stage -le 4 ]; then
  steps/train_deltas.sh --boost-silence 1.25 --cmd "$train_cmd" \
    2000 10000 data/train_clean_5 data/lang_nosp exp/mono_ali_train_clean_5 exp/tri1

  steps/align_si.sh --nj 4 --cmd "$train_cmd" \
    data/train_clean_5 data/lang_nosp exp/tri1 exp/tri1_ali_train_clean_5
    echo "step completed"
fi

# train an LDA+MLLT system.
if [ $stage -le 5 ]; then
  steps/train_lda_mllt.sh --cmd "$train_cmd" \
    --splice-opts "--left-context=3 --right-context=3" 2500 15000 \
    data/train_clean_5 data/lang_nosp exp/tri1_ali_train_clean_5 exp/tri2b

  # Align utts using the tri2b model
  steps/align_si.sh  --nj 4 --cmd "$train_cmd" --use-graphs true \
    data/train_clean_5 data/lang_nosp exp/tri2b exp/tri2b_ali_train_clean_5
    echo "step completed"
fi

# Train tri3b, which is LDA+MLLT+SAT
if [ $stage -le 6 ]; then
  steps/train_sat.sh --cmd "$train_cmd" 2500 15000 \
    data/train_clean_5 data/lang_nosp exp/tri2b_ali_train_clean_5 exp/tri3b
echo "step completed"
fi

# Now we compute the pronunciation and silence probabilities from training data,
# and re-create the lang directory.
if [ $stage -le 7 ]; then
  steps/get_prons.sh --cmd "$train_cmd" \
    data/train_clean_5 data/lang_nosp exp/tri3b
  utils/dict_dir_add_pronprobs.sh --max-normalize true \
    data/local/dict_nosp \
    exp/tri3b/pron_counts_nowb.txt exp/tri3b/sil_counts_nowb.txt \
    exp/tri3b/pron_bigram_counts_nowb.txt data/local/dict

  utils/prepare_lang.sh data/local/dict \
    "<UNK>" data/local/lang_tmp data/lang

  local/format_lms.sh --src-dir data/lang data/local/lm

  utils/build_const_arpa_lm.sh \
    data/local/lm/lm_tglarge.arpa.gz data/lang data/lang_test_tglarge

  steps/align_fmllr.sh --nj 4 --cmd "$train_cmd" \
    data/train_clean_5 data/lang exp/tri3b exp/tri3b_ali_train_clean_5
    echo "step completed"
fi


if [ $stage -le 8 ]; then
  # Test the tri3b system with the silprobs and pron-probs.

  # decode using the tri3b model
  utils/mkgraph.sh data/lang_test_tgsmall \
                   exp/tri3b exp/tri3b/graph_tgsmall
  for test in dev_clean_2; do
    steps/decode_fmllr.sh --nj 4 --cmd "$decode_cmd" \
                          exp/tri3b/graph_tgsmall data/$test \
                          exp/tri3b/decode_tgsmall_$test
    steps/lmrescore.sh --cmd "$decode_cmd" data/lang_test_{tgsmall,tgmed} \
                       data/$test exp/tri3b/decode_{tgsmall,tgmed}_$test
    steps/lmrescore_const_arpa.sh \
      --cmd "$decode_cmd" data/lang_test_{tgsmall,tglarge} \
      data/$test exp/tri3b/decode_{tgsmall,tglarge}_$test
  done
echo "step completed"
fi

# Train a chain model
if [ $stage -le 9 ]; then
  local/chain/tuning/run_tdnn_1j.sh --stage 0
fi

# local/grammar/simple_demo.sh

# Don't finish until all background decoding jobs are finished.
wait
