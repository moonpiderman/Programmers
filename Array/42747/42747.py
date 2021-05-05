def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer


'''
c = [5, 5, 5, 5]

test = [10, 11, 33, 8, 9, 22, 7, 1]
c.sort(reverse=True)
answer = max(map(min, enumerate(c, start=1)))
print(answer)

test1 = list(map(min, enumerate(test, start=1)))
print(test1)

test2 = list(map(min, enumerate(c, start=1)))
print(test2)
'''
