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

def visible_trees_at_pos(matrix, row, col, tree_height):
    if is_edge(matrix, row, col):
        return True

    # right side
    heights = matrix[row][:col]
    if len(get_trees_lower_than(heights, tree_height)) == 0:
        return True
    
    # left side
    heights = matrix[row][col+1:]
    if len(get_trees_lower_than(heights, tree_height)) == 0:
        return True
    
    # top side
    heights = get_top_heights(matrix, row, col)
    if len(get_trees_lower_than(heights, tree_height)) == 0:
        return True

    # bottom side
    heights = get_bottom_heights(matrix, row, col)
    if len(get_trees_lower_than(heights, tree_height)) == 0:
        return True

    return False

def part1(matrix):
    count = 0
    row = 0
    for i in matrix:
        col = 0
        for tree_height in i:
            if visible_trees_at_pos(matrix, row, col, tree_height):
                count += 1
            col += 1
        row += 1

    return count

if __name__ == "__main__":
    input_values = get_input("input.txt")
    matrix = get_matrix(input_values)
    
    part1_result = part1(matrix)
    part1_expected = 1662
    assert part1_result == part1_expected