from tkinter import Tk, Button

def change1(event):
    b['fg'] = 'red'
    b['activeforeground'] = 'red'

def change2(event):
    b['fg'] = 'black'
    b['activeforeground'] = 'white'

root = Tk()
b = Button(text='RED', width=10, height=3)

b.bind('<Button-1>', change1)
b.bind('<Button-3>', change2)
b.bind('<Return>', change1)
b.pack()

root.mainloop()
