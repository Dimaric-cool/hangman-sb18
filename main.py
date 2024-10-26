from turtle import *

Screen().setup(800, 700)


shape("turtle")
speed(3)
shapesize(1.5)

pensize(10)

pendown()
for _ in range(4):
    forward(100)
    right(90)
penup()

mainloop()