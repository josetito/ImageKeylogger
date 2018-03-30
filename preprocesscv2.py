import argparse
import imutils
import cv2
import gtk


def get_screen_size():
    width = gtk.gdk.screen_width()
    height = gtk.gdk.screen_height()
    return [width,height]

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="path to the input image")
args = vars(ap.parse_args())

# load the image and resize it to a smaller factor so that
# the shapes can be approximated better
image = cv2.imread(args["image"])
screensize = get_screen_size()
x = screensize[0]
y = screensize[1]

crop_img = image[y:y+50, x:x+50]
cv2.imshow("cropped", crop_img)
cv2.waitKey(0)

'''
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (7, 7), 3)

t, dst = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_TRIANGLE)

_, contours, _ = cv2.findContours(dst, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for c in contours:
    area = cv2.contourArea(c)
    if area > 1000 and area < 10000:
        cv2.drawContours(src, [c], 0, (0, 255, 0), 2, cv2.LINE_AA)

cv2.imshow('contornos', src)
cv2.imshow('umbral', dst)

cv2.waitKey(0)


'''
