def solution(s):
    s = s.lower()
    p = "p"
    y = "y"

    count_p = s.count(p)
    count_y = s.count(y)

    return (count_p == count_y)
