from pathlib import Path
import numpy as np

directions = {
    "R":(1,0),
    "L":(-1,0),
    "U":(0,-1),
    "D":(0,1)
}

grid = np.empty((3,3))

def part2():
    return 0

def part1(lines):
    hx = hy = 0
    tx = ty = 0
    positions = {}

    for line in lines:
        direction = directions[line.split()[0]]
        length = int(line.split()[1])
        for step in range(1, length+1):
            positions[(hx,hy)] = False
            hx += direction[0]
            hy += direction[1]
            # head has a new pos, check tail
            diff_x = abs(hx - tx)
            diff_y = abs(hy - ty)
    return 0

def get_input(filename):
    with open(filename, "r") as f:
        return f.read().split("\n")

if __name__ == "__main__":
    input_values = get_input("sample_input.txt")
    print(input_values)
    
    part1_result = part1(input_values)
    print(part1_result)