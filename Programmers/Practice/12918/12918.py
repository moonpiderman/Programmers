def solution(s):
    arr = list(s)
    check = 0

    for i in arr:
        check = ord(i)
        if (check >= 65 and check <= 90) or (check >= 97 and check <= 122):
            return False
    if len(arr) == 4 or len(arr) == 6:
        return True
    else:
        return False
