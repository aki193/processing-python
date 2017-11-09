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
        
    getColor()
        
def draw():
    for y in range(6):
        for x in range(10):
            image(imges[x+y*10], x*64, y*60, 64, 60)
            


def getColor():
# loadPixels()//ピクセル配列にアクセスする前にpixelsを読み込む
# updatePixels()//読み込んだpixelsの更新
    loadPixels()
    
# R, G, Bの値を取得し+1するための変数?
    redCount = 0
    greenCount = 0
    blueCount = 0
  
    for index, img in enumerate(imges):
        print (index + 1)
        for y in range(img.height):
            for x in range(img.width):
                loc = x + y *img.width
                    
                r = red(img.pixels[loc])
                g = green(img.pixels[loc])
                b = blue(img.pixels[loc])


    pixels[loc] = color(r, g, b)

# 判断した色を+1する。
#    if r >= 90  and g <= 70 and b <= 80:
#        redCount += 1
#        print "Red = "+ str(redCount) + ", Green = " + str(greenCount) + ", Blue = " + str(blueCount)
#    elif r >=90  and g >= 70 and b <= 10:
#        redCount += 1
#        greenCount += 1
#        print "Red = "+ str(redCount) + ", Green = " + str(greenCount) + ", Blue = " + str(blueCount)
#    elif r <= 0 and g <= 60 and b >= 100:
#        blueCount += 1
#        print "Red ="+ str(redCount) + ", Green = " + str(greenCount) + ", Blue = " + str(blueCount)
#                    
#    if redCount > 100:
#        print "It is Red...!?!?"
#     elif blueCount > greenCount:
#        print "It is Blue...!?!?!?" 
#     elif greenCount > blueCount:
#        print "It is Yellow...!?!?!?!?!?"
#     else:
#        print "It is White...!"
#                     
    updatePixels()
                
