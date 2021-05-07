def solution(prices):
    remain_second = [len(prices) - 1 - i for i in range(len(prices))]

    # prices의 index 값을 저장해둘 리스트
    stack = [0]

    for i in range(1, len(prices)):
        while stack:
            index = stack[-1]
            if prices[index] > prices[i]:
                remain_second[index] = i - index
                stack.pop()

            else:
                break
        stack.append(i)
    return remain_second
