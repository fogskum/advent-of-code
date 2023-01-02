from pathlib import Path

cycles = 0

def add_cycle(signal_strengths, register_value):
    global cycles 
    cycles += 1
    if cycles % 40 == 20:
        signal_strengths.append( cycles * register_value )

def compute_signal_strength(instructions):
    signal_strengths = []
    register_value = 1

    for instruction in instructions:
        if cycles > 220:
            break

        if instruction == "noop":
            add_cycle(signal_strengths, register_value)
        else:
            if instruction.split()[0] == "addx":
                add_cycle(signal_strengths, register_value)
                add_cycle(signal_strengths, register_value)
                value = int(instruction.split()[1])
                register_value += value
            
    return sum(signal_strengths)

def part1(instructions):
    return compute_signal_strength(instructions)

def part2(instructions):
    pass

def get_instructions(filename):
    with open(filename, "r") as f:
        return f.read().splitlines()

if __name__ == "__main__":
    instructions = get_instructions("input.txt")
    part1_result = part1(instructions)
    print(part1_result)
    #assert part1_result == 13140
    assert part1_result == 15680