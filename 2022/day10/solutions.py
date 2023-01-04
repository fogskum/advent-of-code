def execute_instructions(instructions):
    # initial register value
    cycle_value = 1
    cycle_values = [cycle_value]
    for instruction in instructions:
        if instruction == "noop":
            # add the last value in list
            cycle_values.append( cycle_values[-1] )
            continue

        if instruction.split()[0] == "addx":
            cycle_values.append(cycle_values[-1])
            cycle_value = int(instruction.split()[1])
            cycle_values.append(cycle_values[-1] + cycle_value)
    
    # sum the signal strength every 40th cycle, starting at 20
    signal_strength = sum([value * cycle_values[value-1] for value in range(20, 240, 40)])
    return cycle_values, signal_strength

def draw_sprite(cycle_values):
    pixles = ""
    for cycle, cycle_value in enumerate(cycle_values):
        if cycle == 240:
            break

        sprite = "".join(["." for _ in range(39)])
        sprite = sprite[:cycle_value-1] + "###" + sprite[cycle_value+1:]
        print(sprite)
           
        print("Start cycle {}".format(cycle+1))
        # create range window where cycle value is in the middle
        pixel_range = range( (cycle % 40) - 1, (cycle % 40) + 2)
        if cycle_value in pixel_range:
            pixles += "#"
        else:
            pixles += "."

        if (cycle+1) % 40 == 0:
            pixles += "\n"

        print(pixles)

def get_instructions(filename):
    with open(filename, "r") as f:
        return f.read().splitlines()

if __name__ == "__main__":
    instructions = get_instructions("input.txt")
    cycle_values, signal_strength = execute_instructions(instructions)
    print(signal_strength)
    #assert signal_strength == 13140
    assert signal_strength == 15680

    draw_sprite(cycle_values)