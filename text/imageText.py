#import textract
import pytesseract
import pyocr
import pyocr.builders
from PIL import Image
import PIL

image = "lao.jpg"

tools = pyocr.get_available_tools()[0]
text = tools.image_to_string(Image.open(image),
                             builder=pyocr.builders.TextBuilder())

print (text)
print (".........................")
text1 = pytesseract.image_to_string(Image.open(image))
print (text1)



pyocr.libtesseract.image_to_pdf(
    PIL.Image.open(image),
    "output_filename"  # .pdf will be appended
)
#text = textract.process('image.png', encoding='ascii', method='tesseract')