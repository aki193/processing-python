lt = []
[] = ar
[] = label
[] = es
[] = es2
lab = 1
cu = 0
def setup():
    size(640,360)    
    global img
    img = loadImage("pic01.jpg")
    img.loadPixels()
    loadPixels()
    
    imgsb = createImage(img.width, img.height, RGB)
    imageMode(CENTER)
    
    for y in range(1, pic0.height):
        for x in range(1, img.width-1):
            int(loc[,y* img.width + x])
            int(z[,0])
            int(loc2[,0])
            int([] tmp={60000,60000,60000,60000})
            
            if red(pic0.pixels[loc]) == 0:
                for ky in range(-1, 0):
                    if ky ==0 && ky == 1 break:
                        loc2 =(y + ky) * img.width + (x +ky)
                    if label[loc2] != 0:
                        tmp[z++] = label[loc2]
                    
                    label[loc] = min(tmp)
                    if label[loc] == 60000:
                        lavel[loc] = lab++
                    for k in range(0, tmp.length):
                        if tmp[k] != 60000:
                            lt[tmp[k]] = min(tmp)
                            
    for i in range(lab-1 , 0):
        int(t[,i])
        while t != lt[t]:
              t   = lt[t]
            #lt[i] = t
            
    for i in range(0, label.length):
        label[i] = lt[label[i]]
        
    ar = int(lab)
    es = int(lab)
    
    for i in range(0, label.length):
        if label[i] != 0:
            ar[label[i]]++
            if ar[lavel[i]] == 1:
                es[label[i]] = i
                
    for x in range(x, pic1.width):
        for y in range(y, pic1.height):
            int(loc[,x + y * pic01.width])
            if lavel[loc] != 0:
                pic01.pixels[loc] = color((200 * label[loc])%255,
                                          (140 * label[loc])%255,
                                          (160 * label[loc])%255)    
                        
def draw():
    image(img, width/2, height/2)   
    image(imgsb, width/2, height/2)
    imgsb.loadPixels();
    
    for i in range(0, ar.length):
        if ar[i] != 0:
            for y in range(0, imgsb.height):
                for x in range(0, imgsb.width):
                    int(loc[,y*imgsb.width + x])
                if loc == es[i]:
                    fill(0)
                    textSize(10)
                    text(ar[i],x/2+640,y/2+20)
        
