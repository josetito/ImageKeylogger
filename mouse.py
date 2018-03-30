from pynput import mouse

'''
Script que captura todos los movimientos del mouse. La hice para intentar cambiar
la forma en como se hace actualmente en la herramienta Research Logger
'''


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
    if dy < 0:
        print('Scrolled {0} at {1} down'.format((x,y)))
    else:
        print('Scrolled {0} at {1} up'.format((x,y)))


# Collect events until released
with mouse.Listener(
        on_click=on_click,
        on_move=on_move,
        on_scroll=on_scroll) as listener:
    listener.join()