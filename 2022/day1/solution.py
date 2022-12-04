from pathlib import Path


def get_sum_calories() -> list[int]:
    with open("input.txt", "r") as f:
        # read calories and split by two line breaks
        elves = f.read().split("\n\n")
        # create matrix of each elvs calories
        each_elf = [[int(item) for item in elf.split("\n")] for elf in elves]
        # create new list of each elf's total calories
        sum_list = [sum(elf) for elf in each_elf]
        return sum_list


if __name__ == "__main__":
    sum_calories = get_sum_calories()
    # part 1: get max value
    max_calories = max(sum_calories)
    print(max_calories)

    # part 2: get sum of top 3
    sorted_calories = sorted(sum_calories)
    top_list = [sorted_calories[-1], sorted_calories[-2], sorted_calories[-3]]
    print(sum(top_list))
