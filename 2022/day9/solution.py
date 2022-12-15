from pathlib import Path
import sys

directions = {
    "R":(1,0),
    "L":(-1,0),
    "U":(0,-1),
    "D":(0,1)
}

class Knot:
    def __init__(self, x, y, symbol) -> None:
        self.x = x
        self.y = y
        self.symbol = symbol

def part2(lines):
    rope = [Knot(0, 0, str(i)) for i in range(10)]

    # count initial tail position
    head_pos = rope[0]
    tail = rope[-1]
    tail_positions = {(tail.x, tail.y):True}

    for line in lines:
        direction = line.split()[0]
        direction_vector = directions[direction]
        steps = int(line.split()[1])
        rope_len = len(rope)
        for _ in range(steps):
            prev_pos = Knot(head_pos.x, head_pos.y, head_pos.symbol)
            head_pos.x += direction_vector[0]
            head_pos.y += direction_vector[1]
            next_knot = rope[1]
            diff_x = abs(head_pos.x - next_knot.x)
            diff_y = abs(head_pos.y - next_knot.y)            
            if diff_x > 1 or diff_y > 1:
                # move all other knots
                for i in range(1, rope_len):
                    prev_tail_pos = Knot(tail.x, tail.y, tail.symbol)
                    temp_pos = Knot(rope[i].x, rope[i].y, rope[i].symbol)
                    rope[i].x = prev_pos.x
                    rope[i].y = prev_pos.y
                    # did the tail get a new position?
                    if tail.x != prev_tail_pos.x or tail.y != prev_tail_pos.y:
                        tail_positions[(tail.x, tail.y)] = True
                    prev_pos = Knot(temp_pos.x, temp_pos.y, temp_pos.symbol)

    return len(tail_positions)

def part1(input_values):
    rope = [Knot(0, 0, str(i)) for i in range(2)]
    # count initial tail position
    head_pos = rope[0]
    tail_pos = rope[-1]
    tail_positions = {(tail_pos.x, tail_pos.y):True}

    for line in input_values:
        direction = line.split()[0]
        direction_vector = directions[direction]
        length = int(line.split()[1])
        for step in range(1, length+1):
            # save previous position
            prev_pos = Knot(head_pos.x, head_pos.y, head_pos.symbol)
            head_pos.x += direction_vector[0]
            head_pos.y += direction_vector[1]
            # head has a new pos, check distance to next knot
            diff_x = abs(head_pos.x - tail_pos.x)
            diff_y = abs(head_pos.y - tail_pos.y)

            if diff_x > 1 or diff_y > 1:
                tail_pos.x = prev_pos.x
                tail_pos.y = prev_pos.y
                tail_positions[(tail_pos.x, tail_pos.y)] = True
    
    return len(tail_positions)

def get_input(filename):
    with open(filename, "r") as f:
        return f.read().split("\n")

if __name__ == "__main__":
    input_values = get_input("sample_input.txt")
    
    part1_result = part1(input_values)
    print(part1_result)
    #part1_expected = 5779
    #assert part1_result == part1_expected

    part2_result = part2(input_values)
    print(part2_result)