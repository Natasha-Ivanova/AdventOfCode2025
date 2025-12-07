# https://adventofcode.com/2025/day/7


def part1(lines, s_index):
    current_lines = {s_index}
    count = 0
    for line in lines:
        for splitter in line:
            if splitter in current_lines:
                current_lines.remove(splitter)
                current_lines.add(splitter-1)
                current_lines.add(splitter+1)
                count+=1
        #print(current_lines)
    return count
    



def part2(lines):
    pass



with open("data/day7.txt") as f:
    s = f.readline().index("S")
    lines = [[i for i, c in enumerate(line.strip()) if c == "^"] for line in f.readlines()]

print("Part 1: "+str(part1(lines, s)))
print("Part 2: "+str(part2(lines)))