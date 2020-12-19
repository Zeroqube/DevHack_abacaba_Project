from PIL import pillow

def change(ch, x, y):
    global pixels
    R, G, B = *pixels[x, y]
    R = R // 8 + ch// 32
    G = G // 7 + ch % 32 // 8
    B = B // 8 + ch % 8
    pixels[x, y] = (R, G, B)



def convert(string):
    numstr = []
    string = string.encode('windows-1251')
    for i in string:
        numstr.append(i)
    return numstr


print(convert(input()))