import numpy as np
import cv2

imgPath = []
images = []

#定数定義
# ORG_WINDOW_NAME = "org"
# GRAY_WINDOW_NAME = "gray"
# CANNY_WINDOW_NAME = "canny"
#
# ORG_FILE_NAME = "org.jpg"
# GRAY_FILE_NAME = "gray.png"
# CANNY_FILE_NAME = "canny.png"

# 画像パスを生成
for i in range(1, 10):
    imgPath.append("data/pic0"+str(i)+".jpg")

for i in range(10, 61):
    imgPath.append("data/pic"+str(i)+".jpg")

#画像の読み込み
for i in range(60):
    images.append(cv2.imread(imgPath[i]))

#グレースケールに変換
for i in range(60):
    imgGray = cv2.cvtColor(images[i], cv2.COLOR_BGR2GRAY)

# エッジ抽出
for i in range(60):
    imgCanny = cv2.Canny(imgGray,50,110,cv2.COLOR_BGR2GRAY)

# # ウィンドウに表示
# #cv2.namedWindow(ORG_WINDOW_NAME)
# #cv2.namedWindow(GRAY_WINDOW_NAME)
# cv2.namedWindow(CANNY_WINDOW_NAME)
#
# #cv2.imshow(ORG_WINDOW_NAME, org_img)
# #cv2.imshow(GRAY_WINDOW_NAME, gray_img)
# cv2.imshow(CANNY_WINDOW_NAME, canny_img)
#
# # ファイルに保存
# cv2.imwrite(GRAY_FILE_NAME, gray_img)
# cv2.imwrite(CANNY_FILE_NAME, canny_img)
#
# # 終了処理
# cv2.waitKey(0)
# cv2.destroyAllWindows()
