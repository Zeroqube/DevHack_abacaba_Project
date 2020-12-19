from PIL import Image
import random


def revert(numstr):

    return numstr


def picture_to_string(key, x, y):
    global pixels
    visited = {}
    numstr = []
    random.seed(key)
    while len(numstr) < 1 or numstr[-1] != 0:
        p = random.randint(0, x * y)
        while p in visited:
            p = random.randint(0, x * y)
        R, G, B = pixels[p // y, p % y]
        numstr.append(R % 8 * 32 + G % 4 * 8 + B % 8)
    return revert(numstr)


name = input('введите путь к изображению')
im = Image.open(name)
pixels = im.load()
x, y = im.size
key = input('введите ключ')
text = picture_to_string(key, x, y)
print(text)

