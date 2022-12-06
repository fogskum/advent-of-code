from pathlib import Path
from collections import Counter

def get_start_pos(input_values, window_size):
    start_idx = 0
    while True:
        end_idx = start_idx + window_size
        seq = input_values[start_idx:end_idx]
        if is_marker(seq):
            return end_idx
        
        start_idx += window_size - 1

def is_marker(seq):
    string = Counter(seq)
    for char, count in string.items():
        if(count > 1):
            return False
    return True

def part1(input_values):
    return get_start_pos(input_values, 4)

def part2(input_values):
    return get_start_pos(input_values, 14) - 1

def get_input(filename):
    with open(filename, "r") as f:
        return f.readline()

if __name__ == "__main__":
    input_values = get_input("input.txt")
    part1_result = part1(input_values)
    part1_expected = 1909
    assert part1_result == part1_expected

    part2_result = part2(input_values)
    part2_expected = 3380
    assert part2_result == part2_expected
