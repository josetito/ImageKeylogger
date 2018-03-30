import cv2
from PIL import Image
import numpy as np
import pytesseract

#Uno selecciona con el mouse la parte que desea seleccionar
def selectArea():
    # Read image
    im = cv2.imread("./imagenes/crop2.png")

    # Select ROI
    r = cv2.selectROI(im)
    #showCrosshair = False
    #fromCenter = False
    #r = cv2.selectROI("Image", im, fromCenter, showCrosshair)


    print int(r[1]),int(r[1] + r[3])
    print int(r[0]),int(r[0] + r[2])

    # Crop image
    imCrop = im[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])]

    # Display cropped image
    cv2.imshow("Image", r)
    cv2.waitKey(0)

#recorte en forma de rectangulo
def rectangulo():
    im =cv2.imread("./imagenes/menu.png")

    cv2.rectangle(im, (100, 100), (200, 200), (255, 0, 0), 2)

    #crop_rectangle = (150, 200, 200, 200)
    #cropped_im = im.crop(crop_rectangle)

    #cropped_im.show()
    cv2.imshow("t",im)
    cv2.waitKey(0)

#realiza un corte con las medidas de las imagenes y luego trata de identificar
#el texto dentro de esa area
def cut():
    im = cv2.imread("./imagenes/menu.png")
    width, height,_ = im.shape  # Get dimensions

    print width,height
    new_width=200
    new_height= 200

    x1 = (width)
    y1 = (height/4)
    x2 = (width)
    y2 = (height/4)
    w = x2 - x1
    h = y2 - y1

    print x1,x2,y1,y2
    print w,h

    #cv2.rectangle(im, (258, 177), (558, 197), (255, 0, 0), 2)
    #[y1:y2, x1:x2
    roi = im[177:197, 258:558]
    #roi = im[y1:y2, x1:x2]

    cv2.imshow("i",im)
    cv2.imshow("roi",roi)
    cv2.waitKey(0)

    cv2.imwrite("./imagenes/roi.png", roi)

    # Recognize text with tesseract for python
    result = pytesseract.image_to_string(Image.open("./imagenes/roi.png"))

    print result

# Lo que hace es un recorte de una parte de la imagen y la remplaza en otro lado de
#la imagen
def cut2():
    #img = cv2.imread("./imagenes/menu.png")

    # simple image editor which will load, modify and save image.

    ori_filename = './imagenes/menu.png'

    new_filename = './imagenes/jordan-airball.png'

    print("Reading and displaying file: ", ori_filename)

    ori_img = cv2.imread(ori_filename)

    cv2.imshow(ori_filename, ori_img)

    print("Modifying file")

    new_img = ori_img

    replacement = new_img[180:230, 230:280]

    ball = new_img[183:223, 525:565]

    new_img[263:303, 475:515] = ball

    #new_img[:53, 50:75] = replacement

    print("Displaying modified file: ", new_filename)

    cv2.imwrite(new_filename, new_img)

    cv2.imshow(new_filename, new_img)

    cv2.waitKey(0)

    cv2.destroyAllWindows()
cut2()

