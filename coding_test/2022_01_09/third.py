import math
def prime(number) :
    for i in range(2, int(math.sqrt(number)) + 1) :
        if number % i == 0 :
            return False
    return True

def solution(N, M):
    count = 0
    arr = []
    for chk in range(2, N + 1):
        if prime(chk):
            arr.append(chk)

    for i in range(len(arr)):
        summ = 0
        for j in range(i, len(arr)):
            summ += arr[j]
            if summ == M:
                count += 1
                break

    return count

if __name__ == '__main__':
    test = [
        [20, 36], [100, 83], [12, 10]
    ]

    for t in test:
        print(solution(t[0], t[1]))