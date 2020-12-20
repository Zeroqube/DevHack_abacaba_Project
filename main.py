from PIL import Image
import random


def change(ch, x, y):
    global pixels
    R, G, B = pixels[x, y]
    R = (R & 0xf8) + (ch // 32)
    G = (G & 0xfc) + ((ch % 32) // 8)
    B = (B & 0xf8) + (ch % 8)
    pixels[x, y] = (R, G, B)


def convert(string):
    numstr = []
    string = string.encode('windows-1251')
    for i in string:
        numstr.append(i)
    return numstr


def string_to_picture(key, text, y):
    global pixels
    visited = set()
    random.seed(key)
    text.append(0x03)  # Признак конца текста
    i = 0
    p = 300
    while True:
        # p = random.randint(0, x * y)
        p += 400
        if p in visited:
            continue
        visited.add(p)
        change(text[i], p % y, p // y)
        i += 1
        if text[i - 1] == 0x03:
            break


im2 = Image.new('RGB', (500, 500), (0, 0, 0))
im2.save('f.bmp')
name = input('введите путь к изображению')
im = Image.open(name)
pixels = im.load()
x, y = im.size
text = input('введите текст') + ''
n_text = convert(text)
key = input('введите ключ')
string_to_picture(key, n_text, y)
name = input('введите путь к изображению')
im.save(name)
