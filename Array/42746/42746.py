def solution(numbers):
    answer = ''
    test = [c for c in a]

    for i, j in enumerate(test):
        if j >= 10:
            while j > 0:
                j = j // 10
                if j > 0 and j < 10:
                    break
            test[i] = j

    for i, j in enumerate(test):
        if j == max(test):
            answer += str(numbers[i])
            numbers.remove(numbers[i])
            test.remove(j)
    answer += str(numbers[0])
    return answer


a = [6, 10, 2]
l = ''

# dic = {i: j for i, j in enumerate(a)}
# print(dic)

test = [c for c in a]

for i, j in enumerate(test):
    if j >= 10:
        while j > 0:
            j = j // 10
            if j > 0 and j < 10:
                break
        test[i] = j

for i, j in enumerate(test):
    if j == max(test):
        l += str(a[i])
        a.remove(a[i])
        test.remove(j)
l += str(a[0])

print(l)


# for i in range(len(a)):
#     l += str(a[i])
# l = int(l)
# print(l)
