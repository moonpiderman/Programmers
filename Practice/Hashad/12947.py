def solution(x):
    mod = 0
    result = x

    while result > 0 :
        mod += result % 10
        result //= 10

    if x % mod == 0 :
        return True
    else :
        return False

if __name__ == '__main__' :
    arr_1 = 10
    arr_2 = 12
    arr_3 = 11
    arr_4 = 13

    print(solution(arr_1))