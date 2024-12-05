with open("4.in", "r") as file:
    patterns = ["MMSS", "SMSM", "MSMS", "SSMM"]
    offsets = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

    data = file.read().splitlines()
    xm = 1
    ym = 1
    xx = len(data[0]) - 1
    yx = len(data) - 1

    count = 0
    for y in range(ym, yx):
        for x in range(xm, xx):
            if data[y][x] == "A": # 100% admit: I stole this from reddit. everything gets destroyed if I don't have this, and I have no idea why
                surrounding = "".join(data[y + dy][x + dx] for dx, dy in offsets)
                if surrounding in patterns:
                    count += 1

    print(count)
