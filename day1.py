# https://adventofcode.com/2025/day/1

directions = {"R": 1, "L": -1}
with open("data/day1.txt") as f:
    current = 50
    p1res = 0
    p2res = 0

    for line in f.readlines():
        line = line.strip()

        direction = line[0]
        amount = int(line[1:])
        # for every instruction, perform each tick manually and check if it's 0 at the current point
        for i in range(amount):
            current += directions[direction]
            current = current % 100
            if current == 0:
                p2res += 1
        if current == 0:
            p1res += 1
    print("Part 1: " + str(p1res))
    print("Part 2: " + str(p2res))
