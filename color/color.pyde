
def getColor():
    loadPixels()
#     imgsb.loadPixels()
    img.loadPixels()
    for y in range(0, img.height):
        for x in range(0, img.width):
            loc = x + y*img.width
            
            r = red(img.pixels[loc])
            g = green(img.pixels[loc])
            b = blue(img.pixels[loc])
            if r != 255 and g != 255 and b != 255:
                print(r, g, b)
            pixels[loc] = color(r, g, b)
            
    if r >= 200 and g <= 20 and b <= 20:
        print("Image is RED!!!")
    elif r <= 30 and g <= 40 and b >= 200:
        print("Image is BLUE!?")   
    elif (r >= 130 , g >= 130 , b <= 20):
        print("Image is GREEN!?!?")
    else:
        print("Image is White!?!?!?")
        return(I)
    updatePixels()
    
    #image(imgsb, width, height)
        
def setup():
    size(640, 360)
    global img, imgsb
    img = loadImage("pic01.jpg")
    imgsb = createImage(img.width, img.height, RGB)
    imageMode(CENTER)
    getColor()
    
def draw():
    background(150)
    image(img, width/2, height/2)
    
