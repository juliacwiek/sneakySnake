import turtle
import time
import random

delay = 0.09

# Set up the screen
window = turtle.Screen()
window.title("Snake Game")
window.bgcolor("light blue")
window.setup(width=600, height=500)
window.tracer(0)  # turns off animation

# Snake head
head = turtle.Turtle()
head.speed(0)  # animation speed of turtle module
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)  # sets the head to origin
head.direction = "stop"

# Snake food! :)
food = turtle.Turtle()
food.speed(0)  # animation speed of turtle module
food.shape("circle")
food.color("white")
food.penup()
food.goto(0, 100)  # set food placement

segments = []


# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y_cord = head.ycor()
        head.sety(y_cord + 20)

    elif head.direction == "down":
        y_cord = head.ycor()
        head.sety(y_cord - 20)

    elif head.direction == "left":
        x_cord = head.xcor()
        head.setx(x_cord - 20)

    elif head.direction == "right":
        x_cord = head.xcor()
        head.setx(x_cord + 20)


# Keyboard bindings
# connects keypress with a particular function
window.listen()  # listen for key presses
window.onkeypress(go_up, "Up")
window.onkeypress(go_down, "Down")
window.onkeypress(go_left, "Left")
window.onkeypress(go_right, "Right")

# Main game loop
while True:
    window.update()

    # Check for collision with the border
    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 230 or head.ycor() < -230:
        time.sleep(1)  # pauses game
        head.goto(0, 0)
        head.direction = "stop"

        # Hide segments
        for segment in segments:
            segment.goto(1000, 1000)

        # Clear segments list
        segments.clear()

        # Check for a collision with food
    if head.distance(food) < 20:
        # Move food to random spot on screen
        x = random.randint(-230, 230)
        y = random.randint(-230, 230)
        food.goto(x, y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

    # Move the end segments first in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Check for body collisions
    for segment in segments:
        if segment.distance(head) < 20:  # means there's an overlap
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Hide segments
            for seg in segments:
                seg.goto(1000, 1000)

            segments.clear()

    time.sleep(delay)



