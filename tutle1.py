import turtle



wn = turtle.Screen()
wn.bgcolor("lightblue")

wn.title("Hello. Tess!")


t=turtle.Turtle()

turtle.position()
turtle.forward(150)

turtle.left(90)
turtle.forward(90)


t1 = turtle.Turtle()

for i in range(4):
    t1.forward(100)
    t1.left(90)

for i in range(30, 600, 30):
    t1.forward(i)
    t1.left(90)


turtle.done()

print("Hello we're going to push this message")