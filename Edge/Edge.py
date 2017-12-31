import numpy as np
import cv2
from matplotlib import pyplot as plt
# imgPath = []
# images = []

#画像をグレースケールで読み込む
img = cv2.imread("data/pic34.jpg",0)

#画像をエッジを抽出
imgCanny = cv2.Canny(img,200,255)

hist = cv2.calcHist([imgCanny],[0],None,[256],[0,256])

print(hist)

plt.xlim(0,255)
plt.plot(hist)
plt.xlabel("Pixel value", fontsize = 20)
plt.ylabel("Number of pixels", fontsize = 20)
plt.grid()
plt.show()



cv2.namedWindow("imge", cv2.WINDOW_NORMAL)
cv2.imshow("imge",imgCanny)
cv2.waitKey(0)
cv2.destroyAllWindows()

#
# # 画像パスの生成（pic1~9）
# for i in range(1,10):
#     imgPath.append("data/pic0"+str(i)+".jpg")
#
# # 画像パスの生成(pic10~60)
# for i in range(10, 61):
#     imgPath.append("data/pic"+str(i)+".jpg")
#
# # 画像の読み込み（pic1~60）
# for i in range(60):
#     images.append(cv2.imread(imgPath[i]))
