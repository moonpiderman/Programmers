def solution(participant, completion):
    dic = {}
    for value in participant:
        dic[value] = dic.get(value, 0) + 1
    for value in completion:
        dic[value] -= 1

    result = [i for i, j in dic.items() if j > 0]
    answer = result[0]

    return answer
