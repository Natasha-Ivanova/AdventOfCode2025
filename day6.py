# https://adventofcode.com/2025/day/6

def part1(lines):
    ops = lines.pop().split()
    problems = [[int(i) for i in line.split()] for line in lines]
    problems = [[problems[i][j] for i in range(len(problems))] for j in range(len(problems[0]))] # swap rows and columns
    res = 0
    for i, problem in enumerate(problems):
        op = ops[i]
        if op == "+":
            res += sum(problem)
        else:
            temp = 1
            for n in problem:
                temp*=n
            res+=temp
    return res

def part2(lines):
    pass


with open("data/day6.txt") as f:
    lines = [line.strip() for line in f.readlines()]

print("Part 1: "+str(part1(lines)))
print("Part 2: "+str(part2(lines)))