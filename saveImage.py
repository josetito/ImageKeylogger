import pyautogui
import numpy as np
import cv2
from pynput import mouse
from pynput.mouse import Button, Controller
import gtk
import copy
import pyscreenshot as ImageGrab

'''
Script

Este script lo que hace es simular el proceso que ocurre en la herramienta Research 
logger.

Este script logra capturar un scrennshot cada vez que se da click en la pantalla
y deja el punto de ese click en el centro de la imagen . 


'''


def get_screen_size():
    width = gtk.gdk.screen_width()
    height = gtk.gdk.screen_height()
    return [width,height]


#Screen total
def screentotal(x,y):
    shot = pyautogui.screenshot()
    shot.save("shot.png")
    img = cv2.imread("shot.png")
    img = cv2.circle(img,(int(x),int(y)),20,(0,255,0),-1)
    cv2.imshow("shot",img)
    cv2.waitKey(0)


def screen1(x,y):
    k = screensize[0]/2
    l = screensize[1]/2
    image_data = pyautogui.screenshot(region=(( x-(screensize[0]/4), y-(screensize[1]/4),k,l)))
    image_data.save("crop.png")
    img2 = cv2.imread("crop.png")
    img2 = cv2.circle(img2,(int(x),int(y)),20,(255,0,0),-1)
    cv2.imshow("crop",img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def screen2(x,y):
    x1 = x-(screensize[0]/4)
    x2 = x+(screensize[0]/4)

    y1 = y-(screensize[1]/4)
    y2 = y+(screensize[1]/4)

    print "x1",x1
    #print x2
    print "y1",y1
    #print y2

    w = x2 - x1
    h = y2 - y1
    print "size",w,h
    # PIL format as RGB
    crop = pyautogui.screenshot(region=(x1,y1,w,h))
    crop.save("crop2.png")
    crop2 = cv2.imread("crop2.png")
    crop2 = cv2.circle(crop2,(int((screensize[0]/4)),int((screensize[1]/4))),5,(255,0,0),-1)
    cv2.imshow("crop2",crop2)
    cv2.imwrite("crop2_point.png",crop2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def dibujar(x,y):
    img = cv2.imread("crop2_point.png")
    width, height,chanels = img.shape

    x1 = x-(screensize[0]/4)
    x2 = x+(screensize[0]/4)

    y1 = y-(screensize[1]/4)
    y2 = y+(screensize[1]/4)

    w = x2 - x1
    h = y2 - y1

    x3 = x - (x1/2)
    x4 = x + (x1/2)

    y3 = y - (y1/2)
    y4 = y + (y1/2)

    w1 = x3 - x4
    h1 = y3 - y4

    print x3,y3
    print w1,h1
    print "llegue"
    img2 = cv2.rectangle(img,(x3 ,y3 ), (w1, h1), (255, 0, 0), 2)
    print "2"
    cv2.imshow("rec",img2)
    print "3"
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def on_click(x, y, button, pressed):
    button = str(button)
    if pressed:
        if button == 'Button.left':
            screen2(x,y)
            dibujar(x,y)
        if button == 'Button.right':
            screen2(x,y)
            dibujar(x,y)
        if button == 'Button.middle':
            screentotal(x,y)
            print "total"

screensize = get_screen_size()
imagedimensions = [500,500]
print "dim",imagedimensions[0]
print screensize[0], screensize[1]
with mouse.Listener(
        on_click=on_click) as listener:
    listener.join()