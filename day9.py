# https://adventofcode.com/2025/day/9
from shapely import Polygon
from shapely import box

def part1(lines):
    max_rect = 0
    for i, corner in enumerate(lines):
        for corner_2 in lines[i+1:]:
            max_rect = max(max_rect, 
                           (abs(corner[0]-corner_2[0])+1)*
                           (abs(corner[1] - corner_2[1]) + 1)) 
    return max_rect

def part2(lines):
    outer = Polygon(list(zip([line[0] for line in lines], [line[1] for line in lines])))
    max_rect = 0
    for i, corner in enumerate(lines):
        for corner_2 in lines[i+1:]:
            inner = box(min(corner[0], corner_2[0]), min(corner[1], corner_2[1]), max(corner[0], corner_2[0]), max(corner[1], corner_2[1]))
            if outer.covers(inner):
                max_rect = max(max_rect, 
                               (abs(corner[0]-corner_2[0])+1)*
                               (abs(corner[1] - corner_2[1]) + 1)) 
    return max_rect

        
with open("data/day9.txt") as f:
    lines = [[int(i) for i in line.split(",")] for line in f.readlines()]

print("Part 1: " + str(part1(lines)))
print("Part 2: " + str(part2(lines)))