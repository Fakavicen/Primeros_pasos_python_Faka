import readchar , os

POS_X = 0 
POS_Y = 1
MAP_WIDTH = 20
MAP_HEIGHT = 15
direction = 0
my_position = [3, 1]

map_objects = [[2,3], [5,4], [3,4], [10,6]]

my_position[POS_X]
my_position[POS_Y]

while True:
    # Draw Map
    print("+" + "-" * MAP_WIDTH * 3 + "+")

    for coordinate_y in range(MAP_HEIGHT):
        print("|", end="")

        for coordinate_x in range(MAP_WIDTH):

            char_to_draw = " "

            for map_object in map_objects:
                if map_object[POS_X] == coordinate_x and map_object[POS_Y] == coordinate_y:
                    char_to_draw = "*"

            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                char_to_draw = "@"


            print(" {} ".format(char_to_draw), end="")
        print("|")

        
    print("+" + "-" * MAP_WIDTH * 3 + "+")

    #movimiento
    ##direction = input("Donde quieres mover? [WASD]")
    direction = readchar.readchar()
    if direction == "w":
        my_position[POS_Y] -= 1
        my_position[POS_Y] %= MAP_HEIGHT
    elif direction == "s":
        my_position[POS_Y] += 1
        my_position[POS_Y] %= MAP_HEIGHT
    elif direction == "a":
        my_position[POS_X] -= 1
        my_position[POS_X] %= MAP_WIDTH
    elif direction == "d":
        my_position[POS_X] += 1
        my_position[POS_X] %= MAP_WIDTH