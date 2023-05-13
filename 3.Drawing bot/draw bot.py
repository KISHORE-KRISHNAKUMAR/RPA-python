from turtle import *
import random
colour=["red","blue","black","green","cyan","lightgreen","turquoise","skyblue"]
 
def square():
   color(random.choice(colour))
   begin_fill()
   pensize(5)
   pendown()
   for i in range(4):
        forward(100)
        right(90)
   color(random.choice(colour))
   end_fill()
   return 0

def rectangle():
   color(random.choice(colour))
   begin_fill()
   pensize(5)
   for i in range(2):
      forward(100)
      right(90)
      forward(50)
      right(90)
   color(random.choice(colour))
   end_fill()
   return 0

def circle():
   import turtle
   a=color(random.choice(colour))
   pensize(5)
   begin_fill()
   turtle.circle(50)
   color(random.choice(colour))
   end_fill()
   return 0

def heart():
    import turtle
    turtle.color(random.choice(colour))
    turtle.begin_fill()
    turtle.pensize(5)
    turtle.left(50)
    turtle.forward(133)
    turtle.circle(50,200)
    turtle.right(140)
    turtle.circle(50,200)
    turtle.forward(133)
    turtle.color(random.choice(colour))
    turtle.end_fill()
    return 0
def triangle():
   color(random.choice(colour))
   begin_fill()
   pensize(5)
   fd(200)
   lt(120)
   fd(200)
   lt(120)
   fd(200)
   color(random.choice(colour))
   end_fill()
   return 0
def smile():
     import turtle
     turtle.penup()
     turtle.goto(0, -100)
     turtle.pendown()
     turtle.color("yellow")
     turtle.begin_fill()
     turtle.circle(100)
     turtle.end_fill()
     turtle.penup()
     turtle.goto(-50, 0)
     turtle.pendown()
     turtle.color("black")
     turtle.begin_fill()
     turtle.circle(15)
     turtle.end_fill()
     turtle.penup()
     turtle.goto(50, 0)
     turtle.pendown()
     turtle.begin_fill()
     turtle.circle(15)
     turtle.end_fill()
    #the mouth
     turtle.penup()
     turtle.goto(-50,-30)
     turtle.pendown()
     turtle.pensize(5)
     turtle.setheading(270)
     turtle.circle(50, 180)
     return 0
while True:
     print("Tell me your required shape!")
     #print("1.Square.\n2.Rectangle.\n3.Circle.\n4.Heart.\n5.Triangle.\n6.Smile")
     a=str(input("Enter your choice:\n"))
     if a=="square":
         square()
     elif a=='rectangle':
         rectangle()
     elif a=='circle':
          circle()
     elif a=='heart':
          heart()
     elif a=='triangle':
          triangle()
     elif a== 'smile':
          smile()
     print("Do you want to continue?")
     b=str(input("Enter your choice:y or n \n"))
     if (b!='y'):
          print("************************************Thank You*********************************")
          break
    

