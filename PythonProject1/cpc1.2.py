# import turtle
# t = turtle.Turtle()
# t.ht()
# ##прямоугольник
# t.penup()
# t.goto(-300, 100)  # Перемещаемся в начальную точку
# t.pendown()
# t.color('red')
# t.begin_fill()
#
# t.forward(150)
# t.left(90)
# t.forward(70)
# t.left(90)
# t.forward(150)
# t.left(90)
# t.forward(70)
# t.left(90)
# t.end_fill()
#
#
# ## ромб, но лежит на боку
# t.penup()
# t.goto(-100, 100)   # Перемещаем в новую точку
# t.pendown()
# t.color('pink') ##заливка
# t.begin_fill()
#
# t.forward(100)
# t.left(60)
# t.forward(100)
# t.left(120)
# t.forward(100)
# t.left(60)
# t.forward(100)
# t.left(120)
# t.end_fill()
#
# ##трапеция
# t.penup()
# t.goto(200, 100)
# t.pendown()
# t.color('violet')
# t.begin_fill()
# t.backward(70)
# t.right(60)
# t.backward(80)
# t.right(120)
# t.backward(150)
# t.right(120)
# t.backward(80)
#
# t.end_fill()
#
# turtle.done()

from turtle import *

colormode(255)
shape('turtle')
color((237, 17, 17), (219, 237, 17))
pensize(3)
speed(0.51)