from tkinter import Tk, Label, IntVar, Radiobutton, W

root = Tk()
root.title("GUI на Python")
root.geometry("300x250")

header = Label(text="Выберите курс", padx=15, pady=10)
header.grid(row=0, column=0, sticky=W)

lang = IntVar()

python_radiobutton = Radiobutton(text="Python", value=1, variable=lang, padx=15, pady=10)
python_radiobutton.grid(row=1, column=0, sticky=W)

javascript_radiobutton = Radiobutton(text="JavaScript", value=2, variable=lang, padx=15, pady=10)
javascript_radiobutton.grid(row=2, column=0, sticky=W)

selection = Label(textvariable=lang, padx=15, pady=10)
selection.grid(row=3, column=0, sticky=W)

root.mainloop()
