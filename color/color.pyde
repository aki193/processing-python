def setup():
    size(640, 360)
    global img
    img = loadImage("pic01.jpg")
    imageMode(CENTER)
    
def draw():
    background(255)
    image(img, width/2, height/2)

    
