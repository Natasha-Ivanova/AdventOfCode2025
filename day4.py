# https://adventofcode.com/2025/day/4

def part1(layout, locations):
    total = 0
    for pos in locations:
        current_surrounding = 0
        surrounding = [-1j, 1j, 1-1j, -1-1j, 1+1j, -1+1j, -1, 1]
        for val in surrounding:
            if pos+val in layout:
                if layout[pos+val] == "@":
                    current_surrounding+=1
        if current_surrounding < 4:
            total+=1
    return total

def part2(layout, to_check):
    total = 0
    while to_check:
        pos = to_check.pop(0)
        if layout[pos] == "@":
            current_surrounding = 0
            surrounding = [-1j, 1j, 1 - 1j, -1 - 1j, 1 + 1j, -1 + 1j, -1, 1]
            for val in surrounding:
                if pos + val in layout:
                    if layout[pos + val] == "@":
                        current_surrounding += 1
            if current_surrounding < 4:
                total += 1
                layout[pos] = "."
                for val in surrounding:
                    if pos + val in layout:
                        if layout[pos+val] == "@":
                            to_check.append(pos+val)
    return total






with open("data/day4.txt") as f:
    rolls = []
    layout = {}
    for i, line in enumerate(f.readlines()):
        for k, v in enumerate(line):
            if v == "@":
                rolls.append(i+k*1j)
            layout[i+k*1j] = v

print("Part 1: "+str(part1(layout, rolls)))
print("Part 2: "+str(part2(layout, rolls)))


