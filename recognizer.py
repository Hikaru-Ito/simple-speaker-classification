# -*- coding:utf-8 -*-
import sys
import json
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.svm import SVC
from sklearn import tree

from make_mfcc import convert_to_mfcc


# データのインポート
f = open('feature.json', 'r')
dataset = json.load(f)

x = []
y = []
for i,v in enumerate(dataset):
    for mfcc in v['mfcc']:
        x.append(mfcc)
        y.append(i)

# テストデータと訓練データの作成
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
print len(y_train), len(y_test)


# ランダムフォレストの分類器を作成
rforest_clf = RandomForestClassifier(random_state=7747)
rforest_clf.fit(x_train, y_train)

# 決定木の分類機を作成
dtree_clf = tree.DecisionTreeClassifier(random_state=7747)
dtree_clf.fit(x_train, y_train)

# SVMの分類機を作成
svm_clf = SVC(kernel='rbf').fit(x_train, y_train)


def testing():
    y_pred = rforest_clf.predict(x_test)
    print "RandomForest => ", (metrics.accuracy_score(y_test, y_pred))

    y_pred = dtree_clf.predict(x_test)
    print "DecisionTreeClassifier => ", (metrics.accuracy_score(y_test, y_pred))

    y_pred = svm_clf.predict(x_test)
    print "SVM => ", (metrics.accuracy_score(y_test, y_pred))


def analyze(wav):
    m = convert_to_mfcc(wav)
    print '================================'
    y_pred = rforest_clf.predict(m)
    print "RandomForest => ", dataset[y_pred[0]]['label']

    y_pred = dtree_clf.predict(m)
    print "DecisionTreeClassifier => ", dataset[y_pred[0]]['label']

    y_pred = svm_clf.predict(m)
    print "SVM => ", dataset[y_pred[0]]['label']
    print '================================'


# 引数に、wavfileがあれば、学習後、名前を出す
args = sys.argv
if len(args) >= 2:
    analyze(args[1])
else:
    testing()