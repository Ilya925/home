from turtle import *

colormode(255)
shape('turtle')

color((117, 2, 84), (238, 242, 22))
pensize(4)
speed(0.5)



#begin_fill()

# for _ in range(4):
#     fd(100)
#     left(90)
# end_fill()
# fillcolor('#16F21A')
# begin_fill()
#
# for _ in range(3):
#     forward(100)
#     left(120)
# end_fill()
# fillcolor((238, 242, 22))
# # fd(100)
# backward(100)
# penup()
# pendown()
# goto(-100, 100)
r =191
g = 33
b = 142
step = 0
for i in range(200, 10, -20):
    fillcolor(r, g, b)
    for _ in range(6):
        begin_fill()
        for _ in range(3):
            fd(i)
            lt(120)
        # circle(i)
        end_fill()
        rt(60)
    r += 5
    g += 10
    b += 5
    # penup()
    # step -= 150
    # goto(step, 0)
    # pendown()
penup()
goto(0, 0)
pendown()
mainloop()