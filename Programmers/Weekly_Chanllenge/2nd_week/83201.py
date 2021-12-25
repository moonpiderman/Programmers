def ave(total):
    if total >= 90:
        return 'A'
    elif total >= 80 and total < 90:
        return 'B'
    elif total >= 70 and total < 80:
        return 'C'
    elif total >= 50 and total < 70:
        return 'D'
    else:
        return 'F'

def solution(scores):
    answer = ''
    row = len(scores) # 자신이 준 점수
    col = len(scores[0]) # 자신이 받은 점수

    # 열을 기준으로 체크하기
    # 해당 학생의 평균값을 내기 위함.

    for c in range(col):
        count = row
        total = [] # 점수의 총합
        for r in range(row):
            total.append(scores[r][c])
        mini = min(total)
        mani = max(total)
        chk = sum(total)
        # 유일한 최고점, 유일한 최저점 체크
        if scores[c][c] == mini or scores[c][c] == mani:
            if scores[c][c] == mini:
                if total.count(mini) == 1:
                    chk -= mini
                    count -= 1
            else:
                if total.count(mani) == 1:
                    chk -= mani
                    count -= 1

        result = chk / count
        answer += ave(result)

    return answer

if __name__ == '__main__':
    scores_1 = [
        [100, 90, 98, 88, 65],
        [50, 45, 99, 85, 77],
        [47, 88, 95, 80, 67],
        [61, 57, 100, 80, 65],
        [24, 90, 94, 75, 65]
    ]

    scores_2 = [
        [50, 90],
        [50, 87]
    ]

    scores_3 = [
        [70, 49, 90],
        [68, 50, 38],
        [73, 31, 100]
    ]

    print(solution(scores_1))
    print(solution(scores_2))
    print(solution(scores_3))