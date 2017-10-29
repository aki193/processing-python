add_library('opencv_processing')

def setup():
    size(960, 480)
    frameRate(30)
    
    global img

    img = loadImage("pic01.jpg")
    
    opencv0 = OpenCV(this, img)
        
def draw():
#   background(0,0,0)

    def calcCircleLevel (contour, area):
        perimeter = opencv0.arcLength(contour, True)
        circle_level = 4.0 * math.pi * area / (perimeter * perimeter); # perimeter = 0 のとき気をつける
        return circle_level

    image(img,0,0,320,240)
#    image(img1, 320, 0, 320, 240)
