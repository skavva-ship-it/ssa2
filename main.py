
import turtle
import random

# setting up the turtle and making variables

ranx = random.randint(-260, 260)
rany = random.randint(-260, 260)
screen = turtle.Screen()

screen.bgcolor("Light Blue")

###shapes = []

# this turtle is a triangle
ranx4 = random.randint(-260, 260)
rany4 = random.randint(-260, 260)
triangle1 = turtle.Turtle()
triangle1.speed(0)
triangle1.shape("triangle")
triangle1.color("green")
triangle1.penup()
triangle1.goto(ranx4, rany4)
triangle1.pendown()

###shapes.append(triangle)

# this turtle is a triangle
ranx5 = random.randint(-260, 260)
rany5 = random.randint(-260, 260)
triangle2 = turtle.Turtle()
triangle2.speed(0)
triangle2.shape("triangle")
triangle2.color("green")
triangle2.penup()
triangle2.goto(ranx5, rany5)
triangle2.pendown()

###shapes.append(triangle)

# this turtle is a triangle
ranx6 = random.randint(-260, 260)
rany6 = random.randint(-260, 260)
triangle3 = turtle.Turtle()
triangle3.speed(0)
triangle3.shape("triangle")
triangle3.color("green")
triangle3.penup()
triangle3.goto(ranx4, rany4)
triangle3.pendown()

###shapes.append(triangle)

# this turtle is a square
ranx1 = random.randint(-260, 260)
rany1 = random.randint(-260, 260)
square1 = turtle.Turtle()
square1.speed(0)
square1.shape("square")
square1.color("blue")
square1.penup()
square1.goto(ranx1, rany1)
square1.pendown()

###shapes.append(square)

# this turtle is a square
ranx7 = random.randint(-260, 260)
rany7 = random.randint(-260, 260)
square2 = turtle.Turtle()
square2.speed(0)
square2.shape("square")
square2.color("blue")
square2.penup()
square2.goto(ranx7, rany7)
square2.pendown()

###shapes.append(square)

# this turtle is a square
ranx8 = random.randint(-260, 260)
rany8 = random.randint(-260, 260)
square3 = turtle.Turtle()
square3.speed(0)
square3.shape("square")
square3.color("blue")
square3.penup()
square3.goto(ranx8, rany8)
square3.pendown()

###shapes.append(square)

# this turtle is a circle
ranx10 = random.randint(-260, 260)
rany10 = random.randint(-260, 260)
circle1 = turtle.Turtle()
circle1.speed(0)
circle1.shape("circle")
circle1.color("red")
circle1.penup()
circle1.goto(ranx10, rany10)
circle1.pendown()

###shapes.append(circle)

# this turtle is a circle
ranx11 = random.randint(-260, 260)
rany11 = random.randint(-260, 260)
circle2 = turtle.Turtle()
circle2.speed(0)
circle2.shape("circle")
circle2.color("red")
circle2.penup()
circle2.goto(ranx11, rany11)
circle2.pendown()

###shapes.append(circle)

# this turtle is a circle
ranx12 = random.randint(-260, 260)
rany12 = random.randint(-260, 260)
circle3 = turtle.Turtle()
circle3.speed(0)
circle3.shape("circle")
circle3.color("red")
circle3.penup()
circle3.goto(ranx12, rany12)
circle3.pendown()


###shapes.append(circle)

# this code will move the turtle
def right10():
    sam.right(10)


screen.onkey(right10, "Right")


def left10():
    sam.left(10)


screen.onkey(left10, "Left")

screen.listen()

# these funtions will help sam move to score more points


screen.listen()

sam = turtle.Turtle()
sam.penup()
sam.speed(1)
sam.shape("turtle")

# while True:
# for shape in shapes:
#  randomplacex = random.randint(-250, 250)
# randomplacey = random.randint(-250, 250)
# sam.forward(10)
# if abs(sam.xcor() - shape.xcor()) < 10 and abs(sam.ycor() - shape.ycor()) < 10:
# shape.penup()
# shape.goto(randomplacex, randomplacey)

s = turtle.Turtle()
s.penup()
s.goto(-250, 0)
score = 0

while score < 11:
    sam.forward(10)
    randomplacex = random.randint(-250, 250)
    randomplacey = random.randint(-250, 250)
    sam.forward(10)
    if sam.xcor() > 260 or sam.xcor() < -260 or sam.ycor() > 200 or sam.ycor() < -200:
        sam.speed(0)
        sam.right(180)
        sam.speed(1)
        sam.forward(10)
    if abs(sam.xcor() - triangle1.xcor()) < 10 and abs(sam.ycor() - triangle1.ycor()) < 10:
        triangle1.penup()
        triangle1.goto(randomplacex, randomplacey)
        score += 1
    if abs(sam.xcor() - triangle2.xcor()) < 10 and abs(sam.ycor() - triangle2.ycor()) < 10:
        triangle2.penup()
        triangle2.goto(randomplacex, randomplacey)
        score += 1
    if abs(sam.xcor() - triangle3.xcor()) < 10 and abs(sam.ycor() - triangle3.ycor()) < 10:
        triangle3.penup()
        triangle3.goto(randomplacex, randomplacey)
        score += 1
    if abs(sam.xcor() - square1.xcor()) < 10 and abs(sam.ycor() - square1.ycor()) < 10:
        square1.penup()
        square1.goto(randomplacex, randomplacey)
        score += 1
    if abs(sam.xcor() - square2.xcor()) < 10 and abs(sam.ycor() - square2.ycor()) < 10:
        square2.penup()
        square2.goto(randomplacex, randomplacey)
        score += 1
    if abs(sam.xcor() - square3.xcor()) < 10 and abs(sam.ycor() - square3.ycor()) < 10:
        square3.penup()
        square3.goto(randomplacex, randomplacey)
        score += 1
    if abs(sam.xcor() - circle1.xcor()) < 10 and abs(sam.ycor() - circle1.ycor()) < 10:
        circle1.penup()
        circle1.goto(randomplacex, randomplacey)
        score += 1
    if abs(sam.xcor() - circle2.xcor()) < 10 and abs(sam.ycor() - circle2.ycor()) < 10:
        circle3.penup()
        circle3.goto(randomplacex, randomplacey)
        score += 1
    if abs(sam.xcor() - circle3.xcor()) < 10 and abs(sam.ycor() - circle3.ycor()) < 10:
        circle3.penup()
        circle3.goto(randomplacex, randomplacey)
        score += 1
    s.clear()
    s.write("score:" + str(score))






