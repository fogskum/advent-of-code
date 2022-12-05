from pathlib import Path

def part2(input_values):
    return sum([1 for r in get_ranges(input_values) if range_overlaps(r[0], r[1])])

def part1(input_values):
    return sum([1 for r in get_ranges(input_values) if range_contains(r[0], r[1])])

# returns a list of section ranges tuples for the two elves
def get_ranges(input_values):
    pairs = [pair.split(',') for pair in input_values]
    range_list = []
    for pair in pairs:
        start_section1 = int(pair[0].split('-')[0])
        end_section1 = int(pair[0].split('-')[1]) + 1
        section_range1 = range(start_section1, end_section1)
        
        start_section2 = int(pair[1].split('-')[0])
        end_section2 = int(pair[1].split('-')[1]) + 1
        section_range2 = range(start_section2, end_section2)

        # pick the smallest range
        if len(section_range1) > len(section_range2):
            temp_range = section_range1
            section_range1 = section_range2
            section_range2 = temp_range
        
        range_list.append((section_range1, section_range2))
    
    return range_list

def range_contains(range1, range2):
    return range1.start in range2 and range1[-1] in range2

def range_overlaps(range1, range2):
    overlap_list = list(set(range1) & set(range2))
    return len(overlap_list) > 0

def get_input(filename):
    with open(filename, "r") as f:
        return f.read().split("\n")

if __name__ == "__main__":
    input_values = get_input("input.txt")
    
    part1_result = part1(input_values)
    assert part1_result == 503 

    part2_result = part2(input_values)
    assert part2_result == 827
