from itertools import combinations
import math

def prime(number) :
    for i in range(2, int(math.sqrt(number)) + 1) :
        if number % i == 0 :
            return 0
    return 1

def solution(nums):
    answer = 0
    result = []
    nums = list(set(nums))
    com = list(combinations(nums, 3))

    for i in range(len(com)) :
        result.append(sum(com[i]))

    for j in result :
        if prime(j) == 1 :
            answer += 1

    return answer

if __name__ == '__main__' :
    nums_1 = [1, 2, 3, 4]
    nums_2 = [1, 2, 7, 6, 4]

    print(solution(nums_1))