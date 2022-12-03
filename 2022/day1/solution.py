from pathlib import Path

def part1():
    with open("input.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            if line.strip():
                print(int(line))
        #all_elves = f.read().split('\n\n')
        #each_elf = [[int(x) for x in elf.split("\n")] for elf in all_elves]
        #print("" + str(sum(elf) for elf in each_elf))

if __name__ == "__main__":
    part1()