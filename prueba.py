
#key = cv2.waitKey(20)
#print(key)

# cat log.txt | cut -f8 -d"|" | cut -f 1-2,5-6 -d"," | tr ' ' ',' > coordenates.log


'''

import subprocess
bashCommand = "cat /home/tito/Documents/ResearchLogger/logs-tito-1517412618/click_images/clickimagelogfile_tito.txt | cut -f8 -d'|' | cut -f 1-2,5-6 -d',' | tr ' ' ',' > coordenates.log"


#output = subprocess.check_output(['bash','-c', bashCommand])
p1 = subprocess.Popen(['bash','-c', bashCommand])
p1.wait()
print "ya"


   
img = cv2.imread('./imagenes/office.png')


x=150
y=200
cv2.circle(img,(x,y),10,(255,0,0),-1)

while(True):
    cv2.imshow('image',img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()


from pynput import mouse

def on_move(x, y):
    print('Pointer moved to {0}'.format(
        (x, y)))

def on_click(x, y, button, pressed):
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    #if not pressed:
        # Stop listener
    #    return False

def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format(
        'down' if dy < 0 else 'up',
        (x, y)))

# Collect events until released
with mouse.Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll) as listener:
    listener.join()


from PIL import Image

# size is width/height
img = Image.open('./imagenes/office.png')
left = 2407
top = 804
width = 300
height = 200
box = (left, top, left+width, top+height)
area = img.crop(box)

area.save('cropped_0_388_image1', 'jpeg')



def crop_image(input_image, output_image, start_x, start_y, width, height):
    """Pass input name image, output name image, x coordinate to start croping, y coordinate to start croping, width to crop, height to crop """
    box = (start_x, start_y, start_x + width, start_y + height)
    output_img = img.crop(box)
    output_img.save(output_image +".png")


crop_image(img,"output", 0, 0, 1280, 399)

import pyscreenshot as ImageGrab
# fullscreen
im=ImageGrab.grab()
im.show()

# part of the screen
im=ImageGrab.grab(bbox=(10,10,500,500))
im.show()
im.save('cropped_image1', 'jpeg')

# to file
#ImageGrab.grab_to_file('im.png')
'''


import os
import psutil
from Xlib import display

from psutil import Process
p = Process(os.getpid())
print "Proceso: ", p.name()
print "ID: ", p.pid
print "Llamado por el usuario: ", p.username()
print "ruta", p.cwd()
print p.cmdline()
print p.open_files()


from pynput import keyboard

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()


