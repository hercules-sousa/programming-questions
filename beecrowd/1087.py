entry = input()

while entry != "0 0 0 0":
    entry = list(map(int, entry.split(" ")))
    x1 = entry[0]
    y1 = entry[1]
    x2 = entry[2]
    y2 = entry[3]
    answer = 0

    if x1 == x2 and y1 == y2:
        answer = 0
    elif x1 == x2 or y1 == y2:
        answer = 1
    elif abs(x1 - x2) == abs(y1 - y2):
        answer = 1
    else:
        answer = 2

    print(answer)
    entry = input()
