# https://adventofcode.com/2025/day/5
import random


def part1(lines):
    ranges = []
    res = 0
    line = lines.pop(0)
    while line != "":
        ranges.append([int(i) for i in line.split("-")])
        line = lines.pop(0)

    for id in lines:
        id = int(id)
        for current_range in ranges:
            if current_range[0] <= id <= current_range[1]:
                res+=1
                break

    return res

def part2(lines):
    ranges = []
    res = 0
    line = lines.pop(0)
    while line != "":
        c_range = [int(i) for i in line.split("-")]
        temp = [c_range]

        for current_range in ranges:
            c_low = c_range[0] #low in range we are checking
            c_high = c_range[1] #high in range we are checking
            low = current_range[0] #low in pre-existing ranges
            high = current_range[1] #high in pre_existing ranges
            if not c_high< low and not high < c_low: # exists some overlap between the pre-existing range and the current range
                temp.append(current_range)
        ranges.append(c_range)

        if len(temp) != 1: # condense all overlapping ranges
            c_low = temp[0][0]
            c_high = temp[0][1]
            for c_range in temp:
                ranges.remove(c_range)
                if c_range[0] < c_low:
                    c_low = c_range[0]
                if c_range[1] > c_high:
                    c_high = c_range[1]
            ranges.append([c_low, c_high])


        line = lines.pop(0)
    for c_range in ranges:
        res += c_range[1]-c_range[0]+1
    return res



with (open("data/day5.txt") as f):
    lines = [line.strip() for line in f.readlines()]

print("Part 1: "+str(part1(lines.copy())))
print("Part 2: "+str(part2(lines.copy())))