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
    
    similarity_score = 0
    for i in left:
        similarity_score += right.count(i) * int(i)

    print(similarity_score)
