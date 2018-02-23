import cv2
import numpy as np
import subprocess

#Xup, Xdown = 0
#Yup, Ydown = 0

nameLog = "coordinates.log"
ImageDirectory = "/home/tito/Documents/pruebas/ResearchLogger/logs-tito-1518708115/click_images/"

bashCommand = "cat /home/tito/Documents/pruebas/ResearchLogger/logs-tito-1518708115/click_images/clickimagelogfile_tito.txt | cut -f8 -d'|' | cut -f 1-2,5-6 -d',' | tr ' ' ',' > " +nameLog+ ""
#mejorada
# cat /home/tito/Documents/ResearchLogger/logs-tito-1517412618/click_images/clickimagelogfile_tito.txt | cut -f8 -d'|' | cut -f 1-2,4-6,8-9 -d',' | tr ' ' ','



p1 = subprocess.Popen(['bash','-c', bashCommand])
p1.wait()

archivo = open(nameLog, "r")
for linea in archivo.readlines():
	Xdown, Ydown, imageName, Xup, Yup = linea.split(",")
	print Xdown, Ydown
	print imageName
	print Xup, Yup
    #print ""+ImageDirectory+""+imageName+""
	img = cv2.imread(""+ImageDirectory+""+imageName+"")
	image = cv2.circle(img,(int(Xdown),int(Ydown)),10,(255,0,0),-1)
	cv2.imwrite(""+imageName+"",image)

	image2 = cv2.circle(img,(int(Xup),int(Yup)),10,(255,0,0),-1)
	cv2.imwrite("2"+imageName+"",image)

	if int(Xdown) != int(Xup):
		print "Se sospecha que se subraya algo"
	else:
		"Click normal"
	#while(1):
#		cv2.imshow('image',img)
#		if cv2.waitKey(20) & 0xFF == 27:
#			break
