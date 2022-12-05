from pathlib import Path
from itertools import chain

def part1(input_values):
    # create dictionaries of priorities
    lowercase_prios = {chr(i+96):i for i in range(1,27)}
    uppercase_prios = {chr(i+38):i for i in range(27,53)}
    
    # concatenate dictionaries
    prio_list = dict(chain.from_iterable(d.items() for d in (lowercase_prios, uppercase_prios)))

    # get items for each compartment    
    pairs = get_item_pairs(input_values)
    
    # look for items that appears in both compartments
    total_score = 0
    for pair in pairs:
        # remove duplicated chars
        item1 = "".join(dict.fromkeys(pair[0]))
        item2 = "".join(dict.fromkeys(pair[1]))
        for char in item1:
            if char in item2:
                # lookup prio for current item
                score = prio_list[char]
                total_score += score
    
    print(total_score)

# create a list of items that goes in to each compartment
def get_item_pairs(input_values):
    items = []
    for line in input_values:
        item_length = int(len(line) / 2)
        item1 = line[:item_length]
        item2 = line[item_length:]
        items.append([item1, item2])
    return items

def get_input(filename):
    with open(filename, "r") as f:
        return f.read().split("\n")

if __name__ == "__main__":
    part1(get_input("input.txt"))