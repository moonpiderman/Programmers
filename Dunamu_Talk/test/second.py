def solution(price):
    answer = []

    # for i in range(len(price)):
    #     if i == len(price) - 1:
    #         answer.append(-1)
    #         break
    #     for j in range(i + 1, len(price)):
    #         if j == len(price) - 1 and price[i] >= price[j]:
    #             answer.append(-1)
    #             break
    #
    #         if price[i] < price[j]:
    #             answer.append(j - i)
    #             break

    for i in range(len(price)):
        if i == len(price) - 1:
            answer.append(-1)
            break
        tmp = [j for j in price[i:] if j > price[i]]
        if len(tmp) == 0:
            answer.append(-1)
        else:
            t = price.index(tmp[0])
            if t < i:
                answer.append(t - i + len(price) - len(tmp) - len(price[i:]))
            else:
                answer.append(t - i)

    return answer

if __name__ == '__main__':
    prices = [
        [4, 1, 4, 7, 6],
        [13, 7, 3, 7, 5, 16, 12]
    ]

    for price in prices:
        print(solution(price))