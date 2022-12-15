from pathlib import Path

directions = {
    "R":(1,0),
    "L":(-1,0),
    "U":(0,-1),
    "D":(0,1)
}

init_x = 0
init_y = 0

def track_tail(lines, rope):
    # count initial position
    tail_pos = rope[-1]
    tail_positions = {(tail_pos[0], tail_pos[1]):True}

    for line in lines:
        direction = line.split()[0]
        direction_vector = directions[direction]
        length = int(line.split()[1])
        for step in range(1, length+1):
            # save previous position
            head_pos = rope[0]
            prev_pos = [head_pos[0], head_pos[1]]
            head_pos[0] += direction_vector[0]
            head_pos[1] += direction_vector[1]
            # head has a new pos, check distance to tail
            diff_x = abs(head_pos[0] - tail_pos[0])
            diff_y = abs(head_pos[1] - tail_pos[1])

            if diff_x > 1 or diff_y > 1:
                tail_pos[0] = prev_pos[0]
                tail_pos[1] = prev_pos[1]
                tail_positions[(tail_pos[0], tail_pos[1])] = True
    
    return len(tail_positions)

def part1(input_values):
    rope = [[init_x, init_y] for _ in range(2)]
    return track_tail(input_values, rope)

def part2(input_values):
    init_x = 0
    init_y = 0
    rope = [[init_x, init_y] for _ in range(10)]
    return track_tail(input_values, rope)

def get_input(filename):
    with open(filename, "r") as f:
        return f.read().split("\n")

if __name__ == "__main__":
    input_values = get_input("input.txt")
    
    part1_result = part1(input_values)
    part1_expected = 5779
    assert part1_result == part1_expected