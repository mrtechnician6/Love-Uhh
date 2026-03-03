import turtle
import time

# Configuration for NK Digital Services Quality
WINDOW_TITLE = "Message from Mrtechnician"
HEART_COLOR = "#FF2E63"  # A modern, vibrant pink-red
TEXT_COLOR = "#FFFFFF"
BG_COLOR = "#080808"    # Deep dark mode

def draw_animated_heart():
    # Setup the screen
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    screen.bgcolor(BG_COLOR)
    screen.title(WINDOW_TITLE)
    
    # Setup the pen
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(2)
    t.color(HEART_COLOR)
    t.pensize(5)
    
    # Position the pen
    t.penup()
    t.goto(0, -150)
    t.pendown()
    
    # Start drawing with fill
    t.begin_fill()
    t.fillcolor(HEART_COLOR)
    
    # The Heart Logic (Mathematical Curve)
    t.left(140)
    t.forward(224)
    
    # Left Curve
    for _ in range(200):
        t.right(1)
        t.forward(2)
        
    t.left(120)
    
    # Right Curve
    for _ in range(200):
        t.right(1)
        t.forward(2)
        
    t.forward(224)
    t.end_fill()
    
    # Animation for the text
    time.sleep(0.5)
    t.penup()
    t.goto(0, 50)
    t.color(TEXT_COLOR)
    
    # Professional Typography
    style = ('Verdana', 35, 'bold italic')
    t.write("I Love You", align="center", font=style)
    
    # Subtext for your brand
    t.goto(0, -20)
    t.write("NK Digital Services", align="center", font=('Arial', 12, 'normal'))

    # Keep window open
    screen.mainloop()

if __name__ == "__main__":
    draw_animated_heart()
