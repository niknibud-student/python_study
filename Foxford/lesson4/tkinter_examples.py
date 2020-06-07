from tkinter import *
def change():
    b1['text'] = 'Изменено'
    b1['bg'] = 'yellow'
    b1['activebackground'] = 'yellow'
    b1['fg'] = 'blue'
    b1['activeforeground'] = '#ffffff'

root = Tk()
'''l1 = Label(text="Python", font='Arial 32')
l2 = Label(text="Tkinter", font=('Comic Sans MS', 24, 'bold'))
l1.config(bd=20, bg='#ffaaaa')
l2.config(bd=20, bg='#aaffff')
l1.pack()
l2.pack()
b1 = Button(text='Изменить', width=15, height=3, background='blue')
b2 = Button(width=20, background='blue')
b3 = Button(width=15, height=3, background='blue')
b4 = Button(width=25, height=5, background='blue')
b2['text'] = 'Кнопка 2'
b3.config(text = 'кнопка 3')
b4.configure(text = 'кнопка 4')
b1.config(command=change)
b1.pack()
b2.pack()
b3.pack()
b4.pack()

Button(root, text='1').grid(row=1, column=1)
Button(root, text='2').grid(row=1, column=2)
Button(root, text='__3__').grid(row=2, column=1, columnspan=2)
'''


root.mainloop()