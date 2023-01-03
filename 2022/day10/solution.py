from pathlib import Path

def execute_instructions(instructions):
    # initial register value
    cycle_values = [1]
    for instruction in instructions:
        if instruction == "noop":
            cycle_values.append( cycle_values[-1] )
        else:
            if instruction.split()[0] == "addx":
                cycle_values.append( cycle_values[-1] )
                cycle_values.append( cycle_values[-1] + int(instruction.split()[1]))
            
    signal_strength = sum([i * cycle_values[i-1] for i in range(20, 240, 40)])
    return cycle_values, signal_strength

def get_instructions(filename):
    with open(filename, "r") as f:
        return f.read().splitlines()

if __name__ == "__main__":
    instructions = get_instructions("input.txt")
    cycle_values, signal_strength = execute_instructions(instructions)
    print(signal_strength)
    #assert part1_result == 13140
    assert signal_strength == 15680
