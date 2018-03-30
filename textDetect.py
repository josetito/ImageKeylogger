import cv2
import numpy as np
import pytesseract
from PIL import Image
import sys
import os

#detecta objetos y letras
def detectObj(img_path):

    img = cv2.imread(img_path)
    mser = cv2.MSER_create()

    img = cv2.resize(img, (img.shape[1]*2, img.shape[0]*2))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    vis = img.copy()

    regions = mser.detectRegions(gray)
    hulls = [cv2.convexHull(p.reshape(-1, 1, 2)) for p in regions[0]]
    cv2.polylines(vis, hulls, 1, (0,255,0))

    cv2.imshow('img', vis)
    cv2.waitKey()


# Pasa la imagen a escala de grises
#Aplica dilate y erode
#intenta extraer texto de la imagen
def get_string(img_path,src_path):
    # Read image with opencv
    img = cv2.imread(img_path)

    # Convert to gray
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("img", img)
    cv2.waitKey(0)

    # Apply dilation and erosion to remove some noise
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)
    cv2.imshow("img2", img)
    cv2.waitKey(0)

    # Write image after removed noise
    cv2.imwrite(src_path + "removed_noise.png", img)

    #  Apply threshold to get image with only black and white
    img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

    # Write the image after apply opencv to do some ...
    cv2.imwrite(img_path, img)

    # Recognize text with tesseract for python
    result = pytesseract.image_to_string(Image.open(img_path))

    # Remove template file
    #os.remove(temp)

    print  result

#utiliza el contorno pero discrimina a lo que realmente se quiere.
def contorno(img_path):
    image = cv2.imread(img_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # grayscale
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)  # threshold
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
    dilated = cv2.dilate(thresh, kernel, iterations=13)  # dilate
    _, contours, hierarchy = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)  # get contours

    # for each contour found, draw a rectangle around it on original image
    for contour in contours:
        # get rectangle bounding contour
        [x, y, w, h] = cv2.boundingRect(contour)

        # discard areas that are too large
        if h > 100 and w > 100:
            continue

        # discard areas that are too small
        if h < 50 or w < 50:
            continue

        # draw rectangle around contour on original image
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 255), 2)

    # write original image with added contours to disk
    cv2.imwrite("contoured.jpg", image)

# La idea era encontrar la parte que contenia texto dentro de la imagen pero
# no funciona la area que reconoce es lo que no tiene texto
def textArea(img_path):
    # Load the image
    img = cv2.imread(img_path)

    # convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # smooth the image to avoid noises
    gray = cv2.medianBlur(gray, 5)

    # Apply adaptive threshold
    thresh = cv2.adaptiveThreshold(gray, 255, 1, 1, 11, 2)
    thresh_color = cv2.cvtColor(thresh, cv2.COLOR_GRAY2BGR)

    # apply some dilation and erosion to join the gaps - change iteration to detect more or less area's
    thresh = cv2.dilate(thresh, None, iterations=15)
    thresh = cv2.erode(thresh, None, iterations=15)

    # Find the contours
    image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # For each contour, find the bounding rectangle and draw it
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.rectangle(thresh_color, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Finally show the image
    #cv2.imshow('img', img)
    cv2.imshow('res', np.hstack([img, thresh_color]))
    cv2.waitKey(0)
    cv2.destroyAllWindows()



#----------------------------------------------------------------------------------
#sin sentido

#dibuja un rectangulo dentro de la imagen
def dibujar(img_path):
    img = cv2.imread(img_path)
    width, height,chanels = img.shape
    x = 10
    y = 10

    x1 = x - (width / 4)
    x2 = x + (width / 4)

    y1 = y - (height / 4)
    y2 = y + (height / 4)

    img2 = cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 2)

    cv2.imshow("h",img)
    cv2.imshow('hola', np.hstack([img,img2]))
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Esta prueba la hice para saber que hacia la funcion Canny
# Lo que hace es a todas las lineas y letras las cambia como si fuera un retato
def canny(img_path):
    img = cv2.imread(img_path)
    edges = cv2.Canny(img, 100, 200)
    cv2.imshow('hola', edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def dd(img,x,y,ancho,alto):
    roi = img[y:y + alto, x:x + ancho]
    cv2.imshow("peq", roi)
    cv2.waitKey(0)
    finalimg = Image.fromarray(roi)


img_path ='/home/tito/Documents/ImageKeylogger/imagenes/menu.png'
src_path = '/home/tito/Documents/ImageKeylogger/imagenes/'

detectObj(img_path)
#get_string(img_path,src_path)
#contorno(img_path)
#textArea(img_path)
#dibujar(img_path)
#canny(img_path)