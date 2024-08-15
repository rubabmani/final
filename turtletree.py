import turtle
wing= turtle. Turtle()
wing.screen.bgcolor("black")
wing.pensize(2)
wing.color("green")
wing.left(90)

wing.backward(80)
wing.speed(10000)
wing.shape("turtle")

def tree(i):
    if i<10:
        return
    else:
        wing.forward(i)
        wing.color("orange")
        wing.circle(2)
        wing.color("brown")
        wing.left(30)
        tree(3*i/4)
        wing.right(60)
        tree(3*i/4)
        wing.left(30)
        wing.backward(i)
        
tree(80) 
turtle.done()       