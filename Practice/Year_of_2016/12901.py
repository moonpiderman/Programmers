import datetime
def solution(a, b):
    today = 'MON TUE WED THU FRI SAT SUN'.split()

    return today[datetime.datetime(2016, a, b).weekday()]

if __name__ == '__main__' :
    a = 5
    b = 24

    print(solution(a, b))