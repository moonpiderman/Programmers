def solution(n, lost, reserve):
    answer = 0

    los = [l for l in lost if l not in reserve]
    res = [r for r in reserve if r not in lost]

    for r in res:
        if r-1 in los:
            los.remove(r-1)
        elif r+1 in los:
            los.remove(r+1)
    answer = n - len(los)

    return answer
