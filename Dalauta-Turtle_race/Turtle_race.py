Frank Dalauta
from turtle import *
from random import *
import tkinter as tk
import turtle
# Function to start the turtle race
def start_race():
    while blue_turtle.xcor() <= 230 and pink_turtle.xcor() <= 230:
        blue_turtle.forward(randint(1, 10))
        pink_turtle.forward(randint(1, 10))
        yellow_turtle.forward(randint(1, 10))
        green_turtle.forward(randint(1, 10))

    # Determine the winner and display a message
    if blue_turtle.xcor() > pink_turtle.xcor() and blue_turtle.xcor() > yellow_turtle.xcor() and blue_turtle.xcor() > green_turtle.xcor():
        print("Blue turtle wins!")
        for _ in range(72):
            blue_turtle.right(5)
            blue_turtle.shapesize(1.5)
    elif pink_turtle.xcor() > blue_turtle.xcor() and pink_turtle.xcor() > yellow_turtle.xcor() and pink_turtle.xcor() > green_turtle.xcor():
        print("Pink turtle wins!")
        for _ in range(72):
            pink_turtle.right(5)
            pink_turtle.shapesize(1.5)
    elif yellow_turtle.xcor() > blue_turtle.xcor() and yellow_turtle.xcor() > pink_turtle.xcor() and yellow_turtle.xcor() > green_turtle.xcor():
        print("Yellow turtle wins!")
        for _ in range(72):
            yellow_turtle.right(5)
            yellow_turtle.shapesize(1.5)
    else:
        print("Green turtle wins!")
        for _ in range(72):
            green_turtle.right(5)
            green_turtle.shapesize(1.5)

    # Reset turtle positions
    reset_turtles()
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        turtle.bye()

# Function to reset turtle positions
def reset_turtles():
    blue_turtle.goto(-300, 150)
    pink_turtle.goto(-300, 50)
    yellow_turtle.goto(-300, -50)
    green_turtle.goto(-300, -150)

# Create the start button function
def start_button_click():
      # Destroy the button after clicking
    start_race()  # Call the start_race function to begin the race

# Set up the turtle race window
setup(800, 500) 
title(" TURTLE RACE")
bgcolor("forestgreen")
speed(100)

penup()
goto(-100, 205)
color("white")
write("TURTLE RACE", font=("Arial", 20,"bold"))

goto(-350,200)
pendown()
color("chocolate")
begin_fill()
for i in range(2):
    forward(700)
    right(90)
    forward(400)
    right(90)
end_fill()

gap_size = 20
shape("square")
penup()

color("white")
for i in range(10):
    goto(250,(170 -(i * gap_size * 2 )))
    stamp()

for i in range(10):
    goto(250 + gap_size,((210 - gap_size)-(i * gap_size * 2 )))
    stamp()

color("black")
for i in range(10):
    goto(250, (190 -(i * gap_size * 2)))
    stamp()


for i in range(10):
    goto(251 + gap_size, ((190 - gap_size )-(i * gap_size * 2)))
    stamp()

# Create the start button
start_button = tk.Button(text="Start Race", command=start_button_click)
start_button.pack()

blue_turtle = Turtle()
blue_turtle.color("cyan")
blue_turtle.shape("turtle")
blue_turtle.shapesize(1.5)
blue_turtle.penup()
blue_turtle.goto(-300, 150)
blue_turtle.pendown()

pink_turtle = Turtle()
pink_turtle.color("magenta")
pink_turtle.shape("turtle")
pink_turtle.shapesize(1.5)
pink_turtle.penup()
pink_turtle.goto(-300, 50)
pink_turtle.pendown()

yellow_turtle = Turtle()
yellow_turtle.color("yellow")
yellow_turtle.shape("turtle")
yellow_turtle.shapesize(1.5)
yellow_turtle.penup()
yellow_turtle.goto(-300, -50)
yellow_turtle.pendown()

green_turtle = Turtle()
green_turtle.color("green")
green_turtle.shape("turtle")
green_turtle.shapesize(1.5)
green_turtle.penup()
green_turtle.goto(-300, -150)
green_turtle.pendown()

pink_turtle.penup()
blue_turtle.penup()
green_turtle.penup()
yellow_turtle.penup()

turtle.done()
turtle.Screen()
exitonclick(