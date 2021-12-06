from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "blue", "green", "yellow", "purple", "orange"]
turtle_list = []

for i in range(6):
    t = Turtle(shape="turtle")
    t.penup()
    t.color(colors[i])
    t.goto(x=-230, y=-125+(i*50))
    turtle_list.append(t)


user_choice = screen.textinput(title="Make your bet", prompt="Which turtle do you think will win? Pick a color:")
flag = True
while flag:
    for t in turtle_list:
        rand = random.randint(1, 10)
        t.forward(rand)
        if t.xcor() > 220:
            if user_choice == t.pencolor():
                print(f"You've won!! The winner turtle is {t.pencolor()}")
            else:
                print(f"You've lost!! The winner turtle is {t.pencolor()}")
            flag = False
            break

screen.exitonclick()

