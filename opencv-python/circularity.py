
import cv2
import math

imgPath = []
images = []

# 円形度計算
def calcCircleLevel (contour, area):
    perimeter = cv2.arcLength(contour, True)
    circle_level = 4.0 * math.pi * area / (perimeter * perimeter); # perimeter = 0 のとき気をつける
    return circle_level

for i in range(1, 10):
    imgPath.append(cv2.imread("data/pic0"+str(i)+".jpg"))

for i in range(10, 61):
    imgPath.append(cv2.imread("data/pic"+str(i)+".jpg"))

for i in range(60):
    images.append(imgPath[i])

# グレースケールへ変換後に２値化する
for i in range(60):
    imgGray = cv2.cvtColor(images[i],cv2.COLOR_BGR2GRAY)
    ret,imgThresh = cv2.threshold(imgGray,220,255,cv2.THRESH_BINARY)
# ２値化した画像から輪郭を取得
    imgTmp, contours, hierarchy = cv2.findContours(imgThresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

# 取得した輪郭に対して処理を行う（輪郭は複数取れている）
for i in range(60):
    for contour in contours:
    # 輪郭を（緑色で太さ３で <- 引数の値）描画する
        imgContour = cv2.drawContours(images[i], contour, -1, (0, 255, 0), 3)
    # 輪郭の面積を算出
        area = cv2.contourArea(contour)
        print(area)
     # 輪郭があったら円形度を算出する（面積がある場合に処理をする．輪郭があっても面積が０の時があるため．）
        if area != 0:
            level = calcCircleLevel(contour, area)
            print(level)
# 画像の表示
for i in range(1, 61):
    cv2.imshow("image contour"+str(i), imgContour)
    cv2.imshow("image threshold"+str(i), imgThresh)

# キーが入力されるまで終了しない
cv2.waitKey(0)
