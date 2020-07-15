from turtle import Turtle, done

t = Turtle()
t.screen.setup(800, 800)

def draw_circle_with_dots(quantity_dots, radius_dot, radius_circle):
    for _ in range(quantity_dots):
        t.circle(radius_circle, 360 / quantity_dots)
        t.dot(radius_dot, "red")

t.up()
t.goto(350, 0)
t.setheading(90)
t.down()

draw_circle_with_dots(45, 10, 350)
done()
