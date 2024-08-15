import turtle as t

# Define a list of valid color names
colors = ["red", "violet", "green", "blue", "yellow", "orange", "purple"]

t.speed(0)
t.bgcolor("black")
t.penup()
#t.goto(-200, 200)
t.pendown()


for i in range(260):
    t.pencolor(colors[i % 7])  # Cycle through the colors list
    t.width(i // 100 + 1)
    t.forward(i)
    t.left(59)

t.done()
