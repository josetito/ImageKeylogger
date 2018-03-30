import numpy as np
import cv2
import pytesseract
from PIL import Image

'''
que hace?
abre una imagen y le aplica ciertas funciones que ayudan. 

aca estoy jugando con los contornos y la saturacion de una imagen para identificar 
donde me debo centrar para sacar la informacion de ahi.
'''

rawImage = cv2.imread('./imagenes/menu.png')
#cv2.imshow('Original Image',rawImage)
#cv2.waitKey(0)

hsv = cv2.cvtColor(rawImage, cv2.COLOR_BGR2HSV)
#cv2.imshow('HSV Image',hsv)
#cv2.waitKey(0)

hue ,saturation ,value = cv2.split(hsv)
#cv2.imshow('Saturation Image',saturation)
#cv2.waitKey(0)
#cv2.imwrite("tracing.png", saturation)

#retval, thresholded = cv2.threshold(saturation, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
#cv2.imshow('Thresholded Image',thresholded)
#cv2.waitKey(0)

#medianFiltered = cv2.medianBlur(thresholded,5)
#cv2.imshow('Median Filtered Image',medianFiltered)
#cv2.waitKey(0)



_, contours, hierarchy = cv2.findContours(saturation, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contour_list = []
idx =0
# for each contour found, draw a rectangle around it on original image
for contour in contours:

    idx += 1
    area = cv2.contourArea(contour)
    if area > 100:
        contour_list.append(contour)

        # get rectangle bounding contour
        [x,y,w,h] = cv2.boundingRect(contour)


        # draw rectangle around contour on original image
        #cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,255),2)

        roi = rawImage[y:y + h, x:x + w]

        #cv2.imwrite(''+ str(idx) + '.png', roi)

        #cv2.imshow('img',roi)
        #cv2.waitKey(0)


cv2.drawContours(rawImage, contour_list,  -1, (255,0,0), 2)
#cv2.imshow('tito',tito)
#cv2.waitKey(0)


cv2.imwrite("tracing2.png", rawImage)

result = pytesseract.image_to_string(Image.open("tracing2.png"))
print (result)

cv2.imshow('Objects Detected',rawImage)
cv2.waitKey(0)
