from collections import deque
def bina(n):
    answer = bin(n)
    return answer[2:]

def solution(N):
    l = deque(list(bina(N)))
    cnt = 0
    tmp = []

    while l:
        if l.popleft() == '0':
            cnt += 1
        else:
            tmp.append(cnt)
            cnt = 0
    return max(tmp)

if __name__ == '__main__':
    Ns = [
        9, 529, 20, 15, 32
    ]

    for num in Ns:
        print(solution(num))