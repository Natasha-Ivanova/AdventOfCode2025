# https://adventofcode.com/2025/day/12

def part1(lines):
    squares = []
    sizes = []
    res = 0
    for i in range(6):
        temp = []
        size = 0
        lines.pop(0)
        for j in range(3):
            l = lines.pop(0)
            temp.append(l)
            size += l.count("#")
        lines.pop(0)
        squares.append(temp)
        sizes.append(size)
    for line in lines:
        line = line.split(": ")
        dimensions = [int(i) for i in line[0].split("x")]
        count = [int(i) for i in line[1].split()]
        max_size = dimensions[0]*dimensions[1]
        size = 0
        for i, j in enumerate(count):
            size += j*sizes[i]
        if size <= max_size:
            res+=1
    return res
            
with open("data/day12.txt") as f:
    lines = [line.strip() for line in f.readlines()]

print("Part 1: " + str(part1(lines.copy())))