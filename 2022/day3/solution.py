from pathlib import Path

def part1(input_values):
    # create dictionaries of priorities
    lowercase_prios = [{chr(i+96):i} for i in range(1,27)]
    uppercase_prios = [{chr(i+38):i} for i in range(27,53)]
    prio_list = lowercase_prios + uppercase_prios

    # get items for each compartment    
    pairs = get_item_pairs(input_values)
    
    # look for items that appears in both compartments
    for pair in pairs:
        item1 = pair[0]
        item2 = pair[1]
        for char in item1:
            if char in item2:
                # lookup prio for current item
                prio = prio_list[char]

# create a list of items that goes in to each compartment
def get_item_pairs(input_values):
    items = []
    for line in input_values:
        item_length = int(len(line) / 2)
        item1 = line[:item_length]
        item2 = line[item_length:]
        items.append([item1, item2])
    return items

def get_input():
    with open("input.txt", "r") as f:
        return f.read().split("\n")

if __name__ == "__main__":
    part1(get_input())