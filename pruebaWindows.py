from pynput import mouse
from PIL import Image
from pynput.mouse import Button
import pyscreenshot as ImageGrab

def on_move(x, y):
    print('Pointer moved to {0}'.format(
        (x, y)))

def on_click(x, y, button, pressed):
    button = str(button)
    if pressed:
        if button == 'Button.left':
            print('Mousebutton_left {0} at {1} Pressed'.format(x,y))
        if button == 'Button.right':
            print('Mousebutton_right {0} at {1} Pressed'.format(x,y))
        if button == 'Button.middle':
            print('Mousebutton_middle {0} at {1} Pressed'.format(x,y))
    else:
        if button == 'Button.left':
            print('Mousebutton_left {0} at {1} Release'.format(x,y))
        if button == 'Button.right':
            print('Mousebutton_right {0} at {1} Release'.format(x,y))
        if button == 'Button.middle':
            print('Mousebutton_middle {0} at {1} Release'.  format(x,y))

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

'''

print "Primer imagen.............."
# size is width/height
img = Image.open('./imagenes/office.png')
left = 2407
top = 804
width = 300
height = 200
box = (left, top, left+width, top+height)
area = img.crop(box)

area.save('cropped_0_388_image1', 'jpeg')

print "Hice la primera imagen"



def crop_image(input_image, output_image, start_x, start_y, width, height):
    """Pass input name image, output name image, x coordinate to start croping, y coordinate to start croping, width to crop, height to crop """
    box = (start_x, start_y, start_x + width, start_y + height)
    output_img = img.crop(box)
    output_img.save(output_image +".png")

print "segunda imagen"
crop_image(img,"output", 0, 0, 1280, 399)
print "termine segunda imagen"



print "tercera imagen"
# fullscreen
im=ImageGrab.grab()
im.show()

# part of the screen
im=ImageGrab.grab(bbox=(10,10,500,500))
im.show()
im.save('cropped_image1', 'jpeg')
print "fin tercera imagen"

# to file
#ImageGrab.grab_to_file('im.png')

print "mouse monitoring............................"
# Collect events until released
with mouse.Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll) as listener:
    listener.join()
'''