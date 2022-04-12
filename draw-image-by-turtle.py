# import packages
import webcolors
import turtle as t
from PIL import Image
from turtle import Screen


def start():
    """Provid the image address then it will start to draw that image with python - turtle automatically exactly like the image"""

    picture = input("Picture: ")
    screen = Screen()
    filename = picture
    screen.colormode(255)
    img = Image.open(filename)
    width, height = img.size
    rgb_img = img.convert("RGB")
    t.speed(0)

    offset_x = -(width / 2)
    offset_y = height / 2

    drawing(width, height, rgb_img, offset_x, offset_y)


def drawing(width, height, rgb_img, offset_x, offset_y):
    x = 0
    y = 0
    t.penup()
    t.setposition(offset_x, offset_y)
    t.pendown()
    t.shape("turtle")
    t.delay(0)

    for i in range(height):
        for i in range(width):
            t.pendown()
            r, g, b = rgb_img.getpixel((x, y))
            t.pencolor(r, g, b)
            t.color(r, g, b)
            t.setposition(x + offset_x, -y + offset_y)
            x = x + 1

        y = y + 1
        x = 0
        t.penup()
        t.setposition(x + offset_x, -y + offset_y)
        t.pendown()
        print("current_line ", y, " of ", height)
    print("finished")


start()
