
# mySketch imageOutput
img = []
imgStr = []
def setup():
    size(640, 360)
    for num in range(1, 10):
        imgStr.append("pic0" + str(num) + ".jpg")
        
    for num in range(10, 61):
        imgStr.append("pic" + str(num) + ".jpg")
        
    for num in range(60):
        img.append(loadImage(imgStr[num])) 
        
    imageMode(CENTER)

def draw():
    background(0, 102, 153)
    
    for y in range(6):
        for x in range(10):
            image(img[x+y*10], 32 + x*64, 30 + y*60, 64, 60)

