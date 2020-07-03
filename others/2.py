from tkinter import Tk, Canvas
from math import sqrt
import time


distance = 0


def click(event):
    global distance

    x = event.x
    y = event.y
    ball_center_x = c.coords(ball)[2] - 20
    ball_center_y = c.coords(ball)[1] + 20
    vector_x = x - ball_center_x
    vector_y = y - ball_center_y
    distance = sqrt(vector_x ** 2 + vector_y ** 2)
    dx = vector_x / distance
    if vector_y == 0:
        dy = 0
    else:
        dy = vector_y / distance

    while distance > 0:
        time.sleep(.01)
        c.move(ball, dx, dy)
        c.update()
        distance = distance - 1


root = Tk()
c = Canvas(root, width=500, height=500)
c.pack()
ball = c.create_oval(0, 100, 40, 140, fill="green")
c.bind("<Button-1>", click)
root.mainloop()
