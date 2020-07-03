from tkinter import Tk, Button

root = Tk()
colors = ['red','green','yellow','grey','orange','white']

def on_click(event):
    t = event.widget
    print(t.grid_info()['row'], t.grid_info()['column'])

for i in range(6):
    b = Button(root, width = 10, bg = colors[i])
    b.grid(row=0,column=i)
    b.bind('<Button-1>',on_click)
root.mainloop()
