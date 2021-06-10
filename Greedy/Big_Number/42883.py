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

def solution(number, k) :
    answer = ''

    return answer


if __name__ == '__main__' :
    number_1 = "1924"
    k_1 = 2

    number_2 = "1231234"
    k_2 = 3

    number_3 = "4177252841"
    k_3 = 4

    print(solution(number_2, k_2))