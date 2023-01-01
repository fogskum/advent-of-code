from pathlib import Path

cycles = 0
signal_strengths = []

def add_cycle(register_value):
    global cycles 
    cycles += 1
    if cycles % 40 == 20:
        signal_strengths.append( cycles * register_value )

def execute_instructions(instructions):
    register_value = 1

    for instruction in instructions:
        if cycles > 220:
            break

        if instruction == "noop":
            add_cycle(register_value)
        else:
            if instruction.split()[0] == "addx":
                add_cycle(register_value)
                add_cycle(register_value)
                value = int(instruction.split()[1])
                register_value += value
            
    return sum(signal_strengths)

def get_instructions(filename):
    with open(filename, "r") as f:
        return f.read().splitlines()

if __name__ == "__main__":
    instructions = get_instructions("input.txt")
    part1_result = execute_instructions(instructions)
    print(part1_result)
    #assert part1_result == 13140
    assert part1_result == 15680
