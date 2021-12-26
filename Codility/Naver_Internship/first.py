def solution(T):
    T.upper()
    if len(T) == 0:
        return ""
    T = sorted(T, reverse=True)

    return "".join(T)

if __name__ == '__main__':
    Ts = [
        "MSSLS", "LLMS", "SMS"
    ]

    for T in Ts:
        print(solution(T))