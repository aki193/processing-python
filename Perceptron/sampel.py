# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

"""
:param type arg1: description
:param type arg2: description
y=w'xを計算している
正ならlabelを1と判定する（ウニ）
負ならlabelを2と判定する（タワシ）
"""
def predict(wvec, xvec):
    out = np.dot(wvec, xvec)
    if out >= 0:
        res = 1
    else:
        res = -1
    return [res, out]

"""
:param type arg1: description
:param type arg2: description
:param type arg3: description
計算結果とラベル判定が負の時（誤認識した時）に重みを修正する
正常な認識の場合は重みをそのまま返す
"""
def train(wvec, xvec, label):
    [res, out] = predict(wvec, xvec)
    if out * label < 0:
        wtmp = wvec + 0.5 * label * xvec
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
    sample_num = 40
    init_wvec = [-1, -1, 1]

    # ファイルから特徴量を読み込む
    x1_1 = readFile('urchinHues.txt')
    x1_2 = readFile('brushHues.txt')
    x2_1 = readFile('brushHues.txt')
    x2_2 = readFile('urchinHues.txt')
    # x1_1=np.ones(int(sample_num/2))+10*np.random.random(int(sample_num/2))
    # x1_2=np.ones(int(sample_num/2))+10*np.random.random(int(sample_num/2))
    # x2_1=-np.ones(int(sample_num/2))-10*np.random.random(int(sample_num/2))
    # x2_2=-np.ones(int(sample_num/2))-10*np.random.random(int(sample_num/2))

    # 第３項の値は1とする
    c = np.array(np.ones(sample_num/2))

    # 色相とエッジと３項目のデータを連結する
    x1 = np.c_[x1_1, x1_2, c]
    x2 = np.c_[x2_1, x2_2, c]

    # ループで扱いやすいようにx1とx2を連結しておく
    class_x = np.r_[x1, x2]

    # クラス分け（1: ウニ, 2: タワシ）
    label1 = np.ones(sample_num/2)
    label2 = -1 * np.ones(sample_num/2)
    label_x = np.array(np.r_[label1, label2])

    # 重みのarrayを作成
    wvec = np.empty((0,3), float)
    wvec = np.append(wvec, np.array([init_wvec]), axis = 0)
    wvec = np.append(wvec, np.array([init_wvec]), axis = 0)

    # array[-1]は最後尾を取得している(array.lastと同義)
    # array[1, :]の`:`は以降の添え字を省略している
    for j in range(1):
        for i in range(sample_num):
            wvec_new = train(wvec[-1], class_x[i], label_x[i])
            wvec = np.append(wvec, np.array([wvec_new]), axis = 0)
        print wvec
    w = wvec[-1]
    print w

    x_fig=range(-15, 15)
    y_fig=[-(w[1]/w[0])*xi-(w[2]/w[1]) for xi in x_fig]
    plt.scatter(x1[:,0],x1[:,1],marker='o',color='g',s=100)
    plt.scatter(x2[:,0],x2[:,1],marker='s',color='b',s=100)
    plt.plot(x_fig,y_fig)

    plt.show()
