# https://adventofcode.com/2025/day/5

def part1(lines):
    ranges = []
    res = 0
    line = lines.pop(0)
    while line != "":
        ranges.append([int(i) for i in line.split("-")])
        line = lines.pop(0)

    for id in lines:
        id = int(id)
        for range in ranges:
            if range[0] <= id <= range[1]:
                res+=1
                break

    return res





with (open("data/day5.txt") as f):
    lines = [line.strip() for line in f.readlines()]

print("Part 1: "+str(part1(lines)))