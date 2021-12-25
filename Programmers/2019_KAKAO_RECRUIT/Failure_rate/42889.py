def solution(N, stages):
    answer = [] # 실패율 저장
    stack = []
    dic = {}
    ppl = len(stages)

    fuck = [0 for r in range(N)]

    # N보다 높은 영역 삭제
    for s in stages :
        if s <= N :
            stack.append(s)

    # key: stage 번호, value: 해당 스테이지를 넘지 못한 유저 수
    for i in range(1, N + 1) :
        if ppl == 0 :
            dic[i] = 0
        else :
            fuck[i-1] = stack.count(i)
            dic[i] = fuck[i-1]
            tmp = ppl
            ppl -= dic[i]
            dic[i] = dic[i] / tmp

    real = sorted(dic.items(), reverse=True, key=lambda item: item[1])

    for i in range(len(real)) :
        answer.append(real[i][0])
    return answer


if __name__ == '__main__' :
    N_1 = 5
    stages_1 = [2, 1, 2, 6, 2, 4, 3, 3]
    N_2 = 4
    stages_2 = [4, 4, 4, 4, 4]

    print(solution(N_1, stages_1))
    # print(solution(N_2, stages_2))