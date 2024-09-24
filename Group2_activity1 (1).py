"""
Hello Professor,
Here is our assignment 1 done by four members:
Maham Mustafa 
Arina Baiazitova
Maaz Shaikh
Mohammed al salaam
Hope you like it!
"""

import turtle
turtle.speed(100) #making this speed fast

c_1=input("enter the color of layer 1: ")
c_2=input("enter the color of layer 2: ")
c_3=input("enter the color of layer 3: ")
c_t=input("enter the color of the table: ")


"""
Making the function for the first layer of the cake.
It consists of 4 parameters for the position, radius and color.
"""
 
def cake_layer_1(x,y,radius):
    turtle.penup() 
    turtle.goto(x,y)
    turtle.pendown()
    turtle.pencolor(c_1)
    turtle.fillcolor(c_1)
    turtle.begin_fill()
    turtle.forward(300)
    turtle.circle(radius,180)
    turtle.right(180)
    turtle.circle(radius,180)
    turtle.right(180)
    turtle.circle(radius,180)
    turtle.right(180)
    turtle.circle(radius,180)
    turtle.right(180)
    turtle.circle(radius,180)
    turtle.forward(300)
    turtle.circle(radius,180)
    turtle.left(180)
    turtle.circle(radius,180)
    turtle.left(180)
    turtle.circle(radius,180)
    turtle.left(180)
    turtle.circle(radius,180)
    turtle.left(180)
    turtle.circle(radius,180)
    turtle.end_fill()


"""
Making the function for the second layer of the cake
"""


def cake_layer_2(x,y,radius):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.pencolor(c_2)
    turtle.fillcolor(c_2)
    turtle.begin_fill()
    turtle.forward(240)
    turtle.circle(radius,180)
    turtle.right(180)
    turtle.circle(radius,180)
    turtle.right(180)
    turtle.circle(radius,180)
    turtle.right(180)
    turtle.circle(radius,180)
    turtle.forward(240)
    turtle.circle(radius,180)
    turtle.left(180)
    turtle.circle(radius,180)
    turtle.left(180)
    turtle.circle(radius,180)
    turtle.left(180)
    turtle.circle(radius,180)
    turtle.left(180)
    turtle.end_fill()


"""
Making the function for the third layer of the cake
"""


def cake_layer_3(x,y,radius):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.pencolor(c_3)
    turtle.fillcolor(c_3)
    turtle.begin_fill()
    turtle.forward(180)
    turtle.circle(radius,180)
    turtle.right(180)
    turtle.circle(radius,180)
    turtle.right(180)
    turtle.circle(radius,180)
    turtle.forward(180)
    turtle.circle(radius,180)
    turtle.left(180)
    turtle.circle(radius,180)
    turtle.left(180)
    turtle.circle(radius,180)
    turtle.left(180)
    turtle.end_fill()

"""
Making the function for the table
"""

def table(x,y,radius):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.pencolor(c_t)
    turtle.fillcolor(c_t)
    turtle.begin_fill()
    turtle.forward(400)
    turtle.circle(radius,180)
    turtle.forward(400)
    turtle.circle(radius,180)
    turtle.end_fill()

"""
Making 4 functions for the legs of the table
"""

def leg_1(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.fillcolor(c_t)
    turtle.begin_fill()
    turtle.right(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(100)
    turtle.end_fill()

def leg_2(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.fillcolor(c_t)
    turtle.begin_fill()
    turtle.right(180)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(100)
    turtle.end_fill()   

def leg_3(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.fillcolor(c_t)
    turtle.begin_fill()
    turtle.right(180)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(100)
    turtle.end_fill()

def leg_4(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.fillcolor(c_t)
    turtle.begin_fill()
    turtle.right(180)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(100)
    turtle.end_fill()

"""
Making the function for the candle
"""
def candle(x, y, height, color):
    #candle
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.pensize(1)
    turtle.pencolor(color)
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.setheading(90)  
    turtle.forward(height) 
    turtle.right(90)       
    turtle.forward(10)    
    turtle.right(90)       
    turtle.forward(height) 
    turtle.right(90)       
    turtle.forward(10)    
    turtle.end_fill()
    
    # the flame
    turtle.penup()
    turtle.goto(x + 5, y + height + 8) 
    turtle.pendown()
    turtle.fillcolor("yellow")
    turtle.begin_fill()
    turtle.circle(5)
    turtle.end_fill()

def balloon_1(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.forward(80)
    turtle.left(90)
    turtle.pendown()
    turtle.forward(80)
    turtle.right(90)
    turtle.fillcolor("red")
    turtle.begin_fill()
    turtle.circle(30)
    turtle.end_fill()

def balloon_2(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.forward(160)
    turtle.left(90)
    turtle.pendown()
    turtle.forward(160)
    turtle.right(90)
    turtle.fillcolor("red")
    turtle.begin_fill()
    turtle.circle(30)
    turtle.end_fill()


"""
This function is for the name
"""

def d(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.pensize(5)
    turtle.pencolor("black")
    turtle.right(90)
    turtle.circle(30,180)
    turtle.left(90)
    turtle.forward(60)
def a(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.left(160)
    turtle.forward(60)
    turtle.right(140)
    turtle.forward(60)
    turtle.penup()
    turtle.goto(-100,-70)
    turtle.pendown()
    turtle.left(70)
    turtle.forward(25)

def n(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(60)
    turtle.right(150)
    turtle.forward(70)
    turtle.left(150)
    turtle.forward(60)

def i(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.forward(60)
    turtle.right(90)
    turtle.forward(30)
    turtle.left(180)
    turtle.forward(60)
    turtle.right(180)
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(60)
    turtle.right(90)
    turtle.forward(30)
    turtle.left(180)
    turtle.forward(60)    

def l(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.right(180)
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(60)

def o(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.circle(30) 





"""
the dimentions with the color
"""


cake_layer_1(-150,-100,10)
cake_layer_2(-120,0,10,)
cake_layer_3(90,140,10)
table(-200,-120,10)
leg_1(-200,-120)
leg_2(-150,-120)
leg_3(140,-120)
leg_4(190,-120)
d(-140,-90)
a(-110,-90)
n(-60,-90)
i(10,-90)
l(80,-90)
o(145,-60)

candle(-40, 140, 30, "red")   # First candle
candle(20, 140, 30, "red")  # Second candle

turtle.penup()
turtle.goto(0, 150)  # Position in the middle of the cake
turtle.pendown()
turtle.fillcolor("blue")
turtle.begin_fill()
turtle.circle(5)  # blueberry
turtle.end_fill()

balloon_1(300,280)
balloon_2(-100,350)
input("stop")