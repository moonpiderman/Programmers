def sol(N):
    mini = 2000000002
    i = 1

    while i ** 2 <= N:
        if i ** 2 == N:
            mini = min(mini, 4 * i)
        elif N % i == 0:
            mini = min(mini, 2 * (i + (N // i)))
        i += 1
    return mini

if __name__ == '__main__':
    print(sol(30))