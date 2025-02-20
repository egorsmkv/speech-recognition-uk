#!/bin/bash

for x in exp/*/decode*; do [ -d $x ] && [[ $x =~ "$1" ]] && grep WER $x/wer_* | utils/best_wer.sh; done

for x in exp/chain/*/decode*; do [ -d $x ] && [[ $x =~ "$1" ]] && grep WER $x/wer_* | utils/best_wer.sh; done
exit 0



