from PIL import Image
import random


def change(ch, x, y):
    global pixels
    R, G, B = pixels[x, y]
    R = R // 8 + ch // 32
    G = G // 7 + ch % 32 // 8
    B = B // 8 + ch % 8
    pixels[x, y] = (R, G, B)


def convert(string):
    numstr = []
    string = string.encode('windows-1251')
    for i in string:
        numstr.append(i)
    return numstr


def string_to_picture(key, text, x, y):
    global pixels, res
    random.seed(key)
    for c in text:
        p = random.randint(0, x * y)
        change(p // y, p % y, c)