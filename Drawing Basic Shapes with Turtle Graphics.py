print("Hi! I can draw a  rectangle, ellipse, square, circle, point, and line.") 
shape = input("Enter the shape you want me to draw: ")

import turtle
#The function Screen() returns a singleton object of a TurtleScreen subclass.
wn = turtle.Screen()
#Python Turtle Graphics window on top
rootwindow = wn.getcanvas().winfo_toplevel()
rootwindow.call('wm', 'attributes', '.', '-topmost', '1')
rootwindow.call('wm', 'attributes', '.', '-topmost', '0')

if (shape.upper() == 'RECTANGLE'):
    #Set or return background color of the TurtleScreen
    turtle.bgcolor("#B8FF70")

    #Return or set the pencolor.
    turtle.pencolor("#4C9600")
   
    #Return or set the fillcolor.
    turtle.fillcolor("#D2FFA4")

    #To be called just before drawing a shape to be filled.
    turtle.begin_fill()

    #Set or return the line thickness
    turtle.pensize(10)

    #Using a for loop, we moved the turtle forward(140), left(90), forward(70), and left(90) and execute it twice.
    for rectangle in range(2):
        turtle.forward(140) 
        turtle.left(90) 
        turtle.forward(70) 
        turtle.left(90)   

    #Fill the shape drawn after the last call to begin_fill()
    turtle.end_fill()

    #To hide turtle arrow
    turtle.hideturtle() 


elif (shape.upper() == 'ELLIPSE'):
    turtle.bgcolor("#FFF770")
    turtle.pencolor("#A79E00")
    turtle.fillcolor("#FFFAA4")
    turtle.begin_fill()
    turtle.pensize(10)

    #divide the ellipse into four arcs
    #define a method to form these arcs in pair
    def ellipse(radius):
        
        #radius of arc
        for i in range(2):
            #two pairs of arcs
            turtle.circle(radius,90)
            turtle.circle(radius/2,90)
     
    #turn turtle right at a 45 degree angle
    turtle.right(45)

    #call the function
    ellipse(120)

    turtle.end_fill()
    turtle.hideturtle() 

    
elif (shape.upper() == 'SQUARE'):
    turtle.bgcolor("#76D6FF")
    turtle.pencolor("#004969")
    turtle.fillcolor("#A8E5FF")
    turtle.begin_fill()
    turtle.pensize(10)

    #Using a for loop, we moved the turtle forward(150) and left(90) and execute it four times.
    for square in range(4):
        turtle.forward(150) 
        turtle.left(90) 
    turtle.end_fill()
    turtle.hideturtle()


elif (shape.upper() == 'CIRCLE'):
    turtle.bgcolor("#FF9570")
    turtle.pencolor("#A72B00")
    turtle.fillcolor("#FFBBA4")
    turtle.begin_fill()
    turtle.pensize(8)

    #The number we have passed in the circle() function is radius of the circle. 
    turtle.circle(80)

    turtle.end_fill()
    turtle.hideturtle()


elif (shape.upper() == 'POINT'): 
    turtle.bgcolor("#FCEDDA")
    turtle.pencolor("#050505")

    #The number we have passed in the dot() function is diameter of the dot. 
    turtle.dot(10) 

    turtle.hideturtle() 


elif (shape.upper() == 'LINE'): 
    turtle.bgcolor("#FFA4B2")
    turtle.pencolor("#9E0019")
    turtle.pensize(5)

    #Moving the turtle forward by 200 units
    turtle.forward(200)

    turtle.hideturtle() 

else:
    print("This shape is not among the available options.")

wn.exitonclick()



