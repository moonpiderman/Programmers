def solution(name):
    cnt = 0
    name = list(name.upper())
    i = 0

    while True:
        cnt += min(ord(name[i]) - ord('A'), ord('Z') - ord(name[i]) + 1)
        name[i] = 'A'

        if name.count('A') == len(name) :
            return cnt

        left, right = 1, 1
        for l in range(1, len(name)) :
            if name[i - l] == 'A':
                left += 1
            else:
                break

        for r in range(1, len(name)) :
            if name[i + r] == 'A':
                right += 1
            else :
                break

        if left < right :
            cnt += left
            i -= left
        else :
            cnt += right
            i += right
    return cnt

if __name__ == '__main__' :
    name_1 = "JEROEN"
    name_2 = "JAN"
    name_3 = "jijo"
    name_4 = "AZAAAZ"

    print(solution(name_4))