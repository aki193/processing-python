import codecs
lines = [] #String
line_index = 0

sampleN = 60
clusterN = 3

sample = []      # PVector
cluster = []     # int
prevCluster = [] # int

center = [] # 重心座標 PVector(x, y座標)
key_pressed_sign = False

# 画面に広く表示されるようにバイアス変数を用意する
hueBias = 3
circleBias = 800

# 特徴量を取得して円，三角，四角
imgHueLevels = [0 for i in range(60)]
imgCircleLevels = [0 for i in range(60)]

# 青，赤，黄
clusterHueLevels = [140.0 * hueBias, 220.0 * hueBias, 60.0 * hueBias]
# 円形，三角，四角
clusterCircleLevels = [int(0.8 * circleBias), int(0.7 * circleBias), int(0.5 * circleBias)]

# サンプル画像のパスと格納される配列
imgPath = []
imageArray = []

def setup():
    size (800, 800, P2D)
    smooth()    
    
    #Path:画像のPath情報を取得
    for num in range(1, 10):  #pic01~09
        imgPath.append("pic0"+ str(num) + ".jpg")
    for num in range(10, 61):    #pic10~60
        imgPath.append("pic"+ str(num) + ".jpg")
    
    #画像読み込み
    for num in range(60):
        imageArray.append(loadImage(imgPath[num]))

    # 色相データの読み込み（画面に広くプロットされるようにバイアスをかける）
    for index, dataStr in enumerate(open('hueLevel.txt', 'r')):
        data = float(dataStr)
        imgHueLevels[index] = int(data * hueBias)
        
    # 円形度データの読み込み（画面に広くプロットされるようにバイアスをかける）    
    for index, dataStr in enumerate(open('circleLevel.txt', 'r')):
        data = float(dataStr)
        imgCircleLevels[index] = int(data * circleBias)

    # 2つの特徴量のデータをプロットする
    for i in range(sampleN):
        sample.append(PVector(imgCircleLevels[i], imgHueLevels[i]))
    # サンプルデータより重心をプロットする
    for i in range(clusterN):
        center.append(PVector(clusterHueLevels[i], clusterCircleLevels[i]))
        
    # クラスタデータを3つの値をランダムで格納する
    for i in range(sampleN):
        cluster.append(i % clusterN)
        prevCluster.append(-1)
    
    key_pressed_sign = False

def draw():
    background(0)
    global key_pressed_sign
    if key_pressed_sign is True:
        clustering()
        key_pressed_sign = False
    
    for i in range(sampleN):
        
        image(imageArray[i], sample[i].x, sample[i].y, 30, 30)
        pushMatrix()
        if cluster[i] == 0:
            stroke(255, 255, 0)
        elif cluster[i] == 1:
            stroke(255, 0, 0)
        elif  cluster[i] == 2:
            stroke(0, 255, 255)
            
        noFill()
        rect(sample[i].x, sample[i].y, 20, 20)
        popMatrix()

    for i in range(clusterN):
        pushMatrix()
        
        if i == 0:
            fill(255, 255, 0)
        elif i == 1:
            fill(255, 0, 0)
        elif i == 2:
            fill(0, 255, 255)
            
        noStroke()
        ellipse(center[i].x, center[i].y, 30, 30)
        popMatrix()
        
def clustering():
    e = False
    for i in range(sampleN):
        if prevCluster[i] != cluster[i]:
            e = True
            
    if e is True:
        for i in range(sampleN):
            prevCluster[i] = cluster[i]
        
        for i in range(sampleN):
            max_cluster = -1
            max_value = width * height
            
            for j in range(clusterN):
                if max_value > PVector.dist(sample[i], center[j]):
                    max_value = PVector.dist(sample[i], center[j])
                    max_cluster = j
                    
            cluster[i] = max_cluster
            
            for j in range(clusterN):
                cn = 0
                cx = 0
                cy = 0
                
                for i in range(sampleN):
                    if cluster[i] == j:
                        cx = cx + sample[i].x
                        cy = cy + sample[i].y
                        cn += 1
                        
                if cn != 0:
                    center[j].x = cx/cn
                    center[j].y = cy/cn

def keyPressed():
    global key_pressed_sign
    key_pressed_sign = True
