from PIL import Image
import requests
import numpy as np
from StringIO import StringIO


import urllib, cStringIO

file = cStringIO.StringIO(urllib.urlopen("https://www.facebook.com/").read())
img = Image.open(file)
img.save("url.png")

#response = requests.get("https://www.facebook.com/")
#img = np.array(Image.open(StringIO(response.content)))
#t  = Image.fromarray(img)
#t.save("url.png")