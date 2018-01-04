# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

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

def plot(i, wvec):
    for w in wvec:
        plt.cla()
        x_fig=range(-15,16)
        y_fig=[-(w[1]/w[0])*xi-(w[2]/w[1]) for xi in x_fig]

        plt.scatter(x1[:,0],x1[:,1],marker='o',color='g',s=100)
        plt.scatter(x2[:,0],x2[:,1],marker='s',color='b',s=100)
        im = plt.plot(x_fig,y_fig)

if __name__=='__main__':

    item_num=100
    loop=1000
    init_wvec=[1,-1,1]
    isUpdate = True     # 収束判定
    ims = []


    x1_1=np.ones(int(item_num/2))+10*np.random.random(int(item_num/2))
    x1_2=np.ones(int(item_num/2))+10*np.random.random(int(item_num/2))
    x2_1=-np.ones(int(item_num/2))-10*np.random.random(int(item_num/2))
    x2_2=-np.ones(50)-10*np.random.random(int(item_num/2))
    z=np.ones(int(item_num/2))

    x1=np.c_[x1_1,x1_2,z]
    x2=np.c_[x2_1,x2_2,z]
    class_x=np.array(np.r_[x1,x2])
    label1=np.ones(int(item_num/2))
    label2=-1*np.ones(int(item_num/2))
    label_x=np.array(np.r_[label1,label2])

    wvec=np.vstack((init_wvec,init_wvec))

    # 重みベクトルが更新されている場合はループする
    while isUpdate:
        # 更新がない状態にする
        isUpdate = False
        for i in range(item_num):
            wvec_new=train(wvec[-1],class_x[i,:],label_x[i])
            # 重みベクトルの更新確認
            if not np.allclose(wvec[-1], wvec_new):
                isUpdate = True
            wvec=np.vstack((wvec,wvec_new))

    # w=wvec[-1]
    # print w

    fig = plt.figure()

    # for w in wvec:
    #     x_fig=range(-15,16)
    #     y_fig=[-(w[1]/w[0])*xi-(w[2]/w[1]) for xi in x_fig]
    #
    #     plt.scatter(x1[:,0],x1[:,1],marker='o',color='g',s=100)
    #     plt.scatter(x2[:,0],x2[:,1],marker='s',color='b',s=100)
    #     im = plt.plot(x_fig,y_fig)
    #     ims.append(im)

    # ani = animation.ArtistAnimation(fig, ims, interval=100)
    ani = animation.FuncAnimation(fig, plot, fargs=wvec, interval=100, frames=10)
    plt.show()

    # ims.append(im)
    # x_fig=range(-15,16)
    # y_fig=[-(w[1]/w[0])*xi-(w[2]/w[1]) for xi in x_fig]
    #
    # plt.scatter(x1[:,0],x1[:,1],marker='o',color='g',s=100)
    # plt.scatter(x2[:,0],x2[:,1],marker='s',color='b',s=100)
    # plt.plot(x_fig,y_fig)
    # plt.show()
