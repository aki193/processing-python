def setup():
    size(640, 360)
    global img, imgsb
    img = loadImage("pic01.jpg")
    imgsb = createImage(img.width, img.height, RGB)
    imageMode(CENTER)
    getColor()
    #
def draw():
    background(150)
    image(img, width/2, height/2)
    
    
def getColor():
#loadPixels()//ピクセル配列にアクセスする前にpixelsを読み込む
#updatePixels()//読み込んだpixelsの更新
    loadPixels()
    img.loadPixels()
#R, G, Bの値を取得し+1するための変数?
    redCount = 0
    greenCount = 0
    buleCount = 0
    
    for y in range(0, img.height):
        for x in range(0, img.width):
            loc = x + y*img.width
            
            r = red(img.pixels[loc])
            g = green(img.pixels[loc])
            b = blue(img.pixels[loc])
            if r != 255 and g != 255 and b != 255:
                print(r, g, b)
            pixels[loc] = color(r, g, b)
# 判断した色を+1する。
            if r >= 100 and g <= 70 and b <= 50:
                redCount += 1
                print "R="+ str(redCount) + ", G=", + str(greenCount) + ", B=" + str(buleCount)       
            elif r <= 0 and g <= 60 and b >= 100:
                greenCount += 1
                print "R="+ str(redCount) + ", G=" + str(greenCount) + ", B=" + str(buleCount)
            elif r >=100  and g >= 80 and b <= 0:
                redCount += 1
                greenCount += 1
                print "R="+ str(redCount) + ", G=" + str(greenCount) + ", B=" + str(buleCount)
                
                
    updatePixels()
