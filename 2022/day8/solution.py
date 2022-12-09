from pathlib import Path
import numpy as np

def get_input(filename):
    with open(filename, "r") as f:
        return f.read().split("\n")

def get_matrix(input_values) -> np.array:
    matrix = []
    for line in input_values:
        # create list of tree heights
        rows = [int(char) for char in line]
        matrix.append(rows)
    return np.array(matrix)

def is_edge(matrix, row, col) -> bool:
    # we assume the matrix is NxN
    max = len(matrix)
    if row == 0 or col == 0 or (row == max - 1) or (col == max - 1):
        return True
    return False

def get_trees_lower_than(heights, height) -> list[int]:
    return [h for h in heights if h >= height]

def is_visible(heights, height) -> bool:
    if len(get_trees_lower_than(heights, height)) == 0:
        return True
    return False

def is_tree_visible_at_pos(matrix, row, col) -> bool:
    if is_edge(matrix, row, col):
        return True

    height = matrix[row][col]
    ranges = [ 
        matrix[:row, col],      # top
        matrix[row+1:, col],    # bottom
        matrix[row, col+1:],    # right
        matrix[row, :col]       # left
    ]

    for range in ranges:
        if is_visible(range, height):
            return True
    return False

def record_num_visible_trees(array, height, nums) -> None:
    count = 0
    for value in array:
        count += 1
        if value >= height:
            break
    
    if count > 0:
        nums.append(count)

def get_scenic_score(matrix, row, col) -> int:
    height = matrix[row][col]
    nums = []
    ranges = [ 
        matrix[:row, col][::-1], # up (reversed)
        matrix[row+1:, col],     # down
        matrix[row, col+1:],     # right
        matrix[row, :col][::-1]  # left (reversed)
    ]
    [record_num_visible_trees(range, height, nums) for range in ranges]
    # calculate the score by multiplying all numbers
    return np.prod(nums).item()

def part1(matrix) -> int:
    count = 0
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            if is_tree_visible_at_pos(matrix, i, j):
                count += 1
    return count

def part2(matrix) -> int:
    max_score = 0
    maxlen = len(matrix)-1
    for i in range(1, maxlen):
        for j in range(1, maxlen):
            score = get_scenic_score(matrix, i, j)
            max_score = score if score > max_score else max_score
    return max_score

if __name__ == "__main__":
    input_values = get_input("input.txt")
    matrix = get_matrix(input_values)
    
    part1_result = part1(matrix)
    part1_expected = 1662
    #part1_expected = 21
    assert part1_result == part1_expected

    part2_result = part2(matrix)
    #part2_expected = 8
    part2_expected = 537600
    assert part2_result == part2_expected