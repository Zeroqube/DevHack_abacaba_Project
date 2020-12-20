import codecs
import random
from PIL import Image


def readpix(x, y):
    R, G, B = pixels[x, y]
    ch = ((R & 0x07) << 5) + ((G & 0x03) << 3) + (B & 0x07)
    return ch


def revert(numstr):
    string = codecs.decode(bytes(numstr), 'windows-1251')
    return string


def picture_to_string(key, y):
    global pixels
    numstr = []
    random.seed(key)
    visited = set()
    while True:
        p = random.randint(0, x * y)
        if p in visited:
            continue
        visited.add(p)
        ch = readpix(p // y, p % y)
        if ch == 0x03:
            break
        numstr.append(ch)
    return numstr


name = input('введите путь к изображению')
im = Image.open(name)
pixels = im.load()
x, y = im.size
key = input('введите ключ')
text = picture_to_string(key, y)
res = revert(text)
print(res)