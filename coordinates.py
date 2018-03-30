import cv2
import numpy as np
import subprocess
import gtk
'''
Lo que hace es parsear el log del sistema para sacar x,y 
'''

nameLog = "coordinates.log"
ImageDirectory = "/home/tito/Documents/pruebas/ResearchLogger/logs-tito-1520000553/click_images/"

bashCommand = "cat /home/tito/Documents/ResearchLogger/logs-tito-1517412618/click_images/clickimagelogfile_tito.txt | cut -f8 -d'|' | cut -f 1-2,4-6,8-9 -d',' | tr ' ' ',' > " +nameLog+ ""
#mejorada
# cat /home/tito/Documents/ResearchLogger/logs-tito-1517412618/click_images/clickimagelogfile_tito.txt | cut -f8 -d'|' | cut -f 1-2,4-6,8-9 -d',' | tr ' ' ','
# vieja cat /home/tito/Documents/pruebas/ResearchLogger/logs-tito-1520000553/click_images/clickimagelogfile_tito.txt | cut -f8 -d'|' | cut -f 1-2,5-6 -d',' | tr ' ' ','

def get_screen_size():
    width = gtk.gdk.screen_width()
    height = gtk.gdk.screen_height()
    return [width,height]

def executeCommand(bashCommand):
    p1 = subprocess.Popen(['bash','-c', bashCommand])
    p1.wait()

def readFile(nameLog):
    screensize = get_screen_size()
    archivo = open(nameLog, "r")
    for linea in archivo.readlines():
        Xdown, Ydown, click_down, image_down, Xup, Yup, click_up, image_up = linea.split(",")
        print Xdown, Ydown
        print image_down
        print Xup, Yup
        #print ""+ImageDirectory+""+imageName+""
        img = cv2.imread(""+ImageDirectory+""+image_down+"")
        image = cv2.circle(img,(int(screensize[0]/4),int((screensize[1]/4))),10,(255,0,0),-1)
        cv2.imwrite(""+image_down+"",image)

        image2 = cv2.circle(img,(int(Xup),int(Yup)),10,(255,0,0),-1)
        cv2.imwrite("2"+image_down+"",image)

        x= screensize[0]/4
        y= screensize[1]/4

        center = (int(x),int(y))
        radius = int(20)
        cv2.circle(image,center,radius,(0,255,0),2)
        cv2.imshow("j",image)
        cv2.waitKey(0)

        cv2.rectangle(img, (x, y), (x + 100, y + 20), (0, 255, 0), 2)
        cv2.imshow("r",image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
	    #if int(Xdown) != int(Xup):
    	#	print "Se sospecha que se subraya algo"
	    #else:
	    #	"Click normal"
	    #while(1):
    #		cv2.imshow('image',img)
    #		if cv2.waitKey(20) & 0xFF == 27:
    #			break



