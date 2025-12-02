# https://adventofcode.com/2025/day/2

def checkDouble(n):
    string = str(n)
    if len(string) % 2 == 0:
        half = string[0:len(string) // 2]
    else:
        return False
    return half * 2 == string


def checkRepeats(n):
    string = str(n)
    if (len(string)) == 1:
        return False
    for i in range(2, len(string) // 2 + 1):
        if len(string) % i == 0:
            segment = string[0:len(string) // i]
            if segment * i == string:
                return True
    return string[0] * len(string) == string


def part1(ranges):
    total = 0
    for ids in ranges:
        ids = ids.split("-")
        first = int(ids[0])
        last = int(ids[1])
        for i in range(first, last + 1):
            if checkDouble(i):
                total += i
    return total


def part2(ranges):
    total = 0
    for ids in ranges:
        ids = ids.split("-")
        first = int(ids[0])
        last = int(ids[1])
        for i in range(first, last + 1):
            if checkRepeats(i):
                total += i
    return total


with open("data/day2.txt") as f:
    line = f.readline().strip()

idRanges = line.split(",")
print("Part 1: " + str(part1(idRanges)))
print("Part 2: " + str(part2(idRanges)))
