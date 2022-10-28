import math


n = int(input())


def is_prime(n):
    if n <= 1:
        return False
    if n % 2 == 0:
        return n == 2

    max_div = math.floor(math.sqrt(n))
    for i in range(3, 1 + max_div, 2):
        if n % i == 0:
            return False
    return True

# def is_prime(n):
#     if n == 2 or n == 3:
#         return True
#     if n % 2 == 0:
#         return False
#     for i in range(3, n // 2):
#         if n % i == 0:
#             return False
#     return True


while n != 0:
    people = list()

    for i in range(1, n + 1):
        people.append(i)

    pos = 0
    skip_num = 1
    last_prime = -1
    while len(people) > 1:
        pos += 1
        skip_num += 1
        if pos == len(people):
            pos = 0
        if is_prime(skip_num) and skip_num > last_prime:
            people.remove(people[pos])
            if pos == len(people):
                pos = 0
            last_prime = skip_num
            skip_num = 1

    print(*people)

    n = int(input())
