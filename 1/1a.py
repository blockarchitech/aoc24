with open("1.in", "r") as file:
    data = file.read().splitlines()
    left = []
    right = []
    for i in data:
        left_id, right_id = i.split()
        left.append(left_id)
        right.append(right_id)
    left.sort()
    right.sort()
    
    total_distance = 0
    for i in range(len(left)):
        total_distance += abs(int(left[i]) - int(right[i]))
    print(total_distance)

