# https://adventofcode.com/2025/day/3

def part1(banks):
    res = 0
    for bank in banks:
        intBank = [int(i) for i in list(bank)]
        tens = max(intBank)
        tensIndex = intBank.index(tens)
        if tensIndex == len(intBank) - 1:
            tens = max(intBank[:-1])
            tensIndex = intBank.index(tens)
        ones = max(intBank[tensIndex + 1:])
        # print(tens*10+ones)
        res += tens * 10 + ones
    return res


with (open("data/day3test.txt") as f):
    lines = [line.strip() for line in f.readlines()]

print("Part 1: "+str(part1(lines)))