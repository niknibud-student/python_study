# Приложение Календарь событий

from tkinter import Tk, Canvas
from datetime import datetime, date


# Функция возвращает список событий и дат этих событий
def get_events(filname):
    date_list = []
    name_list = []

    with open(filname, encoding='utf-8') as file:
        for line in file:
            # удаляем символ перевода строки и разбиваем строку на название события и дату по ", "
            text = line.rstrip('\n').split(', ')
            #print(text)
            # преобразуем второй элемент списка в дату
            date_list.append(datetime.strptime(text[1], '%d/%m/%Y').date())
            name_list.append(text[0])

    return name_list, date_list


# Функция определяет день недели события
def which_weekday(day_of_week):
    weekday = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
    day_type = 'будний день' if day_of_week < 5 else 'выходной'
    return day_type + ' ' + weekday[day_of_week]


# Функция возвращает сообщение от количестве дней до или после события
def days_before_event(today, event_date, event_name):
    if today > event_date:
        period = today - event_date
        message = 'Праздник {} уже прошёл {} дней назад.\nЭто был {}.'\
            .format(event_name, period.days, which_weekday(date.weekday(event_date)))
    elif today.day == event_date.day and today.month == event_date.month \
        and today.year == event_date.year:
        message = '{} сегодня'.format(event_name)
    else:
        period = event_date - today
        message = 'До праздника {} осталось {} дней.\nЭто будет {}.'\
            .format(event_name, period.days, which_weekday(date.weekday(event_date)))
    return message


event_name_list, event_date_list = get_events('events.txt')
today = date.today()

for i in range(len(event_name_list)):
    print(days_before_event(today, event_date_list[i], event_name_list[i]))

# Создаем окно Tk
window = Tk()
# Создаем холст
canvas = Canvas(window, width=700, height=600, bg='yellow')
# Помещаем холст в окно Tk
canvas.pack()
# Пишем текст на холсте
canvas.create_text(200, 50, fill='black', anchor='w', justify='center', font='"Times New Roman" 20 bold',
                   text='Первое приложение.\nКалендарь ожидания')

vertical_space = 120

for i in range(len(event_name_list)):
    display = days_before_event(today, event_date_list[i], event_name_list[i])
    canvas.create_text(25, vertical_space, anchor='w', fill='blue', font='Arial 14 bold', text=display)
    vertical_space += 50

window.mainloop()