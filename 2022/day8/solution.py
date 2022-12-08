from pathlib import Path

def get_input(filename):
    with open(filename, "r") as f:
        return f.read().split("\n")

def get_matrix(input_values):
    matrix = []
    for line in input_values:
        rows = [int(char) for char in line]
        matrix.append(rows)
    return matrix

def is_edge(matrix, row, col):
    # we assume the matrix is NxN
    max = len(matrix)
    if row == 0 or col == 0 or (row == max - 1) or (col == max - 1):
        return True
    return False

def get_vertical_heights(matrix, col):
    heights = []
    for row in range(0, len(matrix)):
        height = matrix[row][col]
        heights.append(height)
    return heights

def get_heights_greater_than(heights, height):
    return [h for h in heights if h >= height]

def tree_at_pos_visible(matrix, row, col, tree_height):
    if is_edge(matrix, row, col):
        return True

    count = 0
    # right side
    heights = matrix[row][:col]
    if len(get_heights_greater_than(heights, tree_height)) == 0:
        count += 1
    
    # left side
    heights = matrix[row][col+1:]
    if len(get_heights_greater_than(heights, tree_height)) == 0:
        count += 1
    
    # top size
    heights = get_vertical_heights(matrix, col)
    if len(get_heights_greater_than(heights, tree_height)) == 0:
        count += 1

    return False

def part1(matrix):
    visible_count = 0
    row = 0
    for i in matrix:
        col = 0
        for tree_height in i:
            #tree_height = matrix[row][col]
            if tree_at_pos_visible(matrix, row, col, tree_height):
                visible_count += 1
            col += 1
        row += 1

    return visible_count

if __name__ == "__main__":
    input_values = get_input("sample_input.txt")
    matrix = get_matrix(input_values)
    part1_result = part1(matrix)
    print(part1_result)