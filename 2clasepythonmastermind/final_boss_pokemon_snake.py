import os 
import random
import readchar

POS_X = 0 
POS_Y = 1
MAP_WIDTH = 20
MAP_HEIGHT = 15

my_position = [2, 2]


# map drawing
print("+" + "-" * MAP_WIDTH * 3 + "+")
for coordinate_y in range(MAP_WIDTH):
    print("|", end="")
    for coordinate_x in range(MAP_WIDTH):
        
        if  my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
            print(" @ ", end="")
        else: 
         print("   ", end="")
         
    print("|")
print("+" + "-" * MAP_WIDTH * 3 + "+")