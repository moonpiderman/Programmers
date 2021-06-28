from itertools import combinations
def solution(nums):
    answer = []
    l = list(combinations(nums, len(nums) // 2))
    length = len(l)

    for i in range(length) :
        tmp = []
        # 내부 전부 다 중복체크해야함 시부럴거
        if l[i][0] != l[i][1] :
            tmp.append(l[i][0])
            tmp.append(l[i][1])
        else :
            continue
        tmp.sort()

        if not tmp in answer :
            answer.append(tmp)

    return len(answer[0])

if __name__ == '__main__' :
    nums_1 = [3, 1, 2, 3]
    nums_2 = [3, 3, 3, 2, 2, 4]
    nums_3 = [3, 3, 3, 2, 2, 2]

    print(solution(nums_2))