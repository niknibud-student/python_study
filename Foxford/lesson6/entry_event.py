from tkinter import Tk, Entry, Label, Widget, X, END


def close_window(event):
    root.destroy()


def inLabel(event):
    label.config(text=entry.get())


def selectAll(event):
    root.after(10, select_all, event.widget)


def select_all(widget):
    widget.selection_range(0, END)
    widget.icursor(END)


root = Tk()
root.bind('<Control-q>', close_window)

entry = Entry(width=40)
entry.focus_set()
entry.bind('<Return>', inLabel)
entry.bind('Control-a', selectAll)
entry.pack()

label = Label(height=3, fg='orange', bg='darkgreen', font='Verdana 24')
label.pack(fill=X)

root.mainloop()
