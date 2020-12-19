from PIL import Image
from Methods import *


def main():
    name = input('введите путь к изображению')
    im = Image.open(name)
    pixels = im.load()
    x, y = im.size
    text = input('введите текст')
    n_text = convert(text)
    key = input('введите ключ')
    string_to_picture(key, n_text)
    name = input('введите путь к изображению')
    im.save(name)


if __name__ == '__main__':
    main()
