from turtle import *

# create and style a screen
screen = Screen()
screen.title("Turtle Sketch")
screen.bgcolor("#ffeafb")
screen.setup(1000,600)

# create an artist turtle to draw
artist = Turtle()
artist.shape("turtle")
artist.pensize(3)
artist.color("#0c4196")
artist.speed(0)

def go_down():
	artist.setheading(270)
	artist.forward(10)
	
def go_up():
	artist.setheading(90)
	artist.forward(10)

def go_right():
	artist.setheading(0)
	artist.forward(10)

def go_left():
	artist.setheading(180)
	artist.forward(10)

def draw_star(xcoord,ycoord):
	for x in range(5):
		artist.forward(50)
		artist.left(144)

def draw_star():
	for x in range(5):
		artist.forward(50)
		artist.left(144)

screen.onkeypress(go_down,"Down")
screen.onkeypress(go_up,"Up")
screen.onkeypress(go_left,"Left")
screen.onkeypress(go_right,"Right")
screen.onclick(draw_star)

screen.listen()

mainloop()