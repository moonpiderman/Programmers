def solution(C, F, X):
    time_min = 1000000
    emplo_min = 1000000
    emplo = 0
    emplo_time = 0

    while True:
        if emplo == 0:
            total_time = X / 2
        else:
            emplo_time += C / (((emplo - 1) * F) + 2)
            work_time = X / ((emplo * F) + 2)
            total_time = emplo_time + work_time

        if total_time < time_min and emplo_min > emplo:
            time_min = total_time
            emplo_min = emplo
            answer = time_min
        else:
            break
        emplo += 1
    return round(answer, 6)

if __name__ == '__main__':
    C = [30.0, 30.0, 30.5, 500.0]
    F = [1.0, 2.0, 3.14159, 4.0]
    X = [2.0, 100.0, 1999.1999, 2000.0]

    for i in range(len(C)):
        print(solution(C[i], F[i], X[i]))