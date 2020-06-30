from tkinter import Tk, Entry, Button, Label, StringVar, messagebox as mbox, END

def clear():
    name_entry.delete(0, END)
    surname_entry.delete(0, END)

def display_full_name():
    mbox.showinfo('GUI Python', name.get() + ' ' + surname.get())

root = Tk()
root.title('GUI на Python')

name = StringVar()
surname = StringVar()

name_label = Label(text='Введите имя:')
surname_label = Label(text='Введите фамилию:')

name_label.grid(row=0, column=0, sticky='w')
surname_label.grid(row=1, column=0, sticky='w')

name_entry = Entry(textvariable=name)
surname_entry = Entry(textvariable=surname)

name_entry.insert(0, 'Tom')
surname_entry.insert(0, 'Soyer')

name_entry.grid(row=0, column=1, padx=5, pady=5)
surname_entry.grid(row=1, column=1, padx=5, pady=5)

message_button = Button(text='Display', command=display_full_name)
message_button.grid(row=2, column=0, padx=5, pady=5, sticky='e')

clear_button = Button(text='Clear', command=clear)
clear_button.grid(row=2, column=1, padx=5, pady=5, sticky='e')

root.mainloop()
