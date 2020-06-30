from tkinter import Tk, Entry, Label, Button, Checkbutton, Radiobutton, IntVar, StringVar, END, messagebox as mbox, W, DISABLED

def close_widow():
    root.destroy()

# Проверка ответа на вопрос 1
def quesans1():
    global score

    b1.config(state=DISABLED)

    if (q1a1_check.get() * q1a2_check.get() * q1a3_check.get() == 1) and \
       (q1a4_check.get() + q1a5_check.get() == 0):
        score += 1
        msg = 'Верно'
    else:
        msg = 'Неверно'

    Label(text=msg).grid(row=7, column=2, sticky=W)

# Проверка ответа на вопрос 2
def quesans2():
    global score

    b2.config(state=DISABLED)

    if current_language_index.get() == 1:
        score += 1
        msg = 'Верно'
    else:
        msg = 'Неверно'

    Label(text=msg).grid(row=15, column=2, sticky=W)

# Проверка ответа на вопрос 3
def quesans3():
    global score

    b3.config(state=DISABLED)

    if ans3.get().lower() == 'да':
        score += 1
        msg = 'Верно'
    else:
        msg = 'Неверно'

    Label(text=msg).grid(row=18, column=2, sticky=W)

def display():
    mbox.showinfo('Результаты теста', name.get() + ' ' + surname.get() + ', вы набрали ' + str(score) + ' очков')

languages = ['Python', 'JavaScript', 'C#', 'Java']
row = 1
score = 0

root = Tk()
root.title('Тест для школьников')
root.geometry('500x500')

name = StringVar()
surname = StringVar()
ans3 = StringVar()

current_language_index = IntVar()
current_language_index.set(-1)

question1 = IntVar()
q1a1_check = IntVar()
q1a2_check = IntVar()
q1a3_check = IntVar()
q1a4_check = IntVar()
q1a5_check = IntVar()

name_label = Label(text='Введите имя:')
surname_label = Label(text='Введите фамилию:')
name_label.grid(row=0, column=0, sticky=W)
surname_label.grid(row=1, column=0, sticky=W)

name_entry = Entry(textvariable=name)
surname_entry = Entry(textvariable=surname)
name_entry.grid(row=0, column=1, sticky=W)
surname_entry.grid(row=1, column=1, sticky=W)

# Вопрос 1
Label(text='Вопрос 1').grid(row=2, column=0, sticky=W)
q1a1 = Checkbutton(text='Button', variable=q1a1_check)
q1a1.grid(row=2, column=1, sticky=W)
q1a2 = Checkbutton(text='Checkbutton', variable=q1a2_check)
q1a2.grid(row=3, column=1, sticky=W)
q1a3 = Checkbutton(text='Listbox', variable=q1a3_check)
q1a3.grid(row=4, column=1, sticky=W)
q1a4 = Checkbutton(text='Label', variable=q1a4_check)
q1a4.grid(row=5, column=1, sticky=W)
q1a5 = Checkbutton(text='Spinbox', variable=q1a5_check)
q1a5.grid(row=6, column=1, sticky=W)
b1 = Button(text='Ответить', command=quesans1)
b1.grid(row=7, column=1, sticky=W)
Label(text='').grid(row=8, column=0, sticky=W)

# Вопрос 2
Label(text='Вопрос 2').grid(row=9, column=0, sticky=W)

for index, language in enumerate(languages):
    r1 = Radiobutton(text=language, value=index, variable=current_language_index)
    r1.grid(row=(9 + index), column=1, sticky=W)
    row += 1

selected_language_label = Label(text='')
selected_language_label.grid(row=14, column=1, sticky=W)

b2 = Button(text='Ответить', command=quesans2)
b2.grid(row=15, column=1, sticky=W)
Label(text='').grid(row=16, column=0, sticky=W)

# Вопрос 3
Label(text='Вопрос 3').grid(row=17, column=0, sticky=W)
ans3_entry = Entry(textvariable=ans3)
ans3_entry.grid(row=17, column=1, sticky=W)

b3 = Button(text='Ответить', command=quesans3)
b3.grid(row=18, column=1, sticky=W)

Button(text='Закончить тест', command=display).grid(row=19, column=1, sticky=W)

root.mainloop()
