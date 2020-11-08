# In Robert McCloskey’s book Make Way for Ducklings, the names of the ducklings are Jack, Kack, Lack, Mack, Nack, Ouack, Pack, and Quack. This loop tries to output these names in order.
# Of course, that’s not quite right because Ouack and Quack are misspelled. Can you fix it?

prefixes = "JKLMNOPQ"
suffix = "ack"

for p in prefixes:
    print(p + suffix)


# Get the user to enter some text and print it out in reverse order.

text = input("Please, write something  down")
if text >0 and isinstance(text, str):
    rev_order = []
    i = -1
    for _ in text:
       # print(text[i])
        rev_order.append(text[i])
        i -= 1

rev_order = "".join(rev_order)        
print(rev_order)    
    
# Write a program that uses a for loop to print
# One of the months of the year is January
# One of the months of the year is February
# One of the months of the year is March etc …    

for amonth in ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'November', 'December']:
    print("One of the months of the year is", amonth)

# Assume you have a list of numbers 12, 10, 32, 3, 66, 17, 42, 99, 20. (a) Write a loop that prints each of the numbers on a new line. (b) Write a loop that prints each number and its square on a new line.

numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20]

print("Exercise a")
for number in numbers:
    print(number)

print("Exercise b")    
for number in numbers:
    print(number, number**2)
    
    
# Write a program that asks the user for the number of sides, the length of the side, the color, and the fill color of a regular polygon. The program should draw the polygon and then fill it in.


# Considering exterior angles

import turtle 
wn = turtle.Screen()
poly = turtle.Turtle()

sides = int(input("Enter the number of sides: "))
angle = 360/ sides

length = int(input("Enter the length of sides: "))

line_color = input("Enter the color of the lines: ")
poly.color(line_color)

fill_color = input("Enter the fill color for the polygon:" )
poly.fillcolor(fill_color)

poly.begin_fill()

for i in range(sides):
        poly.forward(length)
        poly.left(angle)
        
poly.end_fill()

wn.exitonclick()

# Considering interior angles 

import turtle
import math

wn = turtle.Screen()
poly = turtle.Turtle()


num_sides = int(input("Please, type the number of sides of your polygon"))


len_sides = float(input("Please, type the length of each side of your polygon"))

sum_angles = (num_sides - 2)*180
print(sum_angles)

each_angle = sum_angles / num_sides
print(each_angle)

color_lines = input("Please, type the color of the lines")
poly.color(color_lines) 

color_pol = input("Please, type the color of your polygon")
poly.fillcolor(color_pol)    
poly.begin_fill()  

for side in range(num_sides):
    poly.forward(len_sides)
    poly.left(each_angle)
    
    
poly.end_fill()

wn.exitonclick()


# A drunk pirate makes a random turn and then takes 100 steps forward, makes another random turn, takes another 100 steps, turns another random amount, etc. A social science student records the angle of each turn before the next 100 steps are taken. Her experimental data is 160, -43, 270, -97, -43, 200, -940, 17, -86. (Positive angles are counter-clockwise.) Use a turtle to draw the path taken by our drunk friend. After the pirate is done walking, print the current heading. Assume that the turtle originally has a heading of 0 and accumulate the changes in heading to print out the final. Your solution should work for any sequence of experimental data.

import turtle

wn = turtle.Screen()
lovelace = turtle.Turtle()

# move the turtle forward a little so that the whole path fits on the screen
lovelace.penup()
lovelace.forward(60)

# now draw the drunk pirate's path
lovelace.pendown()
current_heading = 0
angles = []

num_angles = input("How much do you want to see the pirate wandering?")

for i in range(int(num_angles)):
    angle_value = input("Please type the value of the angle", i)
    angles.append(float(angle_value))


for angle in angles:

    # we use .left() so that positive angles are counter-clockwise
    # and negative angles are clockwise
    current_heading = (current_heading + angle) % 360
    lovelace.left(angle)
    lovelace.forward(100)

# the .heading() method gives us the turtle's current heading in degrees
print("The pirate's final heading was", current_heading)

wn.exitonclick()



