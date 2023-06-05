from turtle import Turtle, Screen
import random



tortoise = Turtle()
screen = Screen()


colours = ["red", "yellow", "blue", "green", "pink"]

directions = [0,90, 180, 270]
tortoise.pensize(20)
tortoise.speed("fastest")

for _ in range(200):
    tortoise.color(random.choice(colours))
    tortoise.forward(20)
    tortoise.setheading(random.choice(directions))

screen.exitonclick()