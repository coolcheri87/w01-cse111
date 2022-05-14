# Cheri Hansen - cherilynne@byui.edu
# Created 5/7/2022
# CSE 111 - Christrian Elsinger
# Create a function to screne window contain outdoor scene for the program. '
# progrm that draws a semi realistic outdoor scene in a computer window.

# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing

import random

def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_sky(canvas, scene_width, scene_height)

    # draw the sun!
    draw_sun(canvas, random.randint(5,795), random.randint(200,500))

    # Draw a cloud.
    for x in range(random.randint(5,8)):
        x1 = random.randint(5,600)
        y1 = random.randint(200,450)
        dx = random.randint(50,300)
        dy = random.randint(30,dx)
        draw_cloud(canvas,x1,y1,x1+dx,y1+dy)

    # draw lots of grasss
    for y in reversed(range(10)):
        for x in range(200):
            draw_grass(canvas, x*4+y+random.randint(0,3), y*9+random.randint(0,4))

    # draw four trees
    treeX = [ 50, 175, 333, 700]
    treeY = [ 22, 155, 130, 145]
    for x in range(4): 
        draw_pine_tree(canvas, treeX[x], treeY[x], 100+random.randint(25,100))

    # draw houses
    draw_house(canvas, random.randint(50, 250), random.randint(10, 30))
    draw_house(canvas, random.randint(450, 650), random.randint(110, 130))
    
    draw_grid(canvas, scene_width, scene_height, 50)


    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# draw a house
def draw_house(canvas, leftX, bottomY):
    for x in reversed(range(6)):
        draw_oval(canvas, leftX+9+x*10, bottomY+152+x*10, leftX+25+x*15, bottomY+170+x*15, fill="darkgray")
    draw_rectangle(canvas, leftX+10, bottomY+100, leftX+25, bottomY+155, fill="tan4") # chimney
    draw_rectangle(canvas, leftX, bottomY, leftX+100, bottomY+100, fill="tan1") # building
    draw_rectangle(canvas, leftX+15, bottomY, leftX+40, bottomY+60, fill="tan3") # door
    draw_polygon(canvas, leftX-25, bottomY+100, leftX+125, bottomY+100, leftX+50, bottomY+150, fill="red") # root
    draw_rectangle(canvas, leftX+60, bottomY+40, leftX+85, bottomY+85, fill="lightblue")

# draw a little blade of grass
def draw_grass(canvas, leftX, bottomY):
    draw_polygon(canvas, leftX, bottomY+10, leftX+random.randint(2,4), bottomY+10, leftX+1, bottomY+15, outline="darkgreen", fill="green")
    draw_rectangle(canvas, leftX, bottomY, leftX+random.randint(2,4), bottomY+10, outline="darkgreen", fill="green")

# draw a pine tree
def draw_pine_tree(canvas, center_x, bottom, height):
    # draw trunk of the tree.
    trunk_width = height / 10
    trunk_height = height / 8
    left_trunk = center_x - trunk_width / 2
    bottom_trunk = bottom
    right_trunk = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height
    draw_rectangle(canvas, left_trunk, bottom_trunk, right_trunk, 
    trunk_top, fill="tan2")

    # draw leafy part of the tree.
    skirt_width = height / 2
    skirt_left = center_x - skirt_width / 2
    skirt_bottom = trunk_top
    peak_x = center_x
    peak_y = bottom + height
    skirt_right = center_x + skirt_width / 2
    draw_polygon(canvas, skirt_left, skirt_bottom, peak_x,
    peak_y, skirt_right, skirt_bottom, fill= "forestGreen")

# Draw a grid
def draw_grid(canvas, width, height, interval):
    # draw verical lines
    label_y = 15
    for x in range(interval, width, interval):
        draw_line(canvas, x, label_y*2, x, height)
        draw_text(canvas, x, label_y, f"{x}") 
     
      # draw horixontal lines
    label_x = 15
    for y in range(interval, width, interval):
        draw_line(canvas, label_x*2, y, width, y)
        draw_text(canvas, label_x, y, f"{y}") 
     
# draw a fluffy white cloud!
def draw_cloud(canvas, x0, y0, x1, y1):
    draw_oval(canvas, x0, y0, x1, y1, width=1, outline="white", fill="white")

# draw mr. sunshine
def draw_sun(canvas, x, y):
    draw_oval(canvas, x-35, y-35, x+35, y+35, outline="yellow", fill="yellow")

# draw the sky and ground...
def draw_sky(canvas, scene_width, scene_height):
    """Draw the ground and all the objects on the ground."""
    draw_rectangle(canvas, 0, 0, scene_width, scene_height / 3, width = 0, fill="tan4")
    draw_rectangle(canvas, 0, scene_height / 3, scene_width, scene_height, width =0, fill="lightBlue")




# Call the main function so that
# this program will start executing.
main()