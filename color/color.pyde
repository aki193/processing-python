imges = []
def setup():
    size(640, 360)
    imgStr = []

    for num in range(1, 10):
        imgStr.append("pic0"+ str(num) + ".jpg")
    for num in range(10, 61):
        imgStr.append("pic"+ str(num) + ".jpg")

    for num in range(60):
        imges.append(loadImage(imgStr[num]))
    
    getColor() #色情報の取得
        
def draw():
    for y in range(6):
        for x in range(10):
            image(imges[x+y*10], x*64, y*60, 64, 60)
    
def getColor():
    loadPixels()#ピクセル配列にアクセスする前にpixelsを読み込む
    
    #enumerate: ループする際に配列の添字つきで要素を得る
    for index, img in enumerate(imges):
        print (index + 1)
<<<<<<< HEAD
       
       #判断された色に+1するための変数
=======
>>>>>>> master
        redCount = 0
        yellowCount = 0
        blueCount = 0

        # 画像の縦・横のpixel値を読み取る
        for y in range(img.height):
            for x in range(img.width):
                loc = x + y *img.width　#画像の読み込んでいる位置

                #pixel値の値をR,G,B値に分ける。
                r = red(img.pixels[loc])
                g = green(img.pixels[loc])
                b = blue(img.pixels[loc])

<<<<<<< HEAD
            
                if r != (255) and g != (255) and b != (255)
                    if r >=90  and g >= 90 and b <= 20:　#Yellow Threshold
                        yellowCount += 1

                    elif r >= 100  and g <= 80 and b <= 80:　#Red Threshold
                        redCount += 1
                        
                    elif r <= 20 and g >= 60 and b >= 100:　#Blue Threshold
                        blueCount += 1    

        
        if yellowCount > blueCount:
            print "It is Yellow...!?!?!?!?!?"     
        elif redCount > 10:
            print "It is Red...!?!?"
        elif blueCount > yellowCount:
            print "It is Blue...!?!?!?" 
        else:
            print "Could not parse:_("

                  
    updatePixels()#読み込んだpixelsの更新  
=======
                if r != (255) and g != (255) and b != (255):
                    
                    if r >=90  and g >= 130 and b <= 10:
                        redCount += 1
                        greenCount += 1

                    elif r >= 130  and g <= 60 and b <= 80:
                        redCount += 1
                        
                    elif r <= 20 and g >= 60 and b >= 100:
                        blueCount += 1    


                    
        if redCount > 10:
            print "It is Red...!?!?"
        elif blueCount > greenCount:
            print "It is Blue...!?!?!?" 
        elif greenCount > blueCount:
            print "It is Yellow...!?!?!?!?!?"
        else:
            print "Could not parse:_("
                    
    updatePixels()
>>>>>>> master

