# import turtle
#
# # Создаём объект черепашки
# t = turtle.Turtle()
# t.ht()
# t.penup()
# t.goto(-150, 130)  # Перемещаемся в начальную точку
# t.pendown()
# t.color('brown')  # Устанавливаем цвет (коричневый)
# t.begin_fill()     # Начинаем заливку
# t.circle(60)        # Рисуем круг
# t.end_fill()      # Завершаем заливку
#
#
# t.penup()
# t.goto(100, 120)   # Перемещаем в новую точку
# t.pendown()
# t.color('green')  # Устанавливаем цвет (зелёный)
# t.begin_fill()     # Начинаем заливку
# t.circle(90)        # Рисуем круг
# t.end_fill()      # Завершаем заливку
#
#
# t.penup()
# t.goto(0, -50)   # Перемещаем в новую точку
# t.pendown()
# t.color('blue')     # Устанавливаем цвет (синий)
# t.begin_fill()     # Начинаем заливку
# t.circle(70)        # Рисуем круг
# t.end_fill()      # Завершаем заливку
#
#
# turtle.done()


from turtle import *

colormode(255)
shape('turtle')
color((237, 17, 17), (219, 237, 17))
pensize(3)
speed(0.51)
r =219
g = 237
b = 17
step = 0
for i in range(80, 20, -20):
    fillcolor(r, g, b)
    begin_fill()
    circle(i)
    r -= 50
    g = 100
    b += 50
    end_fill()
    penup()
    step -= 150
    goto(step, 0)
    pendown()
#end_fill()
penup()
goto(0, 0)
pendown()
mainloop()






