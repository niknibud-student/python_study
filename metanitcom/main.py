from tkinter import *

def clickButton():
    global clicks
    clicks +=1
    btnText.set('Clicks {}'.format(clicks))

def clickButton2():
    clicks.set(clicks.get() + 1)
    
    
root = Tk()
root.title('Графическая программа на Python')

clicks = IntVar()
clicks.set(0)

sc_width = root.winfo_screenwidth()
sc_height = root.winfo_screenheight()
width = 400
height = 300

# Окно по центру экрана
root.geometry('{}x{}+{}+{}'.format(width, height, (sc_width - width) // 2, (sc_height - height) // 2))

# btnText = StringVar()
# btnText.set('Clicks {}'.format(clicks.get()))

Button(textvariable=clicks,
       bg='#555',
       fg='#ccc',
       padx=20,
       pady=8,
       font='Verdana 16',
       command=clickButton2).pack()

root.mainloop()