import random
# import tkinter
from turtle import Turtle, Screen

BREAK_FLAG = False
w = Screen()
w.setup(500, 500)
w.bgcolor('yellow')
t = Turtle()
t.penup()
t.hideturtle()

def outside_window():
    left_wall = -w.window_width() / 2
    right_wall = w.window_width() / 2
    top_wall = w.window_height() / 2
    bottom_wall = -w.window_height() / 2
    (x, y) = snake[0].pos()
    outside = x < left_wall or x > right_wall or y < bottom_wall or y > top_wall
    return outside


def game_over():
    #snake[0].color('blue')
    leaf.color('yellow')
    t.write('Конец игры!', align='center', font=('Arial', 30, 'normal'))


def display_score(current_score):
    score_turtle.clear()
    score_turtle.penup()
    x = (w.window_width() / 2) - 50
    y = (w.window_height() / 2) - 50
    score_turtle.setpos(x, y)
    score_turtle.write(str(current_score), align='right', font=('Arial', 40, 'bold'))


def place_leaf():
    leaf.ht()
    leaf.setx(random.randint(-200, 200))
    leaf.sety(random.randint(-200, 200))
    leaf.st()
'''
def place_flower():
    flower.ht()
    flower.setx(random.randint(-200, 200))
    flower.sety(random.randint(-200, 200))
    flower.st()
'''

snake = []
snake_speed = 10
snake_length = 3
score = 0

def create_snake():
    global snake
    for i in range(snake_length):
        snake_segment = Turtle()
        snake_segment.shape('square')
        snake_segment.shapesize(1,1)
        snake_segment.penup()

        #snake_segment.speed(snake_speed)

        if i > 0:
            snake_segment.color('blue')


        snake.append(snake_segment)
        #snake[i].shapesize(1, 1, 1)


def body_movement():
    global snake
    for i in range(len(snake) - 1, 0, -1):
        x = snake[i - 1].xcor()
        y = snake[i - 1].ycor()

        snake[i].goto(x, y)
        snake[i].showturtle()
        # snake[i].speed(snake_speed)
        # snake head movement

    snake[0].forward(snake_speed)
    snake[0].speed(snake_speed)


def check_leaf_is_eaten():
    # and redraw a food for the snake
    if snake[0].distance(leaf) < 20:
        place_leaf()
        return True
    else:
        False


def create_new_segment():
    global score, snake, snake_speed
    if check_leaf_is_eaten() :
        score = score + 10
        display_score(score)
        new_snake_segment = Turtle()
        new_snake_segment.hideturtle()
        new_snake_segment.shape('square')
        new_snake_segment.color('blue')
        new_snake_segment.penup()
        snake.append(new_snake_segment)


def start_game():
    global game_started, snake_speed, snake_length, score, BREAK_FLAG
    if game_started:
        return
    game_started = True
    text_turtle.clear()
    create_snake()
    display_score(score)
    place_leaf()

    while True:
        if snake_speed < 10:
            snake_speed = snake_speed + 1
        body_movement()
        create_new_segment()
        '''
        for i in snake[4:]:
            i = i.position()
            if snake[0].distance(i) < 20:

                BREAK_FLAG = True
            if BREAK_FLAG:
                w.bgcolor('red')
                break
            w.update()
'''
        if outside_window():
            game_over()
            break



def move_up():
    if snake[0].heading() == 0 or snake[0].heading() == 180:
        snake[0].setheading(90)


def move_down():
    if snake[0].heading() == 0 or snake[0].heading() == 180:
        snake[0].setheading(270)


def move_left():
    if snake[0].heading() == 90 or snake[0].heading() == 270:
        snake[0].setheading(180)


def move_right():
    if snake[0].heading() == 90 or snake[0].heading() == 270:
        snake[0].setheading(0)



leaf = Turtle()
leaf_shape = ((0, 0), (14, 2), (18, 6), (20, 20), (6, 18), (2, 14))
w.register_shape('leaf', leaf_shape)
leaf.shape('leaf')
leaf.color('green')
leaf.penup()
leaf.hideturtle()
leaf.speed(0)


game_started = False

text_turtle = Turtle()
text_turtle.write('Нажмите пробел, чтобы начать игру', align='center', font=('Arial', 16, 'bold'))
text_turtle.hideturtle()

score_turtle = Turtle()
score_turtle.hideturtle()
score_turtle.speed(0)

w.onkey(start_game, 'space')

w.onkey(move_up, "Up")
w.onkey(move_right, "Right")
w.onkey(move_down, "Down")
w.onkey(move_left, "Left")
w.listen()
w.exitonclick()
w.mainloop()
