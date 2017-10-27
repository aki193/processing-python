
# mySketch imageOutput
img = [] #Image
def setup():
    size(640, 360)
    
    imgStr = [] #String

    for num in range(1, 10):
        imgStr.append("pic0" + str(num) + ".jpg")
        
    for num in range(10, 61):
        imgStr.append("pic" + str(num) + ".jpg")
        
    for num in range(60):
        img.append(loadImage(imgStr[num])) 
        
def draw():    
    for y in range(6):
        for x in range(10):
            image(img[x+y*10], x*64, y*60, 64, 60)

