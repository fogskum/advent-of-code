from pathlib import Path
from enum import Enum

class Shape(Enum):
    Rock = 1
    Paper = 2
    Scissor = 3

class Score(Enum):
    Win = 6,
    Loss = 0,
    Draw = 3

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

def part1(input_values):
    opponent_score = 0
    my_score = 0
    for round in input_values:
        opponent_shape = opponent_map[round.split(" ")[0]]
        my_shape = my_map[round.split(" ")[1]]
        print("Opponent plays " + str(opponent_shape) + ", I play " + str(my_shape))

        if opponent_shape == my_shape:
            opponent_score += (my_shape + Score.Draw)
        elif opponent_shape == Shape.Rock and my_shape == Shape.Scissor:
            opponent_score += 

def get_input() -> list[str]:
    with open("input.txt", "r") as f:
        list = f.read().split("\n")
        return list

if __name__ == "__main__":
    # part 1
    input_values = get_input()
    part1(input_values)