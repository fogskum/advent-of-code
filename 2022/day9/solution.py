from pathlib import Path

directions = {
    "R":(1,0),
    "L":(-1,0),
    "U":(0,-1),
    "D":(0,1)
}

class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

# def track_tail(lines, rope):
#     # count initial tail position
#     head_pos = rope[0]
#     tail_pos = rope[-1]
#     tail_positions = {(tail_pos.x, tail_pos.y):True}

#     for line in lines:
#         direction = line.split()[0]
#         direction_vector = directions[direction]
#         length = int(line.split()[1])
#         for step in range(1, length+1):
#             # save previous position
#             prev_pos = Point(head_pos.x, head_pos.y)
#             head_pos.x += direction_vector[0]
#             head_pos.y += direction_vector[1]
#             # head has a new pos, check distance to next knot
#             diff_x = abs(head_pos.x - tail_pos.x)
#             diff_y = abs(head_pos.y - tail_pos.y)

#             if diff_x > 1 or diff_y > 1:
#                 tail_pos.x = prev_pos.x
#                 tail_pos.y = prev_pos.y
#                 tail_positions[(tail_pos.x, tail_pos.y)] = True
    
#     return len(tail_positions)

def track_tail(lines, rope):
    # count initial tail position
    head_pos = rope[0]
    tail_pos = rope[-1]
    tail_positions = {(tail_pos.x, tail_pos.y):True}

    for line in lines:
        direction = line.split()[0]
        direction_vector = directions[direction]
        steps = int(line.split()[1])
        rope_len = len(rope)
        for _ in range(1, steps+1):
            for i in range(0, rope_len):
                prev_knot = rope[i]
                knot = rope[i+1]

                if i == 0:
                    head_pos.x += direction_vector[0]
                    head_pos.y += direction_vector[1]
                else:
                    diff_x = abs(knot.x - prev_knot.x)
                    diff_y = abs(knot.y - prev_knot.y)
                    if diff_x > 1 or diff_y > 1:
                        knot.x = prev_knot.x
                        knot.y = prev_knot.y
                        if i == rope_len-1:
                            tail_positions[(knot.x, knot.y)] = True
                    prev_knot = knot
    
    return len(tail_positions)

def part1(input_values):
    rope = [Point(0, 0) for _ in range(2)]
    return track_tail(input_values, rope)

def part2(input_values):
    rope = [Point(0, 0) for _ in range(10)]
    return track_tail(input_values, rope)

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