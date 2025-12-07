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
    


def timeline_counter(lines, p_index, c_index):
    while(c_index < len(lines) and p_index not in lines[c_index]):
        c_index+=1
    if c_index == len(lines):
        return 1
    c_index+=1
    if p_index+1j*c_index not in results.keys():
        res = timeline_counter(lines, p_index+1, c_index) + timeline_counter(lines, p_index-1, c_index)
        results[p_index+1j*c_index] = res
        return res
    else:
        return results[p_index+1j*c_index]
    
results = dict()
def part2(lines, s_index):
    return timeline_counter(lines, s_index, 0)



with open("data/day7.txt") as f:
    s = f.readline().index("S")
    lines = [[i for i, c in enumerate(line.strip()) if c == "^"] for line in f.readlines()]

print("Part 1: "+str(part1(lines, s)))
print("Part 2: "+str(part2(lines, s)))