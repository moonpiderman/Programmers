import math
def solution(N, M):
    return N // math.gcd(N, M)

if __name__ == '__main__':
    N, M = 10, 4
    print(solution(N, M))