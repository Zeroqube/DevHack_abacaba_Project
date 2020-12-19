from PIL import Image
import random


def change(ch, x, y):
    global pixels
    R, G, B = pixels[x, y]
    R = R // 8 * 8 + ch // 32
    G = G // 4 * 4 + ch % 32 // 8
    B = B // 8 * 8 + ch % 8
    pixels[x, y] = (R, G, B)


def convert(string):
    numstr = []
    string = string.encode('windows-1251')
    for i in string:
        numstr.append(i)
    return numstr


def string_to_picture(key, text, x, y):
    visited = {}
    global pixels
    random.seed(key)
    for c in text:
        p = random.randint(0, x * y)
        while p in visited:
            p = random.randint(0, x * y)
        change(c, p // y, p % y)


name = input('введите путь к изображению')
im = Image.open(name)
pixels = im.load()
x, y = im.size
n = (x * y + 255) // 256
text = input('введите текст')
n_text = convert(text) + [0]
key = input('введите ключ')
string_to_picture(key, n_text, x, y)
name = input('введите путь к изображению')
im.save(name)


