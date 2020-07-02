from tkinter import Tk, Canvas
import math


def create_circle(canvas, x, y, radius, color, tag):
    return canvas.create_oval(x-radius, y-radius, x+radius, y+radius, fill=color, width=0, tag=tag)


def create_line_under_ungle(canvas, x, y, width, ungle, color, tag):
    ungle *= math.pi/180

    x2 = round(width*math.sin(ungle)+x)
    y2 = round(width*math.cos(ungle)+y)

    return canvas.create_line(x, y, x2, y2, width=2, fill=color, tag=tag)

def motion(tag):
    canvas.move(tag, 10, -3)
    #for sunray in sunrays:
    #    canvas.move(sunray, 10, -3)
    if canvas.coords(tag)[2] < 500:
        root.after(1000, motion(tag))


# Начальные данные
x = 0
y = 150
radius = 40
color = 'orange'
tag = 'sun'

root = Tk()
root.geometry("500x500")
canvas = Canvas(root, width=500, height=500)
sun = create_circle(canvas, x, y, radius, color, tag)

# рисуем лучи
sunrays = []
for i in range(0, 360, 15):
    sunrays.append(create_line_under_ungle(canvas, x, y, 60, i, color, tag))

canvas.pack()

motion(tag)

root.mainloop()
