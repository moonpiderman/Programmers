from itertools import permutations


def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
        else:
            return True


def solution(numbers):
    sep = [r for r in numbers]
    total = []
    answer = 0

    for i in range(1, len(sep) + 1):
        total.append(list(map(''.join, permutations(sep, i))))

    q = list(map(int, sum(total, [])))
    q = list(set(q))
    for i in q:
        if is_prime(i) == True:
            answer += 1
    return answer


# numbers = "17"
numbers = "011"
sep = [r for r in numbers]
total = []
result = []

for i in range(1, len(sep) + 1):
    # 순열들을 total 리스트에 나열해주기
    total.append(list(map(''.join, permutations(sep, i))))

# 2차원 리스트 이어붙여주고, 모두 int 형으로 형 변환
q = list(map(int, sum(total, [])))
# 중복 제거
q = list(set(q))

for i in q:
    if is_prime(i) == True:
        result.append(i)
