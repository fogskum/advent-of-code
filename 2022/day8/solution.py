from pathlib import Path
import numpy as np

def get_input(filename):
    with open(filename, "r") as f:
        return f.read().split("\n")

def get_matrix(input_values):
    matrix = []
    for line in input_values:
        # create list of tree heights
        rows = [int(char) for char in line]
        matrix.append(rows)
    return matrix

def is_edge(matrix, row, col):
    # we assume the matrix is NxN
    max = len(matrix)
    if row == 0 or col == 0 or (row == max - 1) or (col == max - 1):
        return True
    return False

def get_top_heights(matrix, row, col):
    heights = []
    for row in range(0, row):
        height = matrix[row][col]
        heights.append(height)
    return heights 

def get_bottom_heights(matrix, start_row, col):
    heights = []
    for row in range(start_row+1, len(matrix)):
        height = matrix[row][col]
        heights.append(height)
    return heights    

def get_trees_lower_than(heights, height):
    return [h for h in heights if h >= height]

def is_visible(heights, height):
    if len(get_trees_lower_than(heights, height)) == 0:
        return True
    return False

def is_tree_visible_at_pos(matrix, row, col, height):
    if is_edge(matrix, row, col):
        return True

    # right side
    heights = matrix[row][:col]
    if is_visible(heights, height):
        return True
    
    # left side
    heights = matrix[row][col+1:]
    if is_visible(heights, height):
        return True
    
    # top side
    heights = get_top_heights(matrix, row, col)
    if is_visible(heights, height):
        return True

    # bottom side
    heights = get_bottom_heights(matrix, row, col)
    if is_visible(heights, height):
        return True

    return False

def record_num_visible_trees(array, height, nums):
    count = 0
    for value in array:
        count += 1
        if value >= height:
            break
    
    if count > 0:
        nums.append(count)

def get_scenic_score(matrix, row, col):
    m = np.array(matrix)
    height = m[row][col]
    nums = []
    ranges = [ 
        m[:row, col][::-1], # up (reversed)
        m[row+1:, col],     # down
        m[row, col+1:],     # right
        m[row, :col][::-1]  # left (revered)
    ]
    [record_num_visible_trees(range, height, nums) for range in ranges]
    # calculate the score by multiplying all numbers
    return np.prod(nums).item()

def part1(matrix):
    count = 0
    row = 0
    for i in matrix:
        col = 0
        for tree_height in i:
            if is_tree_visible_at_pos(matrix, row, col, tree_height):
                count += 1
            col += 1
        row += 1
    return count

def part2(matrix):
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