import re

with open("3.in", "r") as file:
    data = file.read().splitlines()
    total = 0
    for i in data:
        matches = re.findall(r"mul\((\d+),(\d+)\)", i)
        for j in matches:
            total += int(j[0]) * int(j[1])
    print(total)