import turtle
import math

pen = turtle.Turtle()
pen.speed(500)

window = turtle.Screen()
window.bgcolor("#000000")
pen.color("yellow")

batman = 20

pen.left(90)
pen.penup()
pen.goto(-7 * batman, 0)
pen.pendown()

for a in range(-7 * batman, -3 * batman, 1):
    x = a / batman
    rel = math.fabs(x)
    y = 1.5 * math.sqrt((-math.fabs(rel - 1)) * math.fabs(3 - rel) / ((rel - 1) * (3 - rel))) * (
                1 + math.fabs(rel - 3) / (rel - 3)) * math.sqrt(1 - (x / 7) ** 2) + (
                    4.5 + 0.75 * (math.fabs(x - 0.5) + math.fabs(x + 0.5)) - 2.75 * (
                        math.fabs(x - 0.75) + math.fabs(x + 0.75))) * (1 + math.fabs(1 - rel) / (1 - rel))
    pen.goto(a, y * batman)

for a in range(-3 * batman, -1 * batman - 1, 1):
    x = a / batman
    rel = math.fabs(x)
    y = (2.71052 + 1.5 - 0.5 * rel - 1.35526 * math.sqrt(4 - (rel - 1) ** 2)) * math.sqrt(
        math.fabs(rel - 1) / (rel - 1))
    pen.goto(a, y * batman)

pen.goto(-1 * batman, 3 * batman)
pen.goto(int(-0.5 * batman), int(2.2 * batman))
pen.goto(int(0.5 * batman), int(2.2 * batman))
pen.goto(1 * batman, 3 * batman)
print("Batman Logo with Python Turtle")
for a in range(1 * batman + 1, 3 * batman + 1, 1):
    x = a / batman
    rel = math.fabs(x)
    y = (2.71052 + 1.5 - 0.5 * rel - 1.35526 * math.sqrt(4 - (rel - 1) ** 2)) * math.sqrt(
        math.fabs(rel - 1) / (rel - 1))
    pen.goto(a, y * batman)

for a in range(3 * batman + 1, 7 * batman + 1, 1):
    x = a / batman
    rel = math.fabs(x)
    y = 1.5 * math.sqrt((-math.fabs(rel - 1)) * math.fabs(3 - rel) / ((rel - 1) * (3 - rel))) * (
                1 + math.fabs(rel - 3) / (rel - 3)) * math.sqrt(1 - (x / 7) ** 2) + (
                    4.5 + 0.75 * (math.fabs(x - 0.5) + math.fabs(x + 0.5)) - 2.75 * (
                        math.fabs(x - 0.75) + math.fabs(x + 0.75))) * (1 + math.fabs(1 - rel) / (1 - rel))
    pen.goto(a, y * batman)

for a in range(7 * batman, 4 * batman, -1):
    x = a / batman
    rel = math.fabs(x)
    y = (-3) * math.sqrt(1 - (x / 7) ** 2) * math.sqrt(math.fabs(rel - 4) / (rel - 4))
    pen.goto(a, y * batman)

for a in range(4 * batman, -4 * batman, -1):
    x = a / batman
    rel = math.fabs(x)
    y = math.fabs(x / 2) - 0.0913722 * x ** 2 - 3 + math.sqrt(1 - (math.fabs(rel - 2) - 1) ** 2)
    pen.goto(a, y * batman)

for a in range(-4 * batman - 1, -7 * batman - 1, -1):
    x = a / batman
    rel = math.fabs(x)
    y = (-3) * math.sqrt(1 - (x / 7) ** 2) * math.sqrt(math.fabs(rel - 4) / (rel - 4))
    pen.goto(a, y * batman)

pen.penup()
pen.goto(300, 300)
turtle.done()