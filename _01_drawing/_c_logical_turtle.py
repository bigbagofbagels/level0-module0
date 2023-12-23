import random
import turtle


# Returns a random color!
def get_random_color():
    return "#%06X" % (random.randint(0, 0xFFFFFF))

# ====================== DO NOT EDIT THE CODE ABOVE ===========================


def screen_clicked(x, y):
    print('You pressed: x=' + str(x) + ', y=' + str(y))
    
    # 6. Call the turtle .penup() method
    jeffery_bezos.penup()
    # 7. Move the turtle to a new location using .goto(x, y)
    jeffery_bezos.goto(x, y)

def turtle_clicked(x, y):
    print('turtle clicked!')
    
    # 8. Make a for loop to run the next instructions 3 times
    for i in range(3):
        jeffery_bezos.right(360)
        jeffery_bezos.color(get_random_color())

        # 9. Make the turtle spin 360 degrees using the .right() method
        
        # 10. Use the .color() method and getRandomColor() function to change
        # the color of the turtle,
        # myTurtle.color(get_random_color())


if __name__ == '__main__':
    window = turtle.Screen()
    window.setup(width=0.75, height=0.8, startx=0, starty=0)
    
    # 1. Make a new turtle
    jeffery_bezos = turtle.Turtle()
    # 2. Make your turtle's shape 'turtle', .shape('turtle')
    jeffery_bezos.shape('turtle')
    # 3. Set your turtle's color using .color('green') and .pencolor('blue')
    jeffery_bezos.color('green')
    jeffery_bezos.pencolor('blue')
    # 4. Set and new width, length, and outline of our turtle
    jeffery_bezos.turtlesize(stretch_wid=10, stretch_len=10, outline=4)

    # 5. Uncomment the following line and replace 'my_turtle' with your turtle
    jeffery_bezos.onclick(turtle_clicked)


# ===================== DO NOT EDIT THE CODE BELOW ============================
    window.onclick(screen_clicked)
    turtle.done()
