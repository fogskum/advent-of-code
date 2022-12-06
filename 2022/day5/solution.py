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

def get_message(all_stacks):
    return [stack[0] for stack in all_stacks.values()]

def get_stacks(input_values, crate_count):
    line_num = 0
    current_idx = 0
    # init stacks with empty stack
    all_stacks = {i: [] for i in range(1, crate_count+1)}
    for line in input_values:
        if line == "\n":
            break
        line_num += 1
        
        for crate_idx in range(1, crate_count + 1):
            # crate id found on every 4th char
            current_idx = crate_idx * 4 - 3
            crate_id = line[current_idx]
            if crate_id != ' ':
                # create found
                local_crates = all_stacks[crate_idx]
                local_crates.append(crate_id)
    
    return all_stacks

def get_input(filename):
    with open(filename, "r") as f:
        return f.readlines()

if __name__ == "__main__":
    input_values = get_input("sample_input.txt")
    stacks = get_stacks(input_values, 3)
    msg = get_message(stacks)
    print(msg)
    
