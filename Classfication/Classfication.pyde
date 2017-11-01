# PImage[] img = new PImage[2];
# PImage img1;
# PImage[] imgcf = new PImage[2];


# //Look Up Table
# int[] Src = new int[255];
# int[][] Dst = new int[2][10000];
img = []
imgcf = [2]
Src = [255]
Dst = ([2],[10000])

# float r,g,b;
# int[] p = new int[5];//{topleft, top, topright, left, center}
# int[][] la = new int[640][480];
# int min = 10000;
# int count=0;
# int[][] Scount = new int[2][256];

p = [5]
la = ([640],[480])
min = 10000
count = 0
Scount = ([2],[256])

def setup():
    global img1
    global c0
    global c1   
    global loc
    global r
    global g
    global b
   
    frameRate(30)
    for i in range(0, 2):
        img.append(loadImage("pic" +str(i)+"bin.jpg"))
#   img[0] = loadImage("pic0bin.jpg")
#   img[1] = loadImage("pic1bin.jpg")
    size(img[0].width, img[0].height)
#    size(640, 480)
    img[0].loadPixels()
    img[1].loadPixels()
    loadPixels()  
    
    for i in range(0, 2):
        imgcf.append(createImage(img[(i)].width, img[(i)].height, RGB))    
    
#     imgcf[0] = createImage(img[0].width, img[0].height, RGB)
#     imgcf[1] = createImage(img[1].width, img[1].height, RGB)
  
    for k in range(0, 2):
        for x in range(0, img[0].width):
            for y in range(0, img[0].height):
                la[x][y] = 0
  
        for i in range(0,255):
            Dst[k][i] = i

        for x in range(0, img[k].width):
            for y in range(0, img[k].height):
                loc = x + y*img[k].width 
  
#    for (int x = 0; x < img[k].width; x++) {
#       for (int y = 0; y < img[k].height; y++ ) {
#          int loc = x + y*img[k].width;

                r = red(img[k].pixels[loc])
                g = green(img[k].pixels[loc])
                b = blue(img[k].pixels[loc])
        
#          r = red (img[k].pixels[loc]);
#          g = green (img[k].pixels[loc]);
#          b = blue (img[k].pixels[loc]);

                if r < 15 and g < 15 and b < 15:
                    if x - 1 < 0 and y - 1 < 0:
                        p[0] = 0
                        p[1] = 0
                        p[2] = 0
                        p[3] = 0
                        p[4] = la[x][y]
                    elif x + 1 == img[k].width:
                        p[2] = 0
                        p[3] = la[x-1][y]
                        p[4] = la[x][y]
                        if y -1 < 0:
                            p[0] = 0
                            p[1] = 0
                        else:
                            p[0] = la[x-1][y-1]
                            p[1] = la[x][y-1]
                    elif y - 1 < 0:
                        p[0]=0
                        p[1]=0
                        p[2]=0
                        p[3]=la[x-1][y]
                        p[4]=la[x][y]
                    elif x - 1 < 0:    
                        p[0]=0
                        p[1]=la[x][y-1]
                        p[2]=la[x+1][y-1]
                        p[3]=0
                        p[4]=la[x][y]
                    else:
                        p[0]=la[x-1][y-1]
                        p[1]=la[x][y-1]
                        p[2]=la[x+1][y-1]
                        p[3]=la[x-1][y]
                        p[4]=la[x][y]
 
                if p[0] == 0 and p[1]==0 and p[2]==0 and p[3]==0:
                    count = count + 1
                    la[x][y] = count
                else:
                    min = 30000
                    for i in range(0, 5):
                        if p[i] < min and p[i] != 0:
                            min = p[i]
                for i in range(0, 5):
                    if p[i] != min and p[i] != 0:
                        Dsk[k][p[i]] = min
                la[x][y] = min                   

    for i in range(255,-1, -1):
        for x in range(0, img[k].width):
            for y in range(0, img[k].height):
                if la[x][y] == i:
                    la[x][y] = Dst[k][i] 
    
    for i in range(255, -1, -1):
        for x in range(0, img[k].width):
            for y in range(0, img[k].height):
                if la[x][y] == i:
                    Scount[k][255-i] = Scount[k][255-i]+1   
    
    c = 0
    for i in range(255, -1, -1):
        if Scount[k][i] > 30:
            print(255 - i +":pic["+ k +"]-"+ c +"="+ Scount[k][i])  
            c = c + 1
         
    for i in range(255, -1, -1):
        for x in range(0, img[k].width):
            for y in range (0, img[k].height): 
                loc = x + y * img[k].width
                if la[x][y] == i:
                    if k == 0:
                        if i == 0:
                            c0 = (255, 255, 255)   
                        else:
                            c0 = (255, i, 255-i*20)  
                        imgcf[0].pixels[loc] = c0
                    else:   
                        if i == 0:
                            c1 = (255, 255, 255) 
                        elif i == 91:
                            c1 = (0, 255, 255)  
                        elif i == 92:
                            c1 = (255, 0, 0)
                        elif i == 116:
                            c1 = (255, 255, 0)           
                        elif i == 206: 
                            c1 = (0,  255, 0)
                        elif i == 210:
                            c1 = (100, 100, 100)
                        elif i == 174:
                            c1 = (100, 200, 200)
                        elif i == 179:
                            c1 = (0, 0, 255)
                        else:
                            c1 = (0, 0, 0) 
                        imgcf[1].pixels[loc] = c1
    
    imgcf[0].save("data/pic0cf.jpg");
    imgcf[1].save("data/pic1cf.jpg");
    

def draw():
  
    image(img[0], 0, 0, 320, 240)
    image(img[1], 0, 240, 320, 240)
    image(imgcf[0], 320, 0, 320, 240)
    image(imgcf[1], 320, 240, 320, 240)


