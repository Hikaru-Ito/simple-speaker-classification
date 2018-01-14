# -*- coding:utf-8 -*-
import os


TEXT_FILE = './speech_text.txt'
with open(TEXT_FILE) as f:
    texts = f.read().splitlines()

SPEAKERS = [
    'Alex',
    'Fred',
    'Victoria',
    'Kyoko',
    'Otoya',
    'Tom',
    'Ralph',
    'Vicki',
    'Susan',
    'Princess',
    'Ava',
    'Allison',
    'Agnes'
]
SENTENCES = texts[:50]

for speaker in SPEAKERS:
    dir_name = './Voice/'+speaker
    print 'generating > '+speaker
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    for i, sentence in enumerate(SENTENCES):
        os.system('say -v {SPEAKER} -o Voice/{SPEAKER}/{Number}.wav --data-format=LEF32@22050 "{TEXT}"'.format(
            SPEAKER=speaker,
            Number=i,
            TEXT=sentence
        ))