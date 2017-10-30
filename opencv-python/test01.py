
import cv2
import math

# 円形度計算
def calcCircleLevel (contour, area):
    perimeter = cv2.arcLength(contour, True)
    circle_level = 4.0 * math.pi * area / (perimeter * perimeter); # perimeter = 0 のとき気をつける
    return circle_level

# 画像読み込み
imgOrigin = cv2.imread("data/pic45.jpg")
# グレースケールへ変換後に２値化する
imgGray = cv2.cvtColor(imgOrigin,cv2.COLOR_BGR2GRAY)
ret,imgThresh = cv2.threshold(imgGray,220,255,cv2.THRESH_BINARY)
# ２値化した画像から輪郭を取得
imgTmp, contours, hierarchy = cv2.findContours(imgThresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

# 取得した輪郭に対して処理を行う（輪郭は複数取れている）
for contour in contours:
    # 輪郭を（緑色で太さ３で <- 引数の値）描画する
    imgContour = cv2.drawContours(imgOrigin, contour, -1, (0, 255, 0), 3)
    # 輪郭の面積を算出
    area = cv2.contourArea(contour)
    print(area)
    # 輪郭があったら円形度を算出する（面積がある場合に処理をする．輪郭があっても面積が０の時があるため．）
    if area != 0:
        level = calcCircleLevel(contour, area)
        print(level)

cv2.imshow('image', imgContour)
cv2.imshow('image2', imgThresh)
cv2.waitKey(0)

