from PIL import Image
import random
import sys


def change(ch, x, y):
    global pixels
    pos = random.randint(0, 2)
    nch = ch
    R, G, B = pixels[x, y]
    if pos == 0:
        G = (G & 0xf8) + (nch // 32)
        R = (R & 0xfc) + ((nch % 32) // 8)
        B = (B & 0xf8) + (nch % 8)
    elif pos == 1:
        R = (R & 0xf8) + (nch // 32)
        G = (G & 0xfc) + ((nch % 32) // 8)
        B = (B & 0xf8) + (nch % 8)
    elif pos == 2:
        R = (R & 0xf8) + (nch // 32)
        B = (B & 0xfc) + ((nch % 32) // 8)
        G = (G & 0xf8) + (nch % 8)
    pixels[x, y] = (R, G, B)


def convert(string):
    numstr = []
    string = string.encode('windows-1251')
    for i in string:
        numstr.append(i)
    return numstr


def string_to_picture(key, text, x, y):
    global pixels
    visited = set()
    random.seed(key)
    text.append(0x03)  # Признак конца текста
    i = 0
    while True:
        p = random.randint(0, x * y - 1)
        if p in visited:
            continue
        visited.add(p)
        change(text[i], p // y, p % y)
        i += 1
        if text[i - 1] == 0x03:
            break

print('''Введите: путь к начальному изображению; ключ; путь к итоговому изображению''')
data = list(map(str.strip, sys.stdin))
name = data[0]
key = data[1]
name2 = data[2]
text = ''.join(data[3:])

im = Image.open(name)
pixels = im.load()
x, y = im.size
n_text = convert(text)
string_to_picture(key, n_text, x, y)
im.save(name2)
