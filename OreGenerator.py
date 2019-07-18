#coding:utf-8
from PIL import Image

foldername = 'C:/folder/folder/'#Write your folder
color1 = [50, 27, 100]#Choose RGB first
color2 = [100, 20, 100]#Choose RGB second

sample = Image.open("sample.png")
rgb_im = sample.convert('RGB')
size = rgb_im.size
im = Image.new('RGBA', size)

for x in range(size[0]):
    for y in range(size[1]):
        r,g,b = rgb_im.getpixel((x,y))
        if r == 82 and g == 140 and b == 42:
            im.putpixel((x,y), (color1[0], color1[1], color1[2]))#color1
        elif r == 31 and g == 202 and b == 122:
            im.putpixel((x,y), (color1[0] + 50, color1[1] + 50, color1[2] + 80))#color1 Lightness
        elif r == 34 and g == 74 and b == 34:
            im.putpixel((x,y), (color1[0] - 50, color1[1] - 70, color1[2] - 80))#color1 Darkness
        elif r == 158 and g == 228 and b == 98:
            im.putpixel((x,y), (color2[0], color2[1], color2[2]))#color2
        elif r == 200 and g == 240 and b == 134:
            im.putpixel((x,y), (color2[0] + 50, color2[1] + 20, color2[2] + 40))#color2 Lightness
        elif r == 46 and g == 156 and b == 48:
            im.putpixel((x,y), (color2[0] - 100, color2[1] - 70, color2[2] -80))#color2 Darkness
        elif r == 128 and g == 96 and b == 64:
            im.putpixel((x,y), (int((color1[0] + 160) / 2), int((color1[1] + 96) / 2), int((color1[2] + 64) / 2)))#color1 mixed mud
        else:
            im.putpixel((x,y), (r, g, b))


im.save(foldername + '/ore.png')
