from tkinter import Tk, Canvas

root = Tk()
canvas = Canvas(width=500, height=500)
oval = canvas.create_oval(20, 40, 70, 90, fill='orange')
canvas.pack()

#point1 = canvas.create_oval(45-2, 30-2, 45+2, 30+2, fill='black')
#point2 = canvas.create_oval(20-2, 40-2, 20+2, 40+2, fill='black')
#point3 = canvas.create_oval(80-2, 100-2, 80+2, 100+2, fill='black')
point4 = canvas.create_oval(30-2, 65-2, 30+2, 65+2, fill='black')
point5 = canvas.create_oval(45-2, 65-2, 45+2, 65+2, fill='black')

root.mainloop()