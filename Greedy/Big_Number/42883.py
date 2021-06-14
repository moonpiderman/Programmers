from itertools import permutations

def solution_fail(number, k):
    number = list(number)
    permu = list(permutations(number, len(number) - k))
    next = []
    an = [None for r in range(len(permu))]

    for i in permu :
        next.append(list(i))

    for i in range(len(next)) :
        chk = "".join(next[i])
        an[i] = chk

    an = list(map(int, an))
    answer = str(max(an))

    return answer

def solution_1(number, k) :
    stack = [number[0]]
    for num in number[1:] :
        while len(stack) > 0 and stack[-1] < num and k > 0 :
            k -= 1
            stack.pop()
        stack.append(num)

    if k != 0 :
        stack = stack[:-k]
    return ''.join(stack)

def solution(number, k) :
    stack = []

    for i in number :
        while stack and i > stack[-1] :
            if k > 0 :
                stack.pop()
                k -= 1
            else :
                break

        stack.append(i)

    if k > 0 :
        for i in range(k) :
            stack.pop()

    answer = "".join(stack)
    return answer

if __name__ == '__main__' :
    number_1 = "1924"
    k_1 = 2

    number_2 = "1231234"
    k_2 = 3

    number_3 = "4177252841"
    k_3 = 4

    # print(solution_fail(number_2, k_2))
    # print(solution_1(number_2, k_2))
    print(solution(number_2, k_2))