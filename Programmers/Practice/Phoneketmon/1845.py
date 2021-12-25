from itertools import combinations
def solution_fail(nums):
    answer = []
    ball = []
    poke = len(nums) // 2
    l = list(combinations(nums, poke))
    print(l)
    # print(poke)

    for i in l :
        tmp = []
        # for j in range(poke) :
        #
        ball.append(tmp)

    print(answer)

    return len(answer)

def solution_diff(nums) :
    answer = 0
    length = len(nums) // 2
    nums.sort()
    last = 0

    for p in nums :
        if (p != last and answer < length) :
            answer += 1
            last = p

    return answer

def solution(nums) :
    answer = 0
    pick = len(nums) // 2
    nums = list(set(nums))

    if len(nums) >= pick :
        answer = pick
    elif len(nums) < pick :
        answer = len(nums)

    return answer

if __name__ == '__main__' :
    nums_1 = [3, 1, 2, 3]
    nums_2 = [3, 3, 3, 2, 2, 4]
    nums_3 = [3, 3, 3, 2, 2, 2]

    print(solution(nums_1))