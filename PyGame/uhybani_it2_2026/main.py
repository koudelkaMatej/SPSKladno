# Importing pygame module
import pygame
from pygame.locals import *

# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()

# create the display surface object
# of specific dimension.
window = pygame.display.set_mode((600, 600))

# Fill the scree with white color
window.fill((255, 255, 255))

# creating list in which we will store
# the position of the circle
circle_positions = []

# radius of the circle
circle_radius = 60

# Color of the circle
color = (0, 0, 255)

# Creating a variable which we will use
# to run the while loop
run = True

# Creating a while loop
while run:

    # Iterating over all the events received from
    # pygame.event.get()
    for event in pygame.event.get():

        # If the type of the event is quit
        # then setting the run variable to false
        if event.type == QUIT:
            run = False

        # if the type of the event is MOUSEBUTTONDOWN
        # then storing the current position
        elif event.type == MOUSEBUTTONDOWN:
            position = event.pos
            circle_positions.append(position)
            
    # Using for loop to iterate
    # over the circle_positions
    # list
    if len(circle_positions) % 3 == 0:
    
        for i in range(0, len(circle_positions), 3):
            left_corner = circle_positions[i]
            right_corner = circle_positions[i + 1]
            pygame.draw.polygon(window, color, [left_corner, right_corner, circle_positions[i + 2]])

    # Draws the surface object to the screen.
    pygame.display.update()