import sys
from itertools import cycle
from random import randrange
from tkinter import Canvas, Tk, messagebox

# ПАРАМЕТРЫ

canvas_width = 800
canvas_height = 400

color_cycle = cycle(['medium aquamarine', 'aquamarine', 'dark green', 'dark olive green',
                     'dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green',
                     'lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green',
                     'forest green', 'olive drab'])

corona_center_radius = 8
corona_radius = 12
corona_point_radius = 2
score_speed = 10  # получаем 10 очков за каждое пойманное яйцо
y_speed = 1
frame_rate = 16  # 16ms = 60fps
add_interval = 1000  # частота добавления нового яйца
# коэфф сложности6 показывает, с какой частотой должны появляться яйца на экране,
# с какой скоростью падать ( чем ближе к 1, тем проще)
difficulty_factor = 0.995


def create_corona():
    global corona_counter
    x = randrange(10, 740)
    y = 40
    tag = "corona-" + str(corona_counter)  # "egg-%s" % egg_counter
    fill = next(color_cycle)

    corona_radius_45_grad = corona_radius * 0.707

    corona_center = create_circle(x, y, corona_center_radius, tag, fill)

    # add 90degrees corona circles
    create_circle(x + corona_radius, y, corona_point_radius, tag, fill)
    create_circle(x - corona_radius, y, corona_point_radius, tag, fill)
    create_circle(x, y + corona_radius, corona_point_radius, tag, fill)
    create_circle(x, y - corona_radius, corona_point_radius, tag, fill)

    # add 45degrees corona circles
    create_circle(x + corona_radius_45_grad, y + corona_radius_45_grad, corona_point_radius, tag, fill)
    create_circle(x + corona_radius_45_grad, y - corona_radius_45_grad, corona_point_radius, tag, fill)
    create_circle(x - corona_radius_45_grad, y + corona_radius_45_grad, corona_point_radius, tag, fill)
    create_circle(x - corona_radius_45_grad, y - corona_radius_45_grad, corona_point_radius, tag, fill)

    corona_centers.append(corona_center)
    coronas_tags.append(tag)
    corona_counter += 1

    root.after(add_interval, create_corona)
    # root.update()


def create_circle(x, y, radius, tag, fill_color):
    return canvas.create_oval(x - radius, y - radius, x + radius, y + radius, tag=tag, fill=fill_color, width=0)


def move_coronas():
    for corona, tag in zip(corona_centers, coronas_tags):
        (_, corona_y1, _, _) = canvas.coords(corona)
        canvas.move(tag, 0, y_speed)
        if corona_y1 > canvas_height:
            corona_dropped(corona, tag)
    root.after(frame_rate, move_coronas)


def corona_dropped(corona, tag):
    corona_centers.remove(corona)
    coronas_tags.remove(tag)
    canvas.delete(tag)
    increase_score(score_speed)
    if int(live_temperature) >= 40:
        messagebox.showinfo('Ой, заболел!', 'Итоговый счет:' + str(score))
        sys.exit()
        # root.destroy()


def lose_a_life():
    global live_temperature
    live_temperature += 0.8
    update_texts()


def check_catch():
    (catcher_x, catcher_y, catcher_x2, catcher_y2) = canvas.coords(catcher)
    for corona, tag in zip(corona_centers, coronas_tags):
        (x, y, x2, y2) = canvas.coords(corona)
        if catcher_x < x and x2 < catcher_x2 and catcher_y2 - y2 < 40:
            corona_centers.remove(corona)
            coronas_tags.remove(tag)
            canvas.delete(tag)
            lose_a_life()
    root.after(frame_rate, check_catch)


def increase_score(points):
    global score, frame_rate, add_interval, y_speed
    score += points
    # frame_rate = int(frame_rate * difficulty_factor)
    add_interval = int(add_interval * difficulty_factor)
    y_speed = y_speed / difficulty_factor
    update_texts()


def move_left(event):
    x1 = canvas.coords(catcher)[0]
    if x1 > 0:
        canvas.move(catcher_tag, -20, 0)


def move_right(event):
    x2 = canvas.coords(catcher)[2]
    if x2 < canvas_width:
        canvas.move(catcher_tag, 20, 0)


def update_texts():
    canvas.itemconfigure(lives_text, text='Температура: ' + '{0:.1f}'.format(live_temperature))
    canvas.itemconfigure(score_text, text='Счет: ' + str(score))


def draw_catcher():
    global catcher_tag
    catcher_tag = "catcher_tag"
    # задаем параметры корзины
    hands_color = 'tan1'
    head_color = 'tan3'
    mask_color = 'light cyan'
    head_radius = 19
    # nose_color = 'tan2'
    # nose_radius = 7
    hands_radius = 50  # диаметр окружности для рисования дуги
    # зададим начальную позицию человека (у нижнего края по центру холста)
    initial_center_x = canvas_width / 2
    initial_center_y = canvas_height - 20

    # рисуем руки
    hands_start_x = initial_center_x - hands_radius
    hands_start_y = initial_center_y - hands_radius * 2
    hands_start_x2 = initial_center_x + hands_radius
    hands_start_y2 = initial_center_y

    hands = canvas.create_arc(hands_start_x, hands_start_y, hands_start_x2, hands_start_y2, start=200, extent=140, \
                              style='arc', outline=hands_color, width=3, tag=catcher_tag)

    # рисуем нос
    # create_circle(initial_center_x, initial_center_y - head_radius, nose_radius, catcher_tag, nose_color)
    # рисуем голову
    create_circle(initial_center_x, initial_center_y, head_radius, catcher_tag, head_color)

    # рисуем маску
    mask_start_x = initial_center_x - head_radius
    mask_start_y = initial_center_y - head_radius
    mask_start_x2 = initial_center_x + head_radius
    mask_start_y2 = initial_center_y + head_radius
    canvas.create_arc(mask_start_x, mask_start_y, mask_start_x2, mask_start_y2, start=30, extent=120, \
                      style='arc', outline=mask_color, width=5, tag=catcher_tag)

    return hands


def create_background():
    canvas = Canvas(root, width=canvas_width, height=canvas_height, background="black")
    canvas.create_rectangle(-5, canvas_height - 100, canvas_width + 5, \
                            canvas_height + 5, fill="brown", width=0)
    canvas.create_oval(-80, -80, 120, 120, fill="orange", width=0)
    canvas.pack()
    return canvas


root = Tk()
canvas = create_background()

corona_counter = 0
score = 0
score_text = canvas.create_text(10, 10, anchor='nw', font='Timesnewroman', fill='darkblue')
live_temperature = 36.6
lives_text = canvas.create_text(canvas_width - 10, 10, anchor='ne', font='Timesnewroman', fill='white')

update_texts()

corona_centers = []
coronas_tags = []
root.after(frame_rate, create_corona)
root.after(frame_rate, move_coronas)

canvas.bind('<Left>', move_left)
canvas.bind('<Right>', move_right)
canvas.focus_set()

root.after(frame_rate, check_catch)

catcher = draw_catcher()

root.mainloop()
