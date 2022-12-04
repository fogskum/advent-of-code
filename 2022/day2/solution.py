from pathlib import Path

def process_input() -> list[str]:
    with open("input.txt", "r") as f:
        list = f.read().split("\n")
        return list

if __name__ == "__main__":
    # part 1
    input_values = process_input()
    print(input_values)