/* Task 1 */
import turtle

boss = turtle.Turtle()

def square():
    for i in range(4):
        turtle.forward(100)
        turtle.left(90)


def triangle():
    for i in range(3):
        turtle.forward(100)
        turtle.left(120)


def pentagon():
    for i in range(5):
        turtle.forward(100)
        turtle.left(72)


def hexagon():
    for i in range(6):
        turtle.forward(100)
        turtle.left(60)


def nonagon():
    for i in range(9):
        turtle.forward(100)
        turtle.left(40)


def decagon():
    for i in range(10):
        turtle.forward(100)
        turtle.left(36)


def circle():
    turtle.circle(50)
circle()


n = int(input())
def AnyRegPoly(n):
    for i in range(n):
        turtle.forward(100)
        turtle.left(360/n)
    return(i)



/* Task 2 */
import turtle
cam = turtle.Turtle('turtle')

anyturtle = cam
window = turtle.Screen()
window.colormode(255)
window.bgcolor(0, 0, 0)

def DrawSquare():
    cam.begin_fill()
    for i in range(2):
        cam.speed(1)
        cam.color(0, 0, 255)
        cam.left(90)
        cam.forward(100)
        cam.color(255, 0, 0)
        cam.left(90)
        cam.forward(100)
    cam.end_fill()
DrawSquare()



/* Task 3 */
def sharecorner():
    import turtle

    turtle.reset()
    turtle.hideturtle()

    turtle.shape("square")
    turtle.fillcolor("white")

    for side in range(200, 0, -20):
        turtle.shapesize(side / 20)
        turtle.stamp()
        x, y = turtle.position()
        turtle.goto(x - 10, y + 10)

    turtle.exitonclick()


def concentricsquares():
    import turtle
    def draw_square(t, size):
       for i in range(4):
           t.forward(size)
           t.left(90)
    wn = turtle.Screen()
    cam = turtle.Turtle()
    sizevar = 1
    for i in range(10):
       draw_square(cam, sizevar)
       sizevar += 20
       cam.penup()
       cam.backward(10)
       cam.right(90)
       cam.forward(10)
       cam.left(90)
       cam.pendown()



/* Task 3(revised) */
def sharecorner():
    import turtle

    turtle.reset()
    turtle.hideturtle()

    turtle.shape("square")
    turtle.fillcolor("white")

    for side in range(200, 0, -20):
        turtle.shapesize(side / 20)
        turtle.stamp()
        x, y = turtle.position()
        turtle.goto(x - 10, y + 10)

    turtle.exitonclick()
sharecorner()



/* Task 4 */
import turtle

cameron = turtle.Turtle()

r = (0, 255)
g = (0, 255)
b = (0, 255)
colormode(255)
pencolor(r, g, b)

def DrawSquare(anyturtle, n):
    for i in range (4):
        anyturtle.speed(0)
        anyturtle.forward(n)
        anyturtle.right(90)

DrawSquare(cameron, 100)
        
