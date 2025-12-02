# https://adventofcode.com/2025/day/1

def checkDouble(n):
    string = str(n)
    if len(string) % 2 == 0:
        half = string[0:len(string) // 2]
    else:
       return False
    return half*2 == string

def part1(ranges):
    total = 0
    for ids in ranges:
        ids = ids.split("-")
        first = int(ids[0])
        last = int(ids[1])
        for i in range(first, last+1):
            if checkDouble(i):
                total+=i
    return total


with open("data/day2.txt") as f:
    line = f.readline().strip()

idRanges = line.split(",")
print("Part 1: "+str(part1(idRanges)))


