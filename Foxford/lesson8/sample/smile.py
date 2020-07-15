# -*- coding: utf-8 -*-
#import turtle
from turtle import reset, width, circle, up, down, right, forward, goto, begin_fill, end_fill, color, done

reset()
#tracer(0)
width(2)
#
up()
x=0
y=-100
goto(x, y)
begin_fill()
color('#ffaa00')
down()
circle(100)
end_fill()
color('black')
circle(100)
up()
#
x=-45
y=50
goto(x, y)
down()
color('#0000aa')
begin_fill()
circle(7)
up()
end_fill()
#
x=45
y=50
goto(x, y)
down()
color('#0000aa')
begin_fill()
circle(7)
up()
end_fill()
#
x=-55
y=-50
goto(x, y)
right(45)
width(3)
down()
color('#aa0000')

circle(80, 90)
up()
#
x=0
y=50
goto(x, y)
right(135)
width(3)
down()
color('#000000')
forward(100)
up()
#
done()
