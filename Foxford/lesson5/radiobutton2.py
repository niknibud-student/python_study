from tkinter import Tk, Label, Radiobutton, IntVar, W

languages = [("Python", 1), ("JavaScript", 2), ("C#", 3), ("Java", 4)]


def select():
    l = language.get()
    if l == 1:
        selectedLanguageLabel.config(text="Выбран Python")
    elif l == 2:
        selectedLanguageLabel.config(text="Выбран JavaScript")
    elif l == 3:
        selectedLanguageLabel.config(text="Выбран C#")
    elif l == 4:
        selectedLanguageLabel.config(text="Выбран Java")


root = Tk()
root.title("GUI на Python")
root.geometry("300x280")

header = Label(text="Выберите курс", padx=15, pady=10)
header.grid(row=0, column=0, sticky=W)

language = IntVar()

row = 1
for txt, val in languages:
    Radiobutton(text=txt, value=val, variable=language, padx=15, pady=10, command=select) \
        .grid(row=row, sticky=W)
    row += 1

selectedLanguageLabel = Label(padx=15, pady=10)
selectedLanguageLabel.grid(row=row, sticky=W)

root.mainloop()
