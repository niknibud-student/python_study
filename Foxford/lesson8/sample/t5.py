from turtle import Turtle, done

t = Turtle()
t.screen.setup(800, 800)
t.up()
t.goto(-450, 0)
t.down()
t.setheading(270)

for _ in range(5):
    t.circle(50, 180)
    t.begin_fill()
    t.circle(-50, 180)
    t.end_fill()

done()
