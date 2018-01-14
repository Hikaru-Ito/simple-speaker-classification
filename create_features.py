# -*- coding:utf-8 -*-
from make_mfcc import convert_to_mfcc
import os
import json
import glob

# Voiceの読み込み
path = './Voice/'
dataset = []
for x in os.listdir(path):
    if os.path.isdir(path + x):
        dataset.append({'label': x, 'mfcc': []})

for d in dataset:
    print d['label']
    wavs = glob.glob(path+d['label']+'/*.wav')
    for w in wavs:
        mfcc = convert_to_mfcc(w)[0].tolist()
        d['mfcc'].append(mfcc)

# save
f = open('feature.json', 'w')
json.dump(dataset, f, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))
print '=========== DONE ============'


