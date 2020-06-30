from tkinter import Tk, Entry, Button

def insert():
    e1.insert(0, 'Tkinter - GUI ')

root = Tk()
e1 = Entry(width=50)
e1.pack()
Button(text='Вставить', command=insert).pack()
root.mainloop()
