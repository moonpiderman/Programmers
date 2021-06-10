from itertools import permutations

def solution(number, k):
    answer = ''
    chk = []
    number = list(number)
    permu = list(permutations(number, k))

    # print(permu)
    

    return answer

if __name__ == '__main__' :
    number_1 = "1924"
    k_1 = 2

    number_2 = "1231234"
    k_2 = 3

    number_3 = "4177252841"
    k_3 = 4

    solution(number_1, k_1)