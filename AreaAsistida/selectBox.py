import cv2
import numpy as np
import subprocess
import gtk
import pytesseract
from PIL import Image
import os
import argparse

'''
example: python selectBox.py -l /home/ResearchLogger/logs-tito-1520000553/click_images/clickimagelogfile_tito.txt

'''

nameLog = "coordinates.log"

# get screen size
def get_screen_size():
    width = gtk.gdk.screen_width()
    height = gtk.gdk.screen_height()
    return [width,height]

# execute bash command and generate the nameLog
def executeCommand(file):
    bashCommand = "cat "+file+" | cut -f8 -d'|' | cut -f 1-2,4-6,8-9 -d',' | tr ' ' ',' > " + nameLog + ""
    p1 = subprocess.Popen(['bash','-c', bashCommand])
    p1.wait()

# find the x, y coordinates inside the image and draw a circle
def findCoordinates(image_down,image_up,ImageDirectory):
    screensize = get_screen_size()
    img = cv2.imread("" + ImageDirectory + "" + image_down + "")
    img2 = cv2.imread("" + ImageDirectory + "" + image_up + "")

    x = screensize[0] / 4
    y = screensize[1] / 4

    image = cv2.circle(img, (x, y), 10, (255, 0, 0), -1)
    #cv2.imwrite("" + image_down + "", image)

    image2 = cv2.circle(img2, (x, y), 10, (255, 0, 0), -1)
    #cv2.imwrite("2" + image_down + "", image2)

    imstack = np.hstack((image, image2))
    cv2.imshow("Clicks", imstack)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# crop the image according to the selection box
def cutImage(img,ImageDirectory):
    # Select ROI
    img = cv2.imread("" + ImageDirectory + "" + img + "")
    r = cv2.selectROI(img)

    # Crop image
    imCrop = img[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])]

    cv2.imwrite("seleccion.png", imCrop)

# recognize the text in the image with pytesseract
def recognizeText():
    # Recognize text with tesseract for python
    result = pytesseract.image_to_string(Image.open("seleccion.png"))

    print "Realizo click en --> " + result

# process input
def processInput():
    ap = argparse.ArgumentParser()
    ap.add_argument("-l", "--log", required=True,
                    help="log file to process")
    args = vars(ap.parse_args())

    file = (args["log"])
    if os.path.exists(file):
        pass
    else:
        print "Log file not exists."

    ImageDirectory = os.path.dirname(file) + "/"
    return [ImageDirectory,file]


def main(nameLog):
    ImageDirectory, file = processInput()
    executeCommand(file)
    file = open(nameLog, "r")
    for line in file.readlines():
        Xdown, Ydown, click_down, image_down, Xup, Yup, click_up, image_up, enter = line.split(",")
        findCoordinates(image_down,image_up,ImageDirectory)
        cutImage(image_down,ImageDirectory)
        recognizeText()

main(nameLog)