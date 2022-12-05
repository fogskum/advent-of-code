from pathlib import Path
from itertools import chain

# create dictionaries of priority scores based on ASCII table
lowercase_prios = {chr(i+96):i for i in range(1,27)}
uppercase_prios = {chr(i+38):i for i in range(27,53)}

# concatenate dictionaries
prio_dict = dict(chain.from_iterable(d.items() for d in (lowercase_prios, uppercase_prios)))

# correct=2697
def part2(input_values):
    count = len(input_values)
    page_size = 3
    pages = int(count / 3)
    score = 0

    for page in range(0, pages):
        start = (page) * page_size
        end = start + page_size
        group = input_values[start:end]
        score += calc_score(group)

    return score

# correct answer=7737
def part1(input_values):
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
                score = prio_dict[char]
                total_score += score
    
    return total_score

def calc_score(group):
    score = 0

    # remove duplicated chars
    base_item = "".join(dict.fromkeys(group[0]))
    other_items = group[1:]
    for char in base_item:
        # keep track of number of hits
        hit_count = 0
        for other_item in other_items:
            local_item = "".join(dict.fromkeys(other_item))
            if char in local_item:
                # lookup prio for current item
                hit_count += 1
                if hit_count == 2:
                    score += prio_dict[char]
    
    return score

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
    input_values = get_input("input.txt")
    
    part1_result = part1(input_values)
    print(int(part1_result))

    part2_result = part2(input_values)
    print(int(part2_result))