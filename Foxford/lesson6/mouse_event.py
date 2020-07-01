from tkinter import Tk


def b1(event):
    root.title('Нажата левая кнопка мыши')


def b2(event):
    root.title('Нажата правая кнопка мыши')


def move(event):
    x = event.x
    y = event.y
    root.title('Движение мышью {}x{}'.format(x, y))


root = Tk()
root.minsize(width=500, height=500)
root.bind('<Button-1>', b1)
root.bind('<Button-3>', b2)
root.bind('<Motion>', move)
root.mainloop()
