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
    return count_unique_tail_pos(lines, 10)

def count_unique_tail_pos(lines, nrb_knots):
    # start_x = int(curses.COLS / 2)
    # start_y = int(curses.LINES / 2)
    rope = [Knot(start_x, start_y, str(i)) for i in range(nrb_knots)]

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
                dx = rope[i-1].x - rope[i].x
                dy = rope[i-1].y - rope[i].y
                adx = abs(dx)
                ady = abs(dy)
                
                if adx == 0 and ady == 0:
                    continue
                
                if adx == 1 and ady == 1:
                    continue
                    
                if dx > 1 and dy == 0:
                    rope[i].IncPos(1, 0) # move right
                elif dx < -1 and dy == 0:
                    rope[i].IncPos(-1, 0) # move left
                elif dx == 0 and dy > 1:
                    rope[i].IncPos(0, 1) # move up
                elif dx == 0 and dy < -1:
                    rope[i].IncPos(0, -1) # move down
                elif dx >= 1 and dy > 1 or dx > 1 and dy >= 1:
                    rope[i].IncPos(1, 1) # up+right
                elif dx >= 1 and dy < -1 or dx > 1 and dy <= -1:
                    rope[i].IncPos(1, -1) # down+right
                elif dx <= -1 and dy > 1 or dx < -1 and dy >= 1:
                    rope[i].IncPos(-1, 1) # up+left
                elif dx <= -1 and dy < -1 or dx < -1 and dy <= -1:
                    rope[i].IncPos(-1, -1) # down+left

                tail_positions[(tail.x, tail.y)] = True

    return len(tail_positions)

def part1(lines):
    return count_unique_tail_pos(lines, 2)

def get_input(filename):
    with open(filename, "r") as f:
        return f.read().split("\n")

if __name__ == "__main__":
    input_values = get_input("input.txt")
    
    part1_result = part1(input_values)
    print(part1_result)
    part1_expected = 5779
    assert part1_result == part1_expected

    part2_result = part2(input_values)
    print(part2_result)
    part2_expected = 2331
    assert part2_result == part2_expected