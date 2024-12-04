import re

with open("3.in", "r") as file:
    data = file.read().splitlines()
    total = 0
    do = True

    for i in data:
        matches = re.findall(r"(mul\((\d+),(\d+)\)|do\(\)|don't\(\))", i)
        for j in matches:
            if j[0] == "do()":
                do = True
            elif j[0] == "don't()":
                do = False
            elif j[0].startswith("mul"):
                if do:
                    total += int(j[1]) * int(j[2])


    print(total)