def solution(s):
    result = []
    answer = list(s)
    answer.sort(reverse=True)
    result = "".join(answer)
    return result
