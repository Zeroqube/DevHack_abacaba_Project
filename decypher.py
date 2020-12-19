from PIL import Image
import random


def revert(numstr):
    string = ""
    for i in numstr:
        string += i.decode('windows-1251')
    return string

def picture_to_string(key, x, y, n):
    numstr = []
    random.seed(key)
    for i in range(n):
        p = random.randint(0, x * y)
        numstr.append(R % 8 + G % 4 + B % 8)
    return numstr