class Color:
    RED, BLUE, YELLOW, NONE = range(1, 5)
    
imgColors = [Color.NONE for i in range(60)]
ImageArry = []
def setup():
    size(640, 360)
    imgPath = []
    
    #変数 num : 配列の長さnumberを意味
    #Path:画像のPath情報を表す変数
    for num in range(1, 10):  #pic01~09
        imgPath.append("pic0"+ str(num) + ".jpg")
    for num in range(10, 61):    #pic10~60
        imgPath.append("pic"+ str(num) + ".jpg")

    for num in range(60):
        ImageArry.append(loadImage(imgPath[num]))
    
    getColor() #色情報の取得
 
               
def draw():
    for y in range(6):
        for x in range(10):
            image(ImageArry[x+y*10], x*64, y*60, 64, 60)
    


         

def getColor():
    

#         if imgColor is Color.NONE:
#             print("image is NONE")
    
    loadPixels() #ピクセル配列にアクセスする前にpixelsを読み込む
    #enumerate: ループする際に配列の添字つきで要素を得る
    for index, img in enumerate(ImageArry):
        print "pic" + str(index + 1)
    
        
        #判断された色に+1するための変数
    
    
        redCount = 0
        yellowCount = 0
        blueCount = 0
    
        # 画像の縦・横のpixel値を読み取る
        for y in range(img.height):
            for x in range(img.width):
                loc = x + y *img.width #画像の読み込んでいる位置
    
                #pixel値の値をR,G,B値に分ける。
                r = red(img.pixels[loc])
                g = green(img.pixels[loc])
                b = blue(img.pixels[loc])
    
                if r != (255) and g != (255) and b != (255):
                    if r >=90  and g >= 90 and b <= 20:#Yellow Threshold
                        yellowCount += 1
                    elif r >= 100  and g <= 80 and b <= 80: #Red Threshold
                        redCount += 1
                    elif r <= 20 and g >= 60 and b >= 100: #Blue Threshold
                        blueCount += 1    
                    
                    
                    
        #判断した色を出力
    for imgColor in imgColors: 
        if yellowCount > blueCount: 
            imgColors[i] = Color.YELLOW
    #                 print(imgColors.YELLOW)
            if imgColors in Color.YELLOW:
                print("YELLOW")
    #             elif redCozunt > 10:
    #                 imgColors[i] = Color.RED
    #                 
    #             elif blueCount > yellowCount:
    #                 imgColors[i] = Color.BLUE
#         else:
    #             print "Could not parse:_("  
        
    updatePixels() #読み込んだpixelsの更新  
    
    

