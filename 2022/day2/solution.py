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

win_map = { 
    Shape.Rock: Shape.Paper,
    Shape.Paper: Shape.Scissor,
    Shape.Scissor: Shape.Rock
}

lose_map = { 
    Shape.Rock: Shape.Scissor,
    Shape.Paper: Shape.Rock,
    Shape.Scissor: Shape.Paper
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

def part2(input_values):
    my_score = 0
    for round in input_values:
        opponent_shape = opponent_map[round.split(" ")[0]]
        my_outcome = round.split(" ")[1]
        if my_outcome == "X": # I need to lose
            my_score += calc_score(opponent_shape, lose_map[opponent_shape])
        elif my_outcome == "Y":
            # need to be a draw, use the same shape as my opponent
            my_score += calc_score(opponent_shape, opponent_shape)
        else:
            # I need to win
            my_score += calc_score(opponent_shape, win_map[opponent_shape])
    
    print(my_score)


def get_input() -> list[str]:
    with open("input.txt", "r") as f:
        list = f.read().split("\n")
        return list

if __name__ == "__main__":
    input_values = get_input()
    part1(input_values)
    part2(input_values)