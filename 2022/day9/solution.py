from pathlib import Path
import numpy as np

directions = {
    "R":(1,0),
    "L":(-1,0),
    "U":(0,-1),
    "D":(0,1)
}

class Point2D:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

grid = np.empty((3,3))

def is_tail_near(head, tail):
    return False

def part2():
    return 0

def part1(lines):
    hx = hy = 1
    tx = ty = 1
    positions = {}
    grd = []

    for line in lines:
        direction = line.split()[0]
        direction_vector = directions[direction]
        length = int(line.split()[1])
        for step in range(1, length+1):
            positions[(hx,hy)] = False
            hx += direction_vector[0]
            hy += direction_vector[1]
            # head has a new pos, check tail
            diff_x = abs(hx - tx)
            diff_y = abs(hy - ty)            
            if direction == "R" and diff_x > 1:
                tx += 1
            elif direction == "L" and diff_x > 1:
                tx -= 1
            elif direction == "U" and diff_y > 1:
                ty -= 1
            elif direction == "D" and diff_y > 1:
                ty += 1

            if diff_x > 1 and diff_y > 1:
                if direction == "U":
                    diff_x += 1
                if direction == "D":
                    diff_x +=
    return 0

def get_input(filename):
    with open(filename, "r") as f:
        return f.read().split("\n")

if __name__ == "__main__":
    input_values = get_input("sample_input.txt")
    print(input_values)
    
    part1_result = part1(input_values)
    print(part1_result)