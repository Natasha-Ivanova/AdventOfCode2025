# https://adventofcode.com/2025/day/3


def buildJoltage(bank, size):
    if size > 1:
        current = max(bank[:-(size-1)])
        currentIndex = bank.index(current)
        return current*10**(size-1) +buildJoltage(bank[currentIndex+1:], size-1)
    else:
        return max(bank)

def part1(banks):
    res = 0
    for bank in banks:
        intBank = [int(i) for i in list(bank)]
        res += buildJoltage(intBank, 2)
    return res

def part2(banks):
    res = 0
    for bank in banks:
        intBank = [int(i) for i in list(bank)]
        currentRes = buildJoltage(intBank, 12)
        res+=currentRes
    return res


with (open("data/day3.txt") as f):
    lines = [line.strip() for line in f.readlines()]

print("Part 1: "+str(part1(lines)))
print("Part 2: "+str(part2(lines)))