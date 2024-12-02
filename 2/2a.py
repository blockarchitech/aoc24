with open('2.in', 'r') as file:
    data = file.read().splitlines()
    safe = 0
    for i in data:
        levels = i.split()
        levels = [int(i) for i in levels]
        increasing = all(levels[i] < levels[i + 1] for i in range(len(levels) - 1))
        decreasing = all(levels[i] > levels[i + 1] for i in range(len(levels) - 1))
        if increasing or decreasing:
            if all(abs(levels[i] - levels[i + 1]) >= 1 and abs(levels[i] - levels[i + 1]) <= 3 for i in range(len(levels) - 1)):
                safe += 1

    print(safe)
    