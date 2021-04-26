def solution(participant, completion):
    dic = {}
    for x in participant:
        dic[x] = dic.get(x, 0) + 1
    for x in completion:
        dic[x] -= 1

    result = [i for i, j in dic.items() if j > 0]
    answer = result[0]

    return answer
