'''DocString'''
from itertools import permutations
import enchant
d = enchant.Dict("en_us")

while(True):
    print("\n")
    op = set()
    inp = input("Enter characters: ")
    for n in range(3,len(inp)+1):
        for y in list(permutations(inp,n)):
            z = "".join(y)
            if d.check(z):
                op.add(z)
    print(op)


'''
from os import closerange
from PIL import Image
import pytesseract as tess
tess.pytesseract.tessetact_cmd = r'C:\Users\HP\AppData\Local\Programs\Tesseract-OCR'
​
image = r'D:\\'
left = 195
right= 880
top = 1460
bottom = 2145
im = im.crop((left, top, right, bottom))
text = tess. image_to_string(Image.open(image), lang="eng")
print(text)
'''