#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, json
import csv

line_id = 1
for line in sys.stdin:
    line_id += 1
    try:
        tweets = json.loads(line)
    except(ValueError):
        continue
    for tweet in tweets:
        if 'text' in tweet:
            print('{0}\t{1}'.format(tweet['id']\
    ,'\\n'.join(tweet['text'].split('\n'))))
