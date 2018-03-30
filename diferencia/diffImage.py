import cv2
import pytesseract
import numpy as np
from PIL import Image
import pyocr.builders

def diffImage(image1, image2):
    # load two images
    diff1 = cv2.imread(image1)
    diff2 = cv2.imread(image2)

    # calculate the absolute difference of the two images
    diff_total = cv2.absdiff(diff1, diff2)

    # Search the countours
    imagen_gris = cv2.cvtColor(diff_total, cv2.COLOR_BGR2GRAY)
    _, contours, hierarchy = cv2.findContours(imagen_gris, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    #create a mask
    mask = np.full((diff1.shape[0], diff1.shape[1]), 0, dtype=np.uint8)  # mask is only
    #mask.fill(255,)

    # look akmeach one of the contours and, if it is not noise, we draw its Bounding Box on the original image
    for c in contours:
        if cv2.contourArea(c) >= 200:
            posicion_x, posicion_y, ancho, alto = cv2.boundingRect(c)  # save the dimensions of the Bounding Box
            cv2.rectangle(mask, (posicion_x, posicion_y), (posicion_x + ancho, posicion_y + alto), (255,255,255),-1)  # Draw the bounding box

    # get first masked value (foreground)
    img = cv2.bitwise_and(diff1, diff1, mask=mask)


    #cv2.imshow("diff", img)
    #cv2.waitKey(0)

    img = Image.fromarray(img)
    img.save("diff.png")

    return img

def allPixelWhite(img):
    pixels = img.load()
    for y in xrange(img.size[1]):
        for x in xrange(img.size[0]):
            if pixels[x,y] == (0,0,0):
                pixels[x,y] = (255,255,255)

    #cv2.imshow("white", img)
    #cv2.waitKey(0)
    img.save("blanca.png")
    return img


def processImage(img):
    #read
    img = cv2.imread('blanca.png')

    # convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #cv2.imshow("gray", gray)
    #cv2.waitKey(0)


    # Apply adaptive threshold
    thresh = cv2.adaptiveThreshold(gray, 255, 1, 1, 11, 2)
    #cv2.imshow("thresh", thresh)
    #cv2.waitKey(0)
    ret1, thresh1 = cv2.threshold(thresh, 180, 255, cv2.THRESH_BINARY)
    #cv2.imshow("th1", thresh1)
    #cv2.waitKey(0)
    thresh_color = cv2.cvtColor(thresh1, cv2.COLOR_GRAY2BGR)

    #cv2.imshow("thresh color", thresh_color)
    #cv2.waitKey(0)

    #vcr = cv2.subtract(255, thresh)
    # change reverse color
    finishImg = cv2.bitwise_not(thresh)
    #cv2.imshow("viceversa", finishImg)
    #cv2.waitKey(0)

    finishImg = Image.fromarray(finishImg)

    finishImg.save("blanca1.png")
    return finishImg

def textImage(img):
    result = pytesseract.image_to_string(img, lang ="eng")
    print (result)


imagen1 = "texto1.png"
imagen2 = "texto2.png"

diffImage = diffImage(imagen1,imagen2)
white = allPixelWhite(diffImage)
textImage(white)

print ("...............")

ImageProc = processImage(white)
#textImage(ImageProc)

print (".................")
print ("los otros")

text1 = pytesseract.image_to_string(Image.open("diff.png"), lang="eng+spa")
print (text1)

print (".................")

text2 = pytesseract.image_to_string(Image.open("text.png"), lang="eng+spa")
print (text2)

print ("--------------")

tools = pyocr.get_available_tools()[0]
text = tools.image_to_string(Image.open(ImageProc),
                             builder=pyocr.builders.TextBuilder())
