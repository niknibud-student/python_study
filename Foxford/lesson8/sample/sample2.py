from turtle import Turtle, done

t = Turtle()
t.screen.screensize(600, 600)

def draw_rect(width, height):
    for i in range(2):
        t.left(90)
        t.fd(height)
        t.left(90)
        t.fd(width)


draw_rect(320, 200)

done()
