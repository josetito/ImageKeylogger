import gtk
from pynput import mouse

width = gtk.gdk.screen_width()
height = gtk.gdk.screen_height()
print "Resolucion"
print str(width) +"x"+ str(height)


class Point:
    def __init__(self, x=0, y=0):
        # Collect events until released
        self.x = x
        self.y = y
        print "soy el x y el y: ",x,y
        

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
                print('Mousebutton_middle {0} at {1} Release'.format(x,y))

        return (x,y)

    def on_scroll(self, x, y, dx, dy):
        if dy < 0:
            print('Scrolled {0} at {1} down'.format(x,y))
        else:
            print('Scrolled {0} at {1} up'.format(x, y))
        return (x,y)

    def on_move(self, x, y):
        print('Pointer moved to {0}'.format((x, y)))
        return(x,y)


x = Point(2,4)

#with mouse.Listener(on_move=self.on_move,on_click=self.on_click, on_scroll=self.on_scroll) as listener:
 #           listener.join()

'''
            try:
                listener.join()
            except MyException as e:
                print('{0} was clicked'.format(e.args[0]))
            
'''