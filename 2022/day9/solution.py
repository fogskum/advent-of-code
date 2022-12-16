from pathlib import Path
import sys
import curses

directions = {
    "R":(1,0),
    "L":(-1,0),
    "U":(0,1),
    "D":(0,-1)
}

start_x = 0
start_y = 0

stdscr = curses.initscr()

class Knot:
    def __init__(self, x, y, symbol) -> None:
        self.x = x
        self.y = y
        self.symbol = symbol

    def SetPos(self, x, y):
        self.x = x
        self.y = y

    def IncPos(self, x, y):
        self.x += x
        self.y += y

def draw(rope):
    for knot in rope:
        stdscr.addstr(knot.x, knot.y, knot.symbol)
    stdscr.clear()
    stdscr.refresh()

def part2(lines):
    # start_x = int(curses.COLS / 2)
    # start_y = int(curses.LINES / 2)
    rope = [Knot(start_x, start_y, str(i)) for i in range(10)]

    # count initial tail position
    head = rope[0]
    tail = rope[-1]
    tail_positions = {(tail.x, tail.y):True}

    for line in lines:
        direction = line.split()[0]
        direction_vector = directions[direction]
        steps = int(line.split()[1])
        knot_count = len(rope)
        for _ in range(steps):
            head.IncPos(direction_vector[0], direction_vector[1])
            for i in range(1, knot_count):
                diff_x = rope[i-1].x - rope[i].x
                diff_y = rope[i-1].y - rope[i].y
                if diff_x == 0 or diff_y == 0:
                    continue

                if diff_x > 1:
                    rope[i].IncPos(1, 0) # move right
                if diff_x < 1:
                    rope[i].IncPos(-1, 0) # move left

                if diff_y > 1 and abs(diff_x) == 1:
                    rope[i].IncPos(1, 1) # move up
                if diff_y < 1:
                    rope[i].IncPos(0, -1) # move down

                tail_positions[(tail.x, tail.y)] = True

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
    #print(part1_result)
    #part1_expected = 5779
    #assert part1_result == part1_expected

    part2_result = part2(input_values)
    print(part2_result)