import turtle
import random
import time

# Screen setup
wn = turtle.Screen()
wn.title("Egg Catcher Game")
wn.bgcolor("lightblue")
wn.setup(width=600, height=600)
wn.tracer(0)

# Basket (Player)
basket = turtle.Turtle()
basket.shape("square")
basket.color("brown")
basket.shapesize(stretch_wid=1, stretch_len=5)  # wider rectangle
basket.penup()
basket.goto(0, -250)

# Egg
egg = turtle.Turtle()
egg.shape("circle")
egg.color("white")
egg.penup()
egg.goto(random.randint(-280, 280), 250)

# Score display
pen = turtle.Turtle()
pen.hideturtle()
pen.color("black")
pen.penup()
pen.goto(0, 260)
score = 0
pen.write("Score: 0", align="center", font=("Courier", 24, "normal"))

# Basket movement
def go_left():
    x = basket.xcor()
    if x > -250:
        basket.setx(x - 30)

def go_right():
    x = basket.xcor()
    if x < 250:
        basket.setx(x + 30)

wn.listen()
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

# Main game loop
fall_speed = 0.15
while True:
    wn.update()
    y = egg.ycor()
    egg.sety(y - 10)  # Egg falls down

    # Check if egg caught
    if egg.ycor() < -230 and basket.distance(egg) < 50:
        score += 10
        egg.goto(random.randint(-280, 280), 250)
        pen.clear()
        pen.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

    # Egg missed
    if egg.ycor() < -300:
        pen.clear()
        pen.write("Game Over! Final Score: {}".format(score), align="center", font=("Courier", 24, "normal"))
        time.sleep(2)
        break

    time.sleep(fall_speed)

wn.mainloop()


