# 8퀸 문제 알고리즘 구현하기

pos = [0] * 8                               # 각 열에 배치한 퀸의 배치
flag_ch = [False] * 8                       # 각 행에 퀸을 배치했는지 체크
flag_le = [False] * 15                      # 좌상하 방향으로 퀸을 배치했는지 체크
flag_ri = [False] * 15                      # 우상하 방향으로 퀸을 배치했는지 체크

def put() -> None :
    """각 열에 배치한 퀸의 위치를 출력"""
    for i in range(8) :
        print(pos[i], end=' ')
    print()

def set(i: int) -> None :
    """i열의 알맞은 위치에 퀸을 배치"""
    for j in range(8) :
        if (not flag_ch[j]                  # j 행에 퀸이 배치되지 않았다면
        and not flag_le[i + j]              # 좌상하 방향에 퀸이 배치되지 않았다면
        and not flag_ri[i - j + 7]) :       # 우상하 방향에 퀸이 배치되지 않았다면
            pos[i] = j                          # 퀸을 j행에 배치

            if i == 7 :                         # 모든 열에 퀸을 배치 완료
                put()
            else :
                flag_ch[j] = flag_le[i + j] = flag_ri[i - j + 7] = True
                set(i + 1)                      # 다음 열에 퀸을 배
                flag_ch[j] = flag_le[i + j] = flag_ri[i - j + 7] = False

set(0)  # 0열에 퀸 배치