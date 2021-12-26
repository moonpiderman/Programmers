def solution(A):
    dic = dict()

    for val in A:
        if val in dic.keys():
            dic[val] += 1
        else:
            dic[val] = 1

    for key, value in dic.items():
        if value % 2 != 0:
            return key

if __name__ == '__main__':
    A = [9, 3, 9, 3, 9, 7, 9]
    print(solution(A))