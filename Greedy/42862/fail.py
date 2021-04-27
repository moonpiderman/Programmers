def solution(n, lost, reserve):
    answer = 0

    for res_stu in reserve:
        for lo_stu in lost:
            if (res_stu - 1) == lo_stu or (res_stu + 1) == lo_stu:
                answer += 1
                lost.remove(lo_stu)

    answer = n - len(lost)
    return answer
