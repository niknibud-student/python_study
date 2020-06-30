from tkinter import Tk, IntVar, Checkbutton, W

root = Tk()
root.title("GUI на Python")
root.geometry("300x250")

python_lang = IntVar()
python_checkbutton = Checkbutton(text="Python", variable=python_lang,
                                 onvalue=1, offvalue=0, padx=15, pady=10)
python_checkbutton.grid(row=0, column=0, sticky=W)

javascript_lang = IntVar()
javascript_checkbutton = Checkbutton(text="JavaScript", variable=javascript_lang,
                                     onvalue=1, offvalue=0, padx=15, pady=10)
javascript_checkbutton.grid(row=1, column=0, sticky=W)

root.mainloop()
