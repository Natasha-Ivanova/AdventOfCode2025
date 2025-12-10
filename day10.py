# https://adventofcode.com/2025/day/10
import itertools
from functools import reduce
import z3

def getMinButtons(state, buttons):
    state = sum([2**i  if k=='#' else 0 for i,k in enumerate(state)])
    for size in range(1, len(buttons) + 1):
        for subset in itertools.combinations(buttons, size):
            temp_states = [sum([2**i  for i in val]) for val in subset]
            c_state = reduce(lambda i, j: int(i) ^ int(j), temp_states)
            if c_state == state:
                return size


def part1(states, buttons):
    res = 0
    for i, state in enumerate(states):
        res+=getMinButtons(state, buttons[i])
    return res
    


def part2(buttons, joltages):
    res = 0
    for i, button_set in enumerate(buttons):
        joltage = joltages[i]
        m = [[j in b for b in button_set] for j in range(len(joltage))]
        c = [1] * len(button_set)
        z = z3.Optimize()
        vars = [z3.Int(f'x{i}') for i in range(len(button_set))]
        for i in range(len(button_set)):
            z.add(vars[i] >=0)
        for i in range(len(joltage)):
            z.add(sum([vars[j] for j,b in enumerate(button_set) if i in b]) == joltage[i])
        
        z.minimize(sum(vars))
        assert z.check() == z3.sat
        
        m = z.model()
        for v in vars:
            res += m[v].as_long()
    return int(res)



with open("data/day10.txt") as f:
    states = []
    buttons = []
    joltages = []
    for line in f.readlines():
        line = line.strip().split("] ")
        states.append(line[0][1:])
        line = line[1][1:].split(") {")
        button = [[int(i) for i in l.split(",")] for l in line[0].split(") (")]
        buttons.append(button)
        joltages.append([int(i) for i in line[1][:-1].split(",")])
        

print("Part 1: " + str(part1(states, buttons)))
print("Part 2: " + str(part2(buttons, joltages)))