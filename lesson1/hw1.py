from random import randint


SIZE_N = 5
SIZE_M = 5

char_x = 0
char_y = 0

exit_x = randint(0, SIZE_N - 1)
exit_y = randint(0, SIZE_M - 1)

turns = 0

while True:
    world_map = ""
    for j in range(SIZE_M):
        row = "|"
        for i in range(SIZE_N):
            if char_x == i and char_y == j:
                row += "X|"
            elif exit_y == j and exit_x == i:
                row += "0|"
            else:
                row += " |"
        world_map += f"{row}\n"

    print(world_map)

    if char_x == exit_x and char_y == exit_y:

        print("You Won in {turns}")
        break

    direction = input("Enter direction (u/d/l/r):")
    if direction == "u" and char_y > 0:
        char_y -= 1
    elif direction == "d" and char_y < SIZE_M - 1:
        char_y += 1
    elif direction == "l" and char_x > 0:
        char_x -= 1
    elif direction == "r" and char_x < SIZE_N - 1:
        char_x += 1
    else:
        print("n0")


'''''''''''''''''''''''''''''''''''''''''''''''''''''tkk                        mbb'''''
