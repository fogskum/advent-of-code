from pathlib import Path

class Instruction:
    Quantity = 0
    FromCrate = 0
    ToCrate = 0

def get_stack_count(input_values):
    line_num = 0
    for line in input_values:
        if line == "\n":
            break
        line_num += 1

    print(line_num)
    numbers = input_values[line_num-1].strip().split("   ")
    print(numbers)

def get_input(filename):
    with open(filename, "r") as f:
        return f.readlines()

if __name__ == "__main__":
    input_values = get_input("sample_input.txt")
    get_stack_count(input_values)
    
