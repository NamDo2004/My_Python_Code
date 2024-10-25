import pytesseract as pt
import PIL
from PIL import Image

pt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
file = 'D:\Python_File\Text_Regconition\IMG\img.png'
image = Image.open(file)

text = pt.image_to_string(image)
print(text)