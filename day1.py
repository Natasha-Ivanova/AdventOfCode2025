# https://adventofcode.com/2025/day/1

directions = {"R": 1, "L": -1}
with open("data/day1.txt") as f:
    pointer = 50  # where the pointer currently is
    p1res = 0
    p2res = 0

    for line in f.readlines():
        line = line.strip()

        direction = directions[line[0]]
        clicks = int(line[1:])
        p2res += clicks // 100
        clicks = clicks % 100
        pointer += clicks*direction

        if pointer % 100 == 0:
            p1res += 1
        if pointer == 0:
            p2res += 1
        elif pointer < 0:  # passed 0 on a left turn
            if clicks + pointer != 0: # check that pointer wasn't on 0 before turn
                p2res += 1
            pointer = 100 + pointer
        elif pointer >= 100: # passed 0 on a right turn
            p2res += 1
            pointer = pointer - 100


    print("Part 1: " + str(p1res))
    print("Part 2: " + str(p2res))
