def setup():
    size(640, 360)
    global img, imgsb
    img = loadImage("pic01.jpg")
    imgsb = createImage(img.width, img.height, RGB)
    imageMode(CENTER)
    
def draw():
    background(150)
    #image(img, width/2, height/2)
    
    #x = int(imgsb.width)
    #y = int(imgsb.height)
    #pix_R = imgsb.get(x, y)
    #pix_G = imgsb.get(x, y)
    #pix_B = imgsb.get(x, y)
    
    loadPixels()
    imgsb.loadPixels()
    for x in xrange(imgsb.width):
        for y in xrange(img.height):
            loc = x + y*imgsb.width
            
            R = red(imgsb.pixels[loc])
            G = green(imgsb.pixels[loc])
            B = blue(imgsb.pixels[loc])
            
            imgsb.pixels[loc] = color(R, G, B)
            updatePixels()
