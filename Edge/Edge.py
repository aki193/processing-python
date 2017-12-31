import numpy as np
import cv2
from matplotlib import pyplot as plt

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
cv2.waitKey(0)
cv2.destroyAllWindows()
