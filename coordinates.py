import cv2
import numpy as np

img = cv2.imread('./imagenes/tito.png')
#print img

x=150
y=200
cv2.circle(img,(x,y),10,(255,0,0),-1)

while(True):
    cv2.imshow('image',img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()