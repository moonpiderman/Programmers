from itertools import permutations

def solution(numbers):
    answer = []
    tu_list = list(permutations(numbers, 2))

    for i in range(len(tu_list)) :
        answer.append(tu_list[i][0] + tu_list[i][1])

    answer = list(set(answer))
    answer.sort()

    return answer

if __name__ == '__main__' :
    numbers_1 = [2, 1, 3, 4, 1]
    numbers_2 = [5, 0, 2, 7]

    print(solution(numbers_1))