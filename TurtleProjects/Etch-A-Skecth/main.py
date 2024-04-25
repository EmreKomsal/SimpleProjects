from turtle import Turtle, Screen

tim = Turtle()

def move_forward():
    global tim
    tim.forward(10)
    
def move_backward():
    global tim
    tim.backward(10)
    
def turn_left():
    global tim
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)
    
def turn_right():
    global tim
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)
    
def clear():
    global tim
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
    
def draw_circle():
    global tim
    tim.circle(100)
    
def draw_square():
    global tim
    for _ in range(4):
        tim.forward(100)
        tim.right(90)
        
def draw_car():
    global tim
    tim.penup()
    tim.goto(-100, -20)
    tim.pendown()
    tim.begin_fill()
    tim.color("blue")
    
    # Draw the main body of the car
    for _ in range(2):
        tim.forward(200)
        tim.left(90)
        tim.forward(40)
        tim.left(90)
    tim.end_fill()
    
    # Draw the roof of the car
    tim.penup()
    tim.goto(-60, 20)
    tim.pendown()
    tim.begin_fill()
    for _ in range(2):
        tim.forward(120)
        tim.left(90)
        tim.forward(40)
        tim.left(90)
    tim.end_fill()
    
    # Draw the wheels
    tim.penup()
    tim.goto(-60, -40)
    tim.pendown()
    tim.color("black")
    tim.begin_fill()
    tim.circle(20)
    tim.end_fill()
    
    tim.penup()
    tim.goto(40, -40)
    tim.pendown()
    tim.begin_fill()
    tim.circle(20)
    tim.end_fill()
    
def pen():
    global tim
    if tim.isdown():
        tim.penup()
    else:
        tim.pendown()
    
def main():
    screen = Screen()

    screen.listen()
    
    screen.onkey(key="w", fun=move_forward)
    screen.onkey(key="s", fun=move_backward)
    screen.onkey(key="a", fun=turn_left)
    screen.onkey(key="d", fun=turn_right)
    screen.onkey(key="c", fun=clear)
    screen.onkey(key="o", fun=draw_circle)
    screen.onkey(key="q", fun=draw_square)
    screen.onkey(key="e", fun=draw_car)
    screen.onkey(key="p", fun=pen)
    
    screen.exitonclick()
    
if __name__ == "__main__":
    main()