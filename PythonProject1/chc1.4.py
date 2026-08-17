import turtle
t = turtle.Turtle()
t.ht()

t.penup()
t.goto(-100, 0)  # Перемещаемся в начальную точку
t.pendown()
for i in range(4):
  t.forward(30)
  t.left(90)

t.penup()
t.goto(-40, 0)  # второй через 30 пикс от первого
t.pendown()
for i in range(4):
  t.forward(30)
  t.left(90)

t.penup()
t.goto(20, 0)  # третий через 30 пикс от второго
t.pendown()
for i in range(4):
  t.forward(30)
  t.left(90)

turtle.done()