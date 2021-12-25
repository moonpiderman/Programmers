def solution(arr):
    new_arr = []
    for i in range(len(arr)):
        if i == 0:
            new_arr.append(arr[i])
        elif arr[i] != arr[i - 1]:
            new_arr.append(arr[i])
    return new_arr
