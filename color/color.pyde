def setup():
    size(640, 360)
    global img, imgsb
    img = loadImage("pic01.jpg")
    imgsb = createImage(img.width, img.height, RGB)
    imageMode(CENTER)
    
def draw():
    background(150)
    #image(img, width/4, height/4)
    
    loadPixels()
    imgsb.loadPixels()
    for y in range(0, imgsb.height):
        for x in range(0, imgsb.width):
            loc = x + y*imgsb.width
            
            r = red(imgsb.pixels[loc])
            g = green(imgsb.pixels[loc])
            b = blue(imgsb.pixels[loc])
            
            pixels[loc] = color(r, g, b)
            
    #if r >= 200 and g <= 20 and b <= 20:
     #   print("r")
      #  return r
        #return(255, 0, 0)
        
    #elif r <= 30 and g <= 40 and b >= 200:
     #   print("blue")   
      #  return(0, 0, 255)                
               
    #elif (R >= 130 , G >= 130 , B <= 20):
     #   print("blue")
      #  return(255, 255, 0)
    #else:
     #   return(0 ,0 ,0)
    
    updatePixels()
    
    #image(imgsb, width, height)
    

    
