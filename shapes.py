import turtle
import math
#------------------------------------------------------------------------------
# Starter code to get things going
# (feel free to delete once you've written your own functions
#------------------------------------------------------------------------------

# Create the world, and a turtle to put in it
bob = turtle.Turtle()

# Get moving, turtle!
bob.fd(100)

# Wait for the user to close the window
turtle.mainloop()


#------------------------------------------------------------------------------
# Make some shapes
#   Work through exercises 1-4 in Chapter 4.3.
#------------------------------------------------------------------------------

# NOTE: for part 2 of 4.3, you will add another parameter to this function
def square(t, length):
    """
    Draw a square using Turtle t

    >>> don = turtle.Turtle()
    >>> square(don)
    """
    for i in range(4):
        t.fd(length)
        t.lt(90)

## Polygon
def polygon(t,length,number_of_sides):
    angle = 360/number_of_sides
    for i in range(number_of_sides):
        t.fd(length)
        t.lt(angle)

def circle = (t,r):
    circum = 2*math.pi*r
    n = 360
    length = circum/360
    polygon(t,length,n)

## Circle


#------------------------------------------------------------------------------
# Make some art
#   Complete *at least one of* Exercise 2, 3, 4, or 5 in `shapes.py`.
#------------------------------------------------------------------------------

def polypie(t, n, r):
    """Draws a pie

    t: Turtle
    n: number of segments
    r: length of the radial spokes
    """
    angle = 360.0 / n
    for i in range(n):
        isosceles(t, r, angle/2)
        t.lt(angle)


def triangle(t, length_of_equal_sides, diff_angle):

    angle = diff_angle/2

    t.rt(angle)
    t.fd(r)
    t.lt(90+angle)
    t.fd(2*r * math.sin(angle * math.pi / 180))
    t.lt(90+angle)
    t.fd(r)
    t.lt(180-angle)

# If you come up with some cool drawings you'd like to share with the rest of the class, let us know!
