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
    global pixels
    random.seed(key)
    for c in text:
        p = random.randint(0, x * y)
        change(p // y, p % y, c)


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
    global pixels
    random.seed(key)
    for c in text:
        p = random.randint(0, x * y)
        change(p // y, p % y, c)


im2 = Image.new('RGB', (500, 500), (0, 0, 0))
im2.save('f.JPG')
name = input('введите путь к изображению')
im = Image.open(name)
pixels = im.load()
x, y = im.size
text = input('введите текст')
n_text = convert(text)
key = input('введите ключ')
print(pixels[312, 97])
string_to_picture(key, n_text, x, y)
name = input('введите путь к изображению')
im.save(name)


