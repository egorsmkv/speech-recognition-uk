#!/bin/bash

# path to directory where model path will placed

dir="${1:-$HOME}"
echo "$dir"
if [ ! -d "$dir/model" ]
then
  mkdir -p "$dir/model/ivector"
fi

cp exp/chain/tdnn1*_sp_online/ivector_extractor/final.dubm "$dir/model/ivector"
cp exp/chain/tdnn1*_sp_online/ivector_extractor/final.ie "$dir/model/ivector"
cp exp/chain/tdnn1*_sp_online/ivector_extractor/final.mat "$dir/model/ivector"
cp exp/chain/tdnn1*_sp_online/ivector_extractor/global_cmvn.stats "$dir/model/ivector"
cp exp/chain/tdnn1*_sp_online/ivector_extractor/online_cmvn.conf "$dir/model/ivector"
cp exp/chain/tdnn1*_sp_online/ivector_extractor/splice_opts "$dir/model/ivector"
cp exp/chain/tdnn1*_sp_online/conf/splice.conf "$dir/model/ivector"

cp exp/chain/tree_sp/graph_tgsmall/HCLG.fst "$dir/model"
cp exp/chain/tree_sp/graph_tgsmall/words.txt "$dir/model"
cp exp/chain/tree_sp/graph_tgsmall/phones/word_boundary.int "$dir/model"
cp exp/chain/tdnn1*_sp_online/conf/mfcc.conf "$dir/model"
cp exp/chain/tdnn1*_sp_online/final.mdl "$dir/model"
