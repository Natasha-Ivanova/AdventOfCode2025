# https://adventofcode.com/2025/day/11
from functools import cache

def pathCount(connections, visited, current, end):
    if current == end:
        return 1
    else:
        visited = visited.copy()
        visited.add(current)
        res = 0
        if current in connections.keys():
            for connection in connections[current]:
                if connection not in visited: 
                    res += pathCount(connections, visited, connection, end)
        return res                   
                   
@cache
def pathCount2(current, dac, fft):
    if current == "out":
        return int(dac and fft)
    else:    
        if current == "dac":
            dac = True
        elif current == "fft":
            fft = True
        res = 0
        for connection in lines[current]:
                res += pathCount2(connection, dac, fft)  
        return res

def part1(connections):
    return pathCount(connections, set(), "you", "out")


def part2():
    return pathCount2("svr", False, False)


with open("data/day11.txt") as f:
    lines = {a.split(": ")[0]:a.split(": ")[1].split() for a in f.readlines()}


print("Part 1: " + str(part1(lines)))
print("Part 2: " + str(part2()))