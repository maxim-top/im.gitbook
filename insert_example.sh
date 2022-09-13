#!/bin/bash
cur_dir=`pwd`
repos=(lanying-im-embedded lanying-im-embedded lanying-im-android lanying-im-android lanying-im-ios lanying-im-ios)
paths=(en/reference/floo zh-hans/reference/floo en/reference/floo-android \
 zh-hans/reference/floo-android en/reference/floo-ios zh-hans/reference/floo-ios)
num=${#paths[*]}

for i in `seq 0 $((num-1))`
do
    path=${paths[i]}
    files=`find $path -name "*.md"|sed "s:^:$cur_dir/:"`
    for f in $files
    do
        python insert_example.py ${repos[i]} "$f"
    done
done
