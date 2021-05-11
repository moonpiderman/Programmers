from collections import deque

def solution(numbers, target) :
    answer = 0
    length = len(numbers)
    stack = []

    stack.append([numbers[0], 0])
    stack.append([-1 * numbers[0], 0])

    while stack :
        total, index = stack.pop()
        index += 1
        if length > index :
            stack.append([total + numbers[index], index])
            stack.append([total - numbers[index], index])
            print(stack)
        else :
            if total == target :
                answer += 1
    return answer

def solution_queue(numbers, target):
    answer = 0
    length = len(numbers)
    queue = deque()

    queue.append([numbers[0], 0])
    queue.append([-1 * numbers[0], 0])

    while queue :
        total, index = queue.popleft()
        index += 1
        if length > index :
            queue.append([total + numbers[index], index])
            queue.append([total - numbers[index], index])
            print(queue)
        else :
            if total == target :
                answer += 1
    return answer

if __name__ == '__main__' :
    numbers_1 = [1, 1, 1, 1, 1]
    target_1 = 3
    print(solution(numbers_1, target_1))
    # print(solution_queue(numbers_1, target_1))