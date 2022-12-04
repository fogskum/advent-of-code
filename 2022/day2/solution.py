from pathlib import Path
from enum import Enum, IntEnum

class Shape(IntEnum):
    Rock = 1
    Paper = 2
    Scissor = 3

opponent_map = {
    "A": Shape.Rock,
    "B": Shape.Paper,
    "C": Shape.Scissor
}

my_map = {
    "X": Shape.Rock,
    "Y": Shape.Paper,
    "Z": Shape.Scissor
}

def calc_score(opponent_shape, my_shape) -> int:
    win = 6
    draw = 3
    score = 0
    shape_score = int(my_shape)

    if opponent_shape == my_shape:
        # draw
        score = (shape_score + draw)
    elif opponent_shape == Shape.Rock:
        if my_shape == Shape.Scissor:
            score = shape_score
        elif my_shape == Shape.Paper:
            score = (shape_score + win)
    elif opponent_shape == Shape.Paper:
        if my_shape == Shape.Rock:
            score = shape_score
        elif my_shape == Shape.Scissor:
            score = (shape_score + win)
    elif opponent_shape == Shape.Scissor:
        if my_shape == Shape.Rock:
            score = (shape_score + win)
        elif my_shape == Shape.Paper:
            score = shape_score
    return score

# correct score = 10816
def part1(input_values):
    my_score = 0
    for round in input_values:
        opponent_shape = opponent_map[round.split(" ")[0]]
        my_shape = my_map[round.split(" ")[1]]
        print("Opponent plays " + str(opponent_shape) + ", I play " + str(my_shape))
        my_score += calc_score(opponent_shape, my_shape)
        
    print( "My total score: " + str(my_score) )

def get_input() -> list[str]:
    with open("input.txt", "r") as f:
        list = f.read().split("\n")
        return list

if __name__ == "__main__":
    # part 1
    input_values = get_input()
    part1(input_values)