
import cv2
import math

def calcCircleLevel (contour, area):
    perimeter = cv2.arcLength(contour, True)
    circle_level = 4.0 * math.pi * area / (perimeter * perimeter); # perimeter = 0 のとき気をつける
    return circle_level

im = cv2.imread("data/pic45.jpg")


imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
#ret,thresh = cv2.threshold(imgray,20,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)
ret,thresh = cv2.threshold(imgray,220,255,cv2.THRESH_BINARY)
#image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
for contour in contours:
    img = cv2.drawContours(im, contour, -1, (0, 255, 0), 3)
    area = cv2.contourArea(contour)
    print(area)
    if area != 0:
        level = calcCircleLevel(contour, area)
        print(level)
#img = cv2.drawContours(im, contours[], -1, (0, 255, 0), 3)

#img = cv2.drawContours(image, contours[0], -1, (0,255,0), 3)

cv2.imshow('image', img)
cv2.imshow('image2', thresh)
cv2.waitKey(0)

