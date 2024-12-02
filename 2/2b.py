with open('2.in', 'r') as file:
    data = file.read().splitlines()
    safe = 0
    for i in data:
        levels = i.split()
        levels = [int(i) for i in levels]
        for j in range(len(levels)):
            temp = levels.copy()
            temp.pop(j)
            increasing = all(temp[i] < temp[i + 1] for i in range(len(temp) - 1))
            decreasing = all(temp[i] > temp[i + 1] for i in range(len(temp) - 1))
            if increasing or decreasing:
                if all(abs(temp[i] - temp[i + 1]) >= 1 and abs(temp[i] - temp[i + 1]) <= 3 for i in range(len(temp) - 1)):
                    safe += 1
                    break
    print(safe)