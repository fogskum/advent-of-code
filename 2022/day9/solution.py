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
    head_pos = [1, 1]
    tail_pos = [1, 1]
    # count initial position
    tail_positions = {(tail_pos[0], tail_pos[1]):True}

    for line in lines:
        direction = line.split()[0]
        direction_vector = directions[direction]
        length = int(line.split()[1])
        for step in range(1, length+1):
            # save previous position
            prev_pos = [head_pos[0], head_pos[1]]
            head_pos[0] += direction_vector[0]
            head_pos[1] += direction_vector[1]
            # head has a new pos, check tail
            diff_x = abs(head_pos[0] - tail_pos[0])
            diff_y = abs(head_pos[1] - tail_pos[1])

            if diff_x > 1 or diff_y > 1:
                tail_pos[0] = prev_pos[0]
                tail_pos[1] = prev_pos[1]
                tail_positions[(tail_pos[0], tail_pos[1])] = True
    
    return len(tail_positions)

def get_input(filename):
    with open(filename, "r") as f:
        return f.read().split("\n")

if __name__ == "__main__":
    input_values = get_input("input.txt")
    
    part1_result = part1(input_values)
    print(part1_result)
    part1_expected = 5779
    assert part1_result == part1_expected