def solution(arr, divisor):
    check = 0
    k = 0
    error_list = [-1]

    for i in range(0, len(arr)):
        if arr[i] % divisor == 0:
            check += 1

    new_arr = [0 for i in range(check)]

    for j in range(0, len(arr)):
        if arr[j] % divisor == 0:
            new_arr[k] = arr[j]
            k += 1

    new_arr.sort()

    if check == 0:
        return error_list
    else:
        return new_arr
