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

    x1_1 = readFile('urchinHues.txt')
    x1_2 = readFile('urchinHues.txt')
    x2_1 = readFile('brushHues.txt')
    x2_2 = readFile('brushHues.txt')
    c = np.ones(sample_num)

    x1 = np.c_[x1_1, x1_2, c]
    x2 = np.c_[x2_1, x2_2, c]
