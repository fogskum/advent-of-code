from pathlib import Path

def part1(input_values):
    print(input_values)

def get_input(filename):
    with open(filename, "r") as f:
        return f.read().split("\n")

if __name__ == "__main__":
    input_values = get_input("sample_input.txt")
    part1(input_values)
