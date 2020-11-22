import turtle              
import random
from time import sleep

window = turtle.Screen()
window.setup(1.0,1.0)       
window.bgcolor('gray')


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

start = turtle.Turtle()
start.penup()
start.hideturtle()
start.goto(0, -200)
start.write("3", font=("Arial", 24, "italic"), align="center")
sleep(1)
start.clear()
start.write("2", font=("Arial", 24, "italic"), align="center")
sleep(1)
start.clear()
start.write("1", font=("Arial", 24, "italic"), align="center")
sleep(1)
start.clear()
start.write("START", font=("Arial", 24, "italic"), align="center")
sleep(1)
start.clear()


turtleOne.down()            
turtleTwo.down()  
turtleThree.down()
for turn in range(150):
 turtleOne.forward(random.randint(1,5))
 turtleTwo.forward(random.randint(1,5))
 turtleThree.forward(random.randint(1,5))


if(turtleOne.xcor()>250):
 turtle.goto(0, -200)
 turtle.color("red")
 turtle.write("Red Turtle Won", font=("Arial", 24, "italic"),align="center") 
elif(turtleTwo.xcor()>250):
 turtle.goto(0, -200)
 turtle.color("blue")
 turtle.write("Blue Turtle Won", font=("Arial", 24, "italic"),align="center")
else:
  turtle.goto(0, -200)
  turtle.color("green")
  turtle.write("Green Turtle Won",font=("Arial", 24, "italic"), align="center")


window.exitonclick()
