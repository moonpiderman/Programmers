from itertools import permutations
import math


def is_prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def is_prime_2(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def solution(numbers):
    sep = [r for r in numbers]
    total = []
    answer = 0

    for i in range(1, len(sep) + 1):
        # 순열들을 total 리스트에 나열해주기
        total.append(list(map(''.join, permutations(sep, i))))

    # 2차원 리스트 이어붙여주고, 모두 int 형으로 형 변환
    q = list(map(int, sum(total, [])))
    # 중복 제거
    q = list(set(q))
    for i in q:
        if is_prime(i) == True:
            answer += 1
    return answer
