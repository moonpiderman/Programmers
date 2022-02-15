def solution(participant, completion):
    answer = ""
    dic = {}

    for par in participant:
        if par not in dic.keys():
            dic[par] = 1
        else:
            dic[par] += 1

    for com in completion:
        if com in dic.keys():
            dic[com] -= 1

    for key, val in dic.items():
        if val > 0:
            answer = key
            break

    return answer

if __name__ == '__main__':
    participants = [
        ["leo", "kiki", "eden"],
        ["marina", "josipa", "nikola", "vinko", "filipa"],
        ["mislav", "stanko", "mislav", "ana"]
    ]

    completions = [
        ["eden", "kiki"],
        ["josipa", "filipa", "marina", "nikola"],
        ["stanko", "ana", "mislav"]
    ]

    for i in range(len(participants)):
        print(solution(participants[i], completions[i]))
