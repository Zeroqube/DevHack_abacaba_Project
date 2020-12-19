from PIL import Image
from Methods import *

name = input('введите путь к изображению')
res = []
im = Image.open(name)
pixels = im.load()
x, y = im.size
text = input('введите текст')
n_text = convert(text)
key = input('введите ключ')
string_to_picture(key, n_text, x, y)
name = input('введите путь к изображению')
im.save(name)


