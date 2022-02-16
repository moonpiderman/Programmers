def solution(teamIDs, additional):
    answer = []

    for add in additional:
        if add not in teamIDs:
            teamIDs.append(add)
            answer.append(add)

    return answer

if __name__ == '__main__':
    teamIDs_1 = [
        "world", "prog"
    ]

    additional_1 = [
        "hello", "world", "code", "hello", "try", "code"
    ]

    teamIDs_2 = [
        "abc", "hq", "xyz"
    ]

    additional_2 = [
        "hq", "abc", "pp", "xy", "pp", "hq"
    ]

    print(solution(teamIDs_1, additional_1))
    print(solution(teamIDs_2, additional_2))
