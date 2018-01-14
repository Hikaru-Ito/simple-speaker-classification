# -*- coding:utf-8 -*-
import json
import pyaudio
import numpy as np
import audioop
from scikits.talkbox.features import mfcc
import make_mfcc

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn import tree


# データのインポート
f = open('feature.json', 'r')
dataset = json.load(f)

x = []
y = []
for i,v in enumerate(dataset):
    for m in v['mfcc']:
        x.append(m)
        y.append(i)


# テストデータと訓練データの作成
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# ランダムフォレストの分類器を作成
rforest_clf = RandomForestClassifier(random_state=7747)
rforest_clf.fit(x_train, y_train)

# 決定木の分類機を作成
dtree_clf = tree.DecisionTreeClassifier(random_state=7747)
dtree_clf.fit(x_train, y_train)

# SVMの分類機を作成
svm_clf = SVC(kernel='rbf').fit(x_train, y_train)


CHUNK = 512
RATE = 44100
p = pyaudio.PyAudio()

stream = p.open(
    format=pyaudio.paInt16,
    channels=1,
    rate=RATE,
    input=True,
    output=False,
    frames_per_buffer=CHUNK
)


audio_buffer = []
no_sounds = 0

def calc_mfcc(audio_buf):
    mfcc_list = [flatten for inner in audio_buf for flatten in inner]
    return make_mfcc.convert_center_mfcc(mfcc_list)

while stream.is_active():
    data = stream.read(CHUNK)
    rms = audioop.rms(data, 2)
    if rms > 60:
        sig = np.frombuffer(data, dtype="int16")
        ceps, mspec, spec = mfcc(sig)
        audio_buffer.append(ceps)
    else:
        no_sounds += 1

    if no_sounds > 240:
        no_sounds = 0

    if len(audio_buffer) == 80:
        c_mfcc = calc_mfcc(audio_buffer)
        y_pred = rforest_clf.predict([c_mfcc])
        label = dataset[y_pred[0]]['label']
        print label
        audio_buffer = []