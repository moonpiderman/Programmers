import collections
def solution(A):
    if len(A) == 0:
        return -1

    answer = collections.Counter(A).most_common(1)[0]
    if answer[1] > len(A) / 2:
        return A.index(answer[0])
    else:
        return -1

if __name__ == '__main__':
    A = [3, 4, 3, 2, 3, -1, 3, 3]
    print(solution(A))