# import codecs
# class Color:
#     RED, BLUE, YELLOW, NONE = range(1, 5)
#         
#imgColors = [Color.NONE for i in range(60)]
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
#     exportColorData()
    
 
               
def draw():
    for y in range(2):
        for x in range(10):
            image(ImageArry[x+y*10], x*64, y*60, 64, 60)
    


         

def getColor():
    
    loadPixels() #ピクセル配列にアクセスする前にpixelsを読み込む
    #enumerate: ループする際に配列の添字つきで要素を得る
    for index, img in enumerate(ImageArry):
        print ("pic" + str(index + 1))

        #判断された色に+1するための変数
        redCount = 0
        yellowCount = 0
        blueCount = 0
    
        # 画像の縦・横のpixel値を読み取る
        for y in range(img.height):
            for x in range(img.width):
                loc = x + y *img.width #画像の読み込んでいる位置
    
                #pixel値の値をR,G,B値に分ける。
                h = hue(img.pixels[loc])
                s = saturation(img.pixels[loc])
                b = brightness(img.pixels[loc])
                
                if h != 0 and s != 0 and b != 0:
                    print(h) 

#                     
#         #判断した色を出力
#         if yellowCount > blueCount: 
#             print("It is YELLOW")
#             imgColors[index] = Color.YELLOW
#         
#         elif redCount > 10:
#             print("It is RED")
#             imgColors[index] = Color.RED      
#         
#         elif blueCount > yellowCount:
#             print("It is BLUE")
#             imgColors[index] = Color.BLUE
#         else:
#             print "Could not parse:_("  
#             imgColors[index] = Color.NONE
#         
#     updatePixels() #読み込んだpixelsの更新  
#     
# 
# def exportColorData():
#     f = codecs.open('write.txt', 'w', 'shift_jis')
#     i = 0
#     for x in imgColors:
#         i = i + 1
#         f.write ("pic" + str(i)+"\n")
#         if x == 1:
#             f.write("It is RED\n")
#         elif x == 2:
#             f.write("It is BLUE\n")
#         elif x == 3:
#             f.write("It is YELLOW\n")
#         elif x == 4:
#             f.write("It is NONE\n")
#     
#     f.close()
