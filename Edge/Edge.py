import cv2
import math
import numpy as np
from matplotlib import pyplot as plt

imgPath = []
images = []
imgCanny = []
corners =[]

# 画像パスを生成
for i in range(1, 10):
    imgPath.append("data/pic0"+str(i)+".jpg")

for i in range(10, 41):
    imgPath.append("data/pic"+str(i)+".jpg")

# 画像の読み込み
for i in range(40):
    images.append(cv2.imread(imgPath[i],0))

for i in range(40):
    imgCanny.append(cv2.Canny(images[i],600,650))
    
f = open('cornersLevel.txt', 'w')
for i in range(40):
    corners = cv2.goodFeaturesToTrack(imgCanny[i], 100, 0.01, 15)

    cornersPoint = 0
    for j in corners:
        cornersPoint += 1
   
    print("pic"+str(i+1),cornersPoint)
    f.write(str(cornersPoint) + '\n')
f.close()

for i in range(40):
	cv2.imshow("imgCanny" + str(i + 1), imgCanny[i])
    
cv2.waitKey(0)
