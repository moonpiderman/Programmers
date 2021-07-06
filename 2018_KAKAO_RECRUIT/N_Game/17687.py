def solution(n, t, m, p):

    # 재귀 함수를 활용한 진법 변환기
    def convert(n, base):
        arr = "0123456789ABCDEF"
        q, r = divmod(n, base)
        if q == 0:
            return arr[r]
        else:
            return convert(q, base) + arr[r]

    answer = ''
    cand = []

    # 전체
    for i in range(t * m) :
        con = convert(i, n)
        for c in con :
            cand.append(c)

    # 튜브만
    # p - 1 인 이유는 index는 0부터 시작
    for i in range(p - 1, t * m, m):
        answer += cand[i]

    return answer

if __name__ == '__main__' :
    n_1 = 2
    t_1 = 4
    m_1 = 2
    p_1 = 1

    n_2 = 16
    t_2 = 16
    m_2 = 2
    p_2 = 1

    n_3 = 16
    t_3 = 16
    m_3 = 2
    p_3 = 2

    print(solution(n_1, t_1, m_1, p_1))
    print(solution(n_2, t_2, m_2, p_2))
    print(solution(n_3, t_3, m_3, p_3))
