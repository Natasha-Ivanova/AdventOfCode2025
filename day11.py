# https://adventofcode.com/2025/day/11

def pathCount(connections, visited, current):
    if current == "out":
        return 1
    else:
        visited = visited.copy()
        visited.add(current)
        res = 0
        for connection in connections[current]:
            if connection not in visited: 
                res += pathCount(connections, visited, connection)
        return res
                
            
    

def part1(connections):
    return pathCount(connections, set(), "you")


def part2(connections):
    pass


with open("data/day11.txt") as f:
    lines = {a.split(": ")[0]:a.split(": ")[1].split() for a in f.readlines()}


print("Part 1: " + str(part1(lines)))
print("Part 2: " + str(part2(lines)))