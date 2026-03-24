import turtle

screen = turtle.Screen()
canvas = screen.getcanvas()

# Wymuszenie focusu na macOS
root = canvas.winfo_toplevel()
root.attributes("-topmost", True)
root.update()
root.attributes("-topmost", False)


turtle.setup(width=800, height=800)


a=0
b=0

turtle.bgcolor("black")
turtle.speed(0)
turtle.pencolor("green")
turtle.penup()
turtle.goto(0, 200)
turtle.pendown()

while True:
    turtle.forward(a)
    turtle.right(b)
    a += 3
    b += 1
    if b == 200:
        break

turtle.exitonclick()

