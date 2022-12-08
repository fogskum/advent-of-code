from pathlib import Path

def get_input(filename):
    with open(filename, "r") as f:
        return f.read().split("\n")

if __name__ == "__main__":
    input_values = get_input("sample_input.txt")
    print(input_values)