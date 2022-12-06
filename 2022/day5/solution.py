from pathlib import Path

class Instruction:
    def __init__(self, qty, from_stack_id, to_stack_id):
        self.Quantity = qty
        self.FromStackId = from_stack_id
        self.ToStackId = to_stack_id

    Quantity = 0
    FromStackId = 0
    ToStackId = 0

def get_message(all_stacks):
    # return the first crate id in each stack
    return "".join([stack[0] for stack in all_stacks.values()])

def get_stacks(input_values, stack_count):
    current_idx = 0
    # get all lines with crates
    crate_lines = [line for line in input_values if "[" in line]
    # init stacks with empty stack
    all_stacks = {i: [] for i in range(1, stack_count+1)}
    for line in crate_lines:
        for crate_idx in range(1, stack_count + 1):
            # crate id found on every 4th char
            current_idx = crate_idx * 4 - 3
            crate_id = line[current_idx]
            if crate_id != ' ':
                # create found
                local_crates = all_stacks[crate_idx]
                local_crates.append(crate_id)

    return all_stacks

def get_instructions(input_values):
    # get lines with instructions
    lines = [line for line in input_values if "move" in line]
    instructions = []
    for line in lines:
        line_parts = line.split(' ')
        instruction = Instruction(int(line_parts[1]), int(line_parts[3]), int(line_parts[5]))
        instructions.append(instruction)

    return instructions

def apply_instructions(instructions, stacks):
    for instruction in instructions:
        #  find stack to move from
        stack_from = stacks[instruction.FromStackId]
        stack_to = stacks[instruction.ToStackId]
        # move crates
        [stack_to.insert(0, stack_from.pop(0)) for n in range(0, instruction.Quantity)]

def part1(input_values, stack_count):
    stacks = get_stacks(input_values, stack_count)
    instructions = get_instructions(input_values)
    apply_instructions(instructions, stacks)
    return get_message(stacks)

def get_input(filename):
    with open(filename, "r") as f:
        return f.readlines()

if __name__ == "__main__":
    input_values = get_input("input.txt")
    
    #part1_expected = "CMZ"
    part1_expected = "FWNSHLDNZ"
    part1_result = part1(input_values, 9)
    assert part1_expected == part1_result
