def solution_1(array, commands):
    answer = []

    for com in commands:
        i = com[0] - 1
        j = com[1] - 1
        k = com[2] - 1

        tmp = sorted((array[i:j + 1]))
        answer.append(tmp[k])

    return answer

def solution(array, commands):
    answer = []

    for com in commands:
        tmp = array[com[0] - 1: com[1]]
        tmp = sorted(tmp)
        answer.append(tmp[com[2] - 1])

    return answer

if __name__ == '__main__':
    arr = [1, 5, 2, 6, 3, 7, 4]
    com = [
        [2, 5, 3],
        [4, 4, 1],
        [1, 7, 3]
    ]

    print(solution(arr, com))
