# -*- coding:utf-8 -*-
import os
from tkinter import *
from PIL import Image, ImageTk

def apply_colors(sample_image, color1, color2):
    size = sample_image.size
    im = Image.new('RGBA', size)

    for x in range(size[0]):
        for y in range(size[1]):
            r,g,b,a = sample_image.getpixel((x,y))
            if r == 82 and g == 140 and b == 42:
                im.putpixel((x,y), (color1[0], color1[1], color1[2], a)) #color1
            elif r == 31 and g == 202 and b == 122:
                im.putpixel((x,y), (color1[0] + 50, color1[1] + 50, color1[2] + 80, a)) #color1 Lightness
            elif r == 34 and g == 74 and b == 34:
                im.putpixel((x,y), (color1[0] - 50, color1[1] - 70, color1[2] - 80, a)) #color1 Darkness
            elif r == 158 and g == 228 and b == 98:
                im.putpixel((x,y), (color2[0], color2[1], color2[2], a)) #color2
            elif r == 200 and g == 240 and b == 134:
                im.putpixel((x,y), (color2[0] + 50, color2[1] + 20, color2[2] + 40, a)) #color2 Lightness
            elif r == 46 and g == 156 and b == 48:
                im.putpixel((x,y), (color2[0] - 100, color2[1] - 70, color2[2] -80, a)) #color2 Darkness
            elif r == 128 and g == 96 and b == 64:
                im.putpixel((x,y), (int((color1[0] + 160) / 2), int((color1[1] + 96) / 2), int((color1[2] + 64) / 2), a))#color1 mixed mud
            else:
                im.putpixel((x,y), (r, g, b, a))
    return im


class ImageFrame(Frame):
    _image_label = None
    image = None
    _render_image = None
    sample_image = None
    color1 = [50, 27, 100]
    color2 = [100, 20, 100]
    save_path = 'generated/ore.png'

    def __init__(self, master=None, width=300, height=300):
        #Load sample image
        image_original = Image.open("sample.png").convert('RGBA')
        Frame.__init__(self, master, width=width, height=height)
        self.master = master

        self.sample_image = image_original.copy()
        self.image = image_original.copy()
        render = ImageTk.PhotoImage(self.image)
        self._image_label = Label(self, image=render)
        self._image_label.image = render
        self._image_label.pack()


    def Save(self):
        self.image.save(self.save_path)


    def SetImage(self, image):
        self.image = image.copy()
        self._render_image = ImageTk.PhotoImage(image)
        self._image_label.configure(image=self._render_image)


class ToolFrame(Frame):
    image_frame = None
    color1 = (50, 27, 100)
    color2 = (100, 20, 100)

    def __init__(self, master=None, image_frame=None, width=300, height=300):
        Frame.__init__(self, master, width=width, height=height)
        self.master = master
        self.image_frame = image_frame

        color1_scale_r = Scale(self, length=290, to=255, orient=HORIZONTAL, command=lambda x: self.SetColor((int(x), self.color1[1], self.color1[2]), self.color2))
        color1_scale_r.set(self.color1[0])
        color1_scale_r.pack()
        color1_scale_g = Scale(self, length=290, to=255, orient=HORIZONTAL, command=lambda x: self.SetColor((self.color1[0], int(x), self.color1[2]), self.color2))
        color1_scale_g.set(self.color1[1])
        color1_scale_g.pack()
        color1_scale_b = Scale(self, length=290, to=255, orient=HORIZONTAL, command=lambda x: self.SetColor((self.color1[0], self.color1[1], int(x)), self.color2))
        color1_scale_b.set(self.color1[2])
        color1_scale_b.pack()

        color2_scale_r = Scale(self, length=290, to=255, orient=HORIZONTAL, command=lambda x: self.SetColor(self.color1, (int(x), self.color2[1], self.color2[2])))
        color2_scale_r.set(self.color2[0])
        color2_scale_r.pack()
        color2_scale_g = Scale(self, length=290, to=255, orient=HORIZONTAL, command=lambda x: self.SetColor(self.color1, (self.color2[0], int(x), self.color2[2])))
        color2_scale_g.set(self.color2[1])
        color2_scale_g.pack()
        color2_scale_b = Scale(self, length=290, to=255, orient=HORIZONTAL, command=lambda x: self.SetColor(self.color1, (self.color2[0], self.color2[1], int(x))))
        color2_scale_b.set(self.color2[2])
        color2_scale_b.pack()

        save_button = Button(self, text="save", command=self.image_frame.Save)
        save_button.pack()

    def SetColor(self, color1, color2):
        self.color1 = color1
        self.color2 = color2
        image = apply_colors(self.image_frame.sample_image.copy(), color1, color2)
        self.image_frame.SetImage(image)


root = Tk()
image_frame = ImageFrame(root)
image_frame.grid(row=0, column=0)

tool_frame = ToolFrame(root, image_frame)
tool_frame.grid(row=1, column=0)

root.wm_title("Terraria ore generator")
root.geometry("300x560")
root.mainloop()
