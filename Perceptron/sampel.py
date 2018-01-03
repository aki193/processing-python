# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

def predict(wvec,xvec):
    out=np.dot(wvec,xvec)
    if out>=0:
        res=1
    else:
        res=-1
    return [res,out]

def train(wvec,xvec,label):
    [res,out]=predict(wvec,xvec)
    if out*label<0:
        wtmp=wvec+0.5*label*xvec
        return wtmp
    else:
        return wvec

def readFile(path):
    dataArray = []
    f = open(path)
    for dataStr in f:
        data = float(dataStr)
        dataArray.append(data)
    f.close()
    return dataArray

if __name__=='__main__':
    sample_num = 20
    init_wvec = [1, 1, -1]

    # ファイルから特徴量を読み込む
    x1_1 = readFile('urchinHues.txt')
    x1_2 = readFile('urchinHues.txt')
    x2_1 = readFile('brushHues.txt')
    x2_2 = readFile('brushHues.txt')
    # 第３項の値は1とする
    c = np.array(np.ones(sample_num))

    # 色相とエッジと３項目のデータを連結する
    x1 = np.c_[x1_1, x1_2, c]
    x2 = np.c_[x2_1, x2_2, c]

    # ループで扱いやすいようにx1とx2を連結しておく
    class_x = np.r_[x1, x2]

    # クラス分け（1: ウニ, 2: タワシ）
    label1 = np.ones(sample_num)
    label2 = -1 * np.ones(sample_num)
    label_x = np.array(np.r_[label1, label2])

    # 重みのarrayを作成
    wvec = np.empty((0,3), float)
    wvec = np.append(wvec, np.array([init_wvec]), axis = 0)
    wvec = np.append(wvec, np.array([init_wvec]), axis = 0)

    print wvec
