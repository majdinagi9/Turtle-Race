import turtle              # 1.  import the modules
import random
from time import sleep

wn = turtle.Screen()
wn.setup(1.0,1.0)       
wn.bgcolor('lightblue')


stamp_size = 20
square_size = 15
finish_line = 250

turtle.color("black")
turtle.shape("square")
turtle.shapesize(square_size / stamp_size)
turtle.penup()

for i in range(10):
   turtle.setpos(finish_line,(180-(i * square_size * 2)))
   turtle.stamp()

for j in range(10):
   turtle.setpos(finish_line +  square_size,((180-  square_size) -(j* square_size* 2)))
   turtle.stamp()

turtle.hideturtle()



turtleOne = turtle.Turtle()   
turtleTwo = turtle.Turtle()
turtleThree = turtle.Turtle()

# turtle.write("START", font = ("Aril",10,"bold"))
turtleOne.color('red')
turtleTwo.color('blue')
turtleThree.color('green')
turtleOne.shape('turtle')
turtleTwo.shape('turtle')
turtleThree.shape('turtle')



turtleTwo.up()                
turtleOne.up()
turtleThree.up()


turtleOne.goto(-190,20)
turtleTwo.goto(-190,-20)
turtleThree.goto(-190,60)


sleep(3)
turtleOne.down()            
turtleTwo.down()  
turtleThree.down()
for turn in range(150):
 turtleOne.forward(random.randint(1,5))
 turtleTwo.forward(random.randint(1,5))
 turtleThree.forward(random.randint(1,5))



#turtleTwo.goto(random.randrange(1,100),20)
# turtleOne.goto(random.randrange(1,100),-20)

# your code goes here

wn.exitonclick()
