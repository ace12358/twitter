#!/bin/bash
while read x; do
    php tweetid2json.php $x | python json_reader3.4.3.py
    sleep 6
done < $1
