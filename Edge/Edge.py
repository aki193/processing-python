import numpy as np
import cv2
from matplotlib import pyplot as plt
# imgPath = []
# images = []

#画像をグレースケールで読み込む
img = cv2.imread("data/pic34.jpg",0)

#画像をエッジを抽出
imgCanny = cv2.Canny(img,500,550)

corners = cv2.goodFeaturesToTrack(imgCanny,100,0.1,15)
corners = np.int0(corners)

cornersPoint = 0
for i in corners:
    x,y = i.ravel()
    cv2.circle(imgCanny,(x,y),3, 100, -1)
    cornersPoint += 1

print(cornersPoint)
plt.imshow(imgCanny),plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
