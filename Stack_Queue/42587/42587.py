from collections import deque

def solution(priorities, location):
    # location은 인덱스 값
    # return은 실질적 n번째인지
    answer = 0
    dic = {i: priorities[i] for i in range(len(priorities))}


    return answer

# dic = {i: priorities[i] for i in range(len(priorities))}

priorities = [1, 1, 9, 1, 1, 1]
location = 0

pop_idx = 0
pop_pri = 0
result = []

# 인덱스 deque 생성
index = []
for i in range(len(priorities)) :
    index.append(i)
index = deque(index)

# deque of priorities
p = deque(priorities)

for i in range(len(priorities)) :
    for j in range(len(priorities)) :
        if priorities[i] < priorities[j] :
            pop_idx = index.popleft()
            pop_pri = p.popleft()
            index.append(pop_idx)
            p.append(pop_pri)
        else :
            result.append(p[i])

print(result)