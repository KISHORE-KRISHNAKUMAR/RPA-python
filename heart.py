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
   a=color(random.choice(colour))
   pensize(5)
   begin_fill()
   circle(50)
   color(random.choice(colour))
   end_fill()
   return 0

def heart():
   color(random.choice(colour))
   begin_fill()
   pensize(5)
   left(50)
   forward(133)
   circle(50,200)
   right(140)
   circle(50,200)
   forward(133)
   color(random.choice(colour))
   end_fill()
   return 0

print("Tell me your required shape!")
print("1.square.\n2.rectangle.\n3.circle.\n4.heart")
a=int(input("Enter your choice:\n"))
if a==1:
    square()
elif a==2:
    rectangle()
elif a==3:
    circle()
elif a==4:
    heart()
      
