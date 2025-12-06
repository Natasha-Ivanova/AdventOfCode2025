# https://adventofcode.com/2025/day/6

def part1(lines):
    ops = lines.pop().split()
    problems = [[int(i) for i in line.split()] for line in lines]
    problems = [[problems[i][j] for i in range(len(problems))] for j in
                range(len(problems[0]))] # swap rows and columns
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
    problems = [[lines[i][j] for i in range(len(lines))] for j in
                range(len(lines[0]))][::-1]
    res = 0
    temp_sum = 0
    temp_mul = 1
    for problem in problems:
        current = "".join(problem[:-1]).replace(" ", "")
        if current != "":
            current = int(current)
            temp_sum+=current
            temp_mul*=current
        op = problem[-1]
        if op == "+":
            res += temp_sum
            temp_sum = 0
            temp_mul = 1
        elif op == "*":
            res += temp_mul
            temp_sum = 0
            temp_mul = 1
    return res


with open("data/day6.txt") as f:
    lines = [line[:-1] for line in f.readlines()]

print("Part 1: "+str(part1(lines.copy())))
print("Part 2: "+str(part2(lines)))