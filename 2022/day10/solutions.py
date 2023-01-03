def execute_instructions(instructions):
    # initial register value
    cycle_values = [1]
    for instruction in instructions:
        if instruction == "noop":
            cycle_values.append( cycle_values[-1] )
            continue

        if instruction.split()[0] == "addx":
            cycle_values.append( cycle_values[-1] )
            cycle_values.append( cycle_values[-1] + int(instruction.split()[1]))
            
    signal_strength = sum([value * cycle_values[value-1] for value in range(20, 240, 40)])
    return cycle_values, signal_strength

def draw_sprite(cycle_values):
    pixles = ""
    for value in cycle_values:
        current_pos = len(pixles)
        print("Start cycle {}".format(current_pos+1))
        if current_pos in range(value-1, value+1, 1):
            pixles += "#"
        else:
            pixles += "."

        sprite = "".join(["." for _ in range(40)])
        sprite = sprite[:value-1] + "###" + sprite[value+1:]
        print(sprite)
        print(pixles)

def get_instructions(filename):
    with open(filename, "r") as f:
        return f.read().splitlines()

if __name__ == "__main__":
    instructions = get_instructions("sample_input.txt")
    cycle_values, signal_strength = execute_instructions(instructions)
    print(signal_strength)
    assert signal_strength == 13140
    #assert signal_strength == 15680

    draw_sprite(cycle_values)