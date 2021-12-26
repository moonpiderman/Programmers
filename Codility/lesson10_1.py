def sol(N):
    i = 1
    answer = 0
    while i ** 2 <= N:
        if i ** 2 == N:
            answer += 1
        elif N % i == 0:
            answer += 2
        i += 1
    return answer

if __name__ == '__main__':
    print(sol(24))