def solution(bridge_length, weight, truck_weights):
    count_time = 0
    queue = [0 for i in range(bridge_length)]

    while queue:
        # 시간은 어차피 흘러야 함
        count_time += 1
        # 앞에 놈을 끄집어 낸다.
        queue.pop(0)
        if truck_weights:
            if sum(queue) + truck_weights[0] <= weight:
                queue.append(truck_weights.pop(0))
            else:
                queue.append(0)

    return count_time
