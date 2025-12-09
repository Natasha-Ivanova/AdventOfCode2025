# https://adventofcode.com/2025/day/9

def part1(lines):
    max_rect = 0
    for i, corner in enumerate(lines):
        for corner_2 in lines[i+1:]:
            max_rect = max(max_rect, 
                           (abs(corner[0]-corner_2[0])+1)*
                           (abs(corner[1] - corner_2[1]) + 1)) 
    return max_rect


def part2(lines):
    pass


with open("data/day9.txt") as f:
    lines = [[int(i) for i in line.split(",")] for line in f.readlines()]

print("Part 1: " + str(part1(lines)))
print("Part 2: " + str(part2(lines)))