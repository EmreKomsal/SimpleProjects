from turtle import Screen, Turtle
import random

class Snake:
    def __init__(self, screen_width = 600, screen_height = 600):
        self.segments = []
        self.create_snake()
        self.screen_width = screen_width
        self.screen_height = screen_height
        
    def create_snake(self):
        starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        for position in starting_positions:
            new_segment = Turtle("square")
            if len(self.segments) % 2 == 0:
                new_segment.color("white")
            else:
                new_segment.color("gray")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)
            
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(20)
        
    def up(self):
        self.segments[0].setheading(90)
        
    def down(self):
        self.segments[0].setheading(270)
        
    def left(self):
        self.segments[0].setheading(180)
        
    def right(self):
        self.segments[0].setheading(0)
        
    def add_segment(self):
        new_segment = Turtle("square")
        if len(self.segments) % 2 == 0:
            new_segment.color("white")
        else:
            new_segment.color("gray")
        new_segment.penup()
        new_segment.goto(self.segments[-1].position())
        self.segments.append(new_segment)
        
    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        
    def check_screen_collision(self):
        if self.segments[0].xcor() > self.screen_width/2 - 20 or self.segments[0].xcor() < -self.screen_width/2 - 20 or self.segments[0].ycor() > self.screen_height/2 - 20 or self.segments[0].ycor() < -self.screen_height/2 - 20:
            return True
        return False 
    
    def check_collision(self):
        for seg in self.segments[1:]:
            if self.segments[0].distance(seg) < 10:
                return True
        return False
    
    def check_food_collision(self, food):
        if self.segments[0].distance(food) < 20:
            return True
        return False

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color("red")
        self.speed("fastest")
        self.refresh()
        
        
    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)