import cv2
import numpy as np
import subprocess
import gtk
import pytesseract
from PIL import Image
import os
import argparse

nameLog = "coordinates.log"

# get screen size
def get_screen_size():
    width = gtk.gdk.screen_width()
    height = gtk.gdk.screen_height()
    return [width,height]

# execute bash command and generate the nameLog
def executeCommand(file):
    bashCommand = "cat "+file+" | cut -f8 -d'|' | tr ' ' '\n' | sed '/^$/d' | paste -s -d'\t\n' > " + nameLog + ""
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

def diff(img1, img2):
    print "diff"

def


def main(nameLog):
    ImageDirectory, file = processInput()
    executeCommand(file)
    file = open(nameLog, "r")
    for line in file.readlines():
        info = line.split("\t")
        if len(info)==2:
            infoImage1 = info[0]
            infoImage2 = info[1].rstrip("\n")
            Xdown, Ydown, miliseg_down, click_down, image_down = infoImage1.split(",")
            Xup, Yup, miliseg_up, click_up, image_up = infoImage2.split(",")

            if (Xdown != Xup or Ydown != Yup):
                print "se sospecha que subrayo"

            findCoordinates(image_down,image_up,ImageDirectory)
            cutImage(image_down,ImageDirectory)
            recognizeText()
        else:
            print "tiene una mas"

main(nameLog)