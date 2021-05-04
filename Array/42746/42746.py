def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)

    return str(int(''.join(numbers)))


# a = [3, 30, 34, 5, 9]
a = [3, 30, 911, 96, 34, 622, 90, 856, 546, 9]

print(solution(a))
