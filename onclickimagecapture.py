import gtk
from pynput import mouse

width = gtk.gdk.screen_width()
height = gtk.gdk.screen_height()
print "Resolucion"
print str(width) +"x"+ str(height)


class Point:
    def __init__(self,*args, **kwargs):
        # Collect events until released
        print "entre aca"
        with mouse.Listener(on_move=self.on_move,on_click=self.on_click, on_scroll=self.on_scroll) as listener:
            listener.join()

    def on_click(self,x, y, button, pressed):
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

    def on_scroll(self, x, y, dx, dy):
        print('Scrolled {0} at {1}'.format(
            'down' if dy < 0 else 'up',
            (x, y)))
    def on_move(self, x, y):
        print('Pointer moved to {0}'.format((x, y)))


x = Point()
