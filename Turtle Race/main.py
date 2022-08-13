from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=900, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? (Red, Green, Orange, "
                                                          "Yellow, Blue, Purple, Pink, Black) Enter the color: ")
color = ["red", "orange", "yellow", "green", "blue", "purple", "black", "pink"]
y_positions = [-100, -70, -40, -10, 20, 50, 80, 110]
all_turtle = []

for turtle_index in range(0, 7):
    new_turtle = Turtle("turtle")
    new_turtle.color(color[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-440, y_positions[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 420:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
