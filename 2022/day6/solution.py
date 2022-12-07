from pathlib import Path
from collections import Counter

def get_marker_pos(input_values, window_size):
    start = window_size-1
    end = len(input_values)-(window_size-1)
    for i in range(start, end):
        marker = input_values[i-window_size:i]
        # check character frequency in marker
        freq = Counter(marker)
        # if the frequency size = window_size, marker is unique
        if len(freq) == window_size:
            return i

def part1(input_values):
    return get_marker_pos(input_values, 4)

def part2(input_values):
    return get_marker_pos(input_values, 14)

def get_input(filename):
    with open(filename, "r") as f:
        return f.readline().strip()

if __name__ == "__main__":
    input_values = get_input("input.txt")
    part1_result = part1(input_values)
    part1_expected = 1909
    assert part1_result == part1_expected

    part2_result = part2(input_values)
    part2_expected = 3380
    assert part2_result == part2_expected
