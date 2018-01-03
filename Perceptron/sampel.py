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

if __name__=='__main__':

    imgHueLevels = []
    f = open('hueLevel.txt')
    for dataStr in f:
        hue = float(dataStr)
        imgHueLevels.append(hue)
    f.close()
    print imgHueLevels
