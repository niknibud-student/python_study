from tkinter import Tk, IntVar, Checkbutton, Label

root = Tk()
root.title("GUI на Python")
root.geometry("300x250")

ismarried = IntVar()

ismarried_checkbutton = Checkbutton(text="Женат/Замужем", variable=ismarried)
ismarried_checkbutton.pack()

ismarried_label = Label(textvariable=ismarried)
ismarried_label.pack()

root.mainloop()
