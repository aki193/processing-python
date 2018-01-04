import cv2
import math
import numpy as np
from matplotlib import pyplot as plt
<<<<<<< Updated upstream

imgPath = []
images = []
imgCanny = []
corners = []

for i in range(1, 10):
    imgPath.append("data/pic0"+str(i)+".jpg")

for i in range(10, 61):
    imgPath.append("data/pic"+str(i)+".jpg")

#画像をグレースケールで読み込む
for i in range(60):
    images.append(cv2.imread(imgPath[i]))
# img = cv2.imread("data/pic34.jpg",0)

#画像をエッジを抽出
for i in range(60):
    imgCanny.append(cv2.Canny(images[i],500,550))

for i in range(60):
    corners = cv2.goodFeaturesToTrack(imgCanny[i],100,0.1,15)
    corners = np.array(corners)

cornersPoint = 0
for i in range(60):
    for corners in imgCanny[i]:
        x,y = a.ravel()
        cv2.circle(imgCanny[i],(x,y),3, 100, -1)
        cornersPoint += 1
#
print(cornersPoint)
plt.imshow(imgCanny),plt.show()
#
=======

imgPath = []
images = []
imgCanny = []
corners =[]

# 画像パスを生成
for i in range(1, 10):
    imgPath.append("data/pic0"+str(i)+".jpg")

for i in range(10, 41):
    imgPath.append("data/pic"+str(i)+".jpg")

# 画像の読み込む
for i in range(40):
    images.append(cv2.imread(imgPath[i],0))

for i in range(40):
    imgCanny.append(cv2.Canny(images[i],600,550))

for i in range(40):
    corners = cv2.goodFeaturesToTrack(imgCanny[i], 100, 0.01, 15)

    cornersPoint = 0
    for j in corners:
        cornersPoint += 1

    print("pic"+str(i+1),cornersPoint)
    # corners = np.array(corners)

# 画像をエッジを抽出
# cornersPoint = 0
# for i in corners:
#     x,y = i.ravel()
#     for i in range(40):
#         cv2.circle(imgCanny[i],(x,y), 3, 255, -1)
#

for i in range(40):
    cv2.imshow("image" + str(i+1), imgCanny[i])

>>>>>>> Stashed changes
cv2.waitKey(0)
