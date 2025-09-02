import turtle
import math

t=turtle.Turtle()
t.speed(0)
t.pensize(2)

def draw_petal(length):
    t.circle(length,60)
    t.left(120)
    t.circle(length,60)
    t.left(60)

circle_colors=["orange","yellow","#FFD500","dark orange","gold"]
petal_colors=["red","white"]

radii=[300,250,200, 150, 100]  
for i,r in enumerate(radii):
    t.penup()
    t.goto(0,-r)
    t.pendown()
    t.fillcolor(circle_colors[i%len(circle_colors)])
    t.begin_fill()
    t.circle(r)
    t.end_fill()

t.penup()
t.goto(0,0)
t.pendown()

for i in range(12):  
    t.fillcolor(petal_colors[i%len(petal_colors)])
    t.begin_fill()
    draw_petal(100)
    t.end_fill()
    t.left(30)

outer_radius=200
inner_radius=150
triangle_count=12  
angle=360/triangle_count
t.penup()
for i in range(triangle_count):
    t.goto(0,0)
    t.setheading(angle*i)  
    t.forward(inner_radius) 
    t.pendown()
    
    t.begin_fill()
    t.color("green")
    
    t.forward(outer_radius-inner_radius) 
    t.left(120)
    t.forward(50)  
    t.left(120)
    t.forward(50)
    t.end_fill()
    
    t.penup()

def move_to(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

def draw_petal(radius,color):
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius,60)
    t.left(120)
    t.circle(radius,60)
    t.end_fill()
    
move_to(0, 0)
t.width(2)
t.color("white")
radius=280  
for i in range(18):  
    angle=i*(360/18)
    x=radius*math.cos(math.radians(angle))
    y=radius*math.sin(math.radians(angle))
    move_to(x,y)
    t.setheading(angle+90)
    for i in range(6):  
        draw_petal(15,"pink")
        t.left(60)
   
t.hideturtle()
turtle.done()



