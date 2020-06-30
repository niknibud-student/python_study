from tkinter import Tk, Entry, Button, END
from tkinter import messagebox
from tkinter import ttk
import math
import sys

#Следующими двумя строками мы создаем окно и даем ему имя.

root = Tk()
root.title("Calculator")

#Создаем список с именами будущих кнопок калькулятора. Я выбрал все самые интересные функции, чтобы продемонстрировать, как их реализовать.

bttn_list = [
"7", "8", "9", "+", "*",
"4", "5", "6", "-", "/",
"1", "2", "3",  "=", "xⁿ",
"0", ".", "±",  "C",
"Exit", "π", "sin", "cos",
"(", ")","n!","√2", ]

#Следующим отрезком кода мы создаем кнопки для нашего калькулятора.

r = 1
c = 0
for i in bttn_list:
    rel = ""
    cmd=lambda x=i: calc(x)
    ttk.Button(root, text=i, command = cmd, width = 10).grid(row=r, column = c)
    c += 1
    if c > 4:
        c = 0
        r += 1

#В каждом калькуляторе есть, так называемое поле ввода, в которое пользователь вводит нужные данные для программы. Это могут быть цифры, функции и математические операции. Их можно вводить, как с клавиатуры, так и при нажатии на кнопку в калькуляторе.

#Пример 1. Я нажимаю на кнопку «2» в калькуляторе и в этом поле ввода, отображается цифра 2.

#В Python Tkinter поле ввода называется Entry

calc_entry = Entry(root, width = 33)
calc_entry.grid(row=0, column=0, columnspan=5)

#Мы подошли к основной задаче калькулятора — его функциям и логике.
#До этого момента нами было создан внешний вид программы. Если бы Вы попробовали запустить ее и нажать на кнопку,
# Вам бы выскочила ошибка, ведь у нас вовсе нет функций калькулятора.
#Приступим, пропишем нашему калькулятору логику и способность считать.

#логика калькулятора
def calc(key):
    if key == "=":
#исключение написания слов
        str1 = "-+0123456789.*/)("
#Этой кода мы разрешаем пользователю вводить только символы -+0123456789.*/)(, а остальные исключаем, запрещаем вводить.

        if calc_entry.get()[0] not in str1:
            calc_entry.insert(END, "First symbol is not number!")
            messagebox.showerror("Error!", "You did not enter the number!")
#исчисления
        try:
            result = eval(calc_entry.get())
            calc_entry.insert(END, "=" + str(result))
        except:
            calc_entry.insert(END, "Error!")
            messagebox.showerror("Error!", "Check the correctness of data")



#В этом блоке кода мы используем функцию eval — это, если можно так сказать, компилятор внутри компилятора. Она будет считать в нашей программе.

#По сути, мы обрабатываем функцию, что сработает при нажатии на кнопку "=".

#Создаем функцию очищения поля ввода. Она будет срабатывать при нажатии на кнопку «C».

#очищение поля ввода
    elif key == "C":
        calc_entry.delete(0, END)

#Создаем функцию изменения минуса на плюс.
#Пример 2. Мы ввели в окно Entry 5, при нажатии на кнопку "±", калькулятор выведет -5.
#И наоборот, мы ввели -5, нажали на кнопку "±" и получили ответ от программы 5.


    elif key == "±":
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
        try:
            if calc_entry.get()[0] == "-":
                calc_entry.delete(0)
            else:
                calc_entry.insert(0, "-")
        except IndexError:
            pass

#Следующая функция — число pi. При нажатии на кнопку «П» программа выведет нам 3.14159265359, то есть число Pi. Вот тут нам и пригодилась библиотека math.

    elif key == "π":
        calc_entry.insert(END, math.pi)

#Функция выхода из программы. При нажатии на кнопку «Exit» окно Tkinter будет уничтожено и процесс остановлен. В этой функции нам нужна была библиотека sys.

    elif key == "Exit":
        root.after(1,root.destroy)
        sys.exit

#Функция возведения в степень. Нужно ввести число, которое нужно возвести в степень. Далее программа выводит **. В Python этот символ означает возведение в степень 2**6 (возведение 2 в степень 6). Мы используем для счета в программе eval, а значит можно выполнить это так же, как и в Питоне. Ну и в конце мы вводим необходимую степень.
#Пример 3. Нам нужно 3 возвести в 5 степень. Вводим число 3, нажимаем на кнопку «xⁿ» (3**...) и вводим необходимую степень, — 5 (3**5). Нажимаем на кнопку "=" и получаем ответ 243.

    elif key == "xⁿ":
        calc_entry.insert(END, "**")

#Опишу сразу две функции, так, как они идентичны.
#Функция sin x и cos x.

#Все просто, при нажатии на клавишу sin или же cos мы получаем синус или косинус по данному числу.

    elif key == "sin":
        calc_entry.insert(END, "=" + str(math.sin(int(calc_entry.get()))))
    elif key == "cos":
        calc_entry.insert(END, "=" + str(math.cos(int(calc_entry.get()))))

#Следующие две функции — скобки ) и (.
#При нажатии на кнопку ")" мы получаем ), аналогично поступаем со второй функцией.

    elif key == "(":
        calc_entry.insert(END, "(")
    elif key == ")":
        calc_entry.insert(END, ")")

#Функция получения факториала из данного числа.

    elif key == "n!":
        calc_entry.insert(END, "=" + str(math.factorial(int(calc_entry.get()))))

#Функция извлечения корня квадратного их данного числа.

    elif key == "√2":
        calc_entry.insert(END, "=" + str(math.sqrt(int(calc_entry.get()))))

#Функция, которая отвечает за очищение поля ввода при нажатии на кнопку "=".

    else:
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
        calc_entry.insert(END, key)

#И последняя строка нашего кода — это «закрытие» окна tkinter.

root.mainloop()
