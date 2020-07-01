from tkinter import Tk, Canvas

root = Tk()

canvas = Canvas(width=300, height=300, bg='white')
canvas.focus_set()
canvas.pack()

ball = canvas.create_oval(140, 140, 160, 160, fill='green')

canvas.bind('<Up>', lambda event: canvas.move(ball, 0, -2))
canvas.bind('<Down>', lambda event: canvas.move(ball, 0, 2))
canvas.bind('<Left>', lambda event: canvas.move(ball,-2, 0))
canvas.bind('<Right>', lambda event: canvas.move(ball, 2, 0))

root.mainloop()
