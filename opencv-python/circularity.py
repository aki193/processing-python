import cv2
import math

#フォントの大きさ
fontscale = 1.0
#フォントカラー(B, G, R)
color=(0, 120, 238)
#フォント
fontface = cv2.FONT_HERSHEY_COMPLEX

OKBLUE = '\033[94m' # ターミナルで青文字を使うための値
OKGREEN = '\033[92m'# ターミナルで緑文字を使うための値

imgPath = []    # 画像のパス（String）
images = []     # 生成した画像(Image)
imgContours = []# 全ての画像の輪郭情報(Contour[])
imgContour = [] # １枚の画像の輪郭情報(Contour)
imgCircleLevels = [0 for i in range(60)]# 円形度情報(Double)

# 円形度計算
def calcCircleLevel (contour, area):
    perimeter = cv2.arcLength(contour, True)
    circle_level = 4.0 * math.pi * area / (perimeter * perimeter); # perimeter = 0 のとき気をつける
    return circle_level

# 画像パスを生成
for i in range(1, 10):
    imgPath.append("data/pic0"+str(i)+".jpg")

for i in range(10, 61):
    imgPath.append("data/pic"+str(i)+".jpg")

# 画像の読み込み
for i in range(60):
    images.append(cv2.imread(imgPath[i]))

# グレースケールへ変換後に２値化する
for i in range(60):
    imgGray = cv2.cvtColor(images[i],cv2.COLOR_BGR2GRAY)
    ret,imgThresh = cv2.threshold(imgGray,220,255,cv2.THRESH_BINARY)

# ２値化した画像から輪郭を取得
    imgTmp, contours, hierarchy = cv2.findContours(imgThresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    imgContours.append(contours)

# 円形度を計算して，輪郭を描画した画像を生成する
for i in range(60):
    for contour in imgContours[i]:
    # 輪郭の面積を算出
        area = cv2.contourArea(contour)
     # 輪郭があったら円形度を算出する（面積がある場合に処理をする．輪郭があっても面積が０の時があるため．）
        if area >= 2000 and area <= 70000:
            # 円形度を取得して配列に格納する
            level = calcCircleLevel(contour, area)
            imgCircleLevels[i] = level
            # 輪郭情報を描画した画像を配列に格納する
            imgContour.append(cv2.drawContours(images[i], contour, -1, (0, 255, 0), 3))
            # 中央にテキスト描く
            cv2.putText(images[i],str(level),(0,25),fontface,fontscale, color)
            # Logを出力
            print("No:" + str(i+1), OKBLUE + "Area = " + str(area), OKGREEN + "Level = " + str(level))
            break   # １度輪郭を取得したら次の画像を解析する

print(imgCircleLevels)

# TODO: 円形度情報からなんの標識なのかを判別する
for i in range(60):
    if imgCircleLevels[i] >= 0.8:
        cv2.putText(images[i],"Straight ahead or left turn permitted",(0,50),fontface,fontscale, color)
    elif imgCircleLevels[i] >= 0.7:
        cv2.putText(images[i],"Children crossing",(0,50),fontface,fontscale, color)
    elif imgCircleLevels[i] >= 0.5:
        cv2.putText(images[i],"Stop",(0,50),fontface,fontscale, color)
    else:
        cv2.putText(images[i],"None",(0,50),fontface,fontscale, color)
# 画像の表示
for i in range(60):
    cv2.imshow("image" + str(i+1), images[i])

# キーが入力されるまで終了しない
cv2.waitKey(0)
