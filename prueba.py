
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
'''

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