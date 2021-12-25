from collections import deque
def solution(N, road, K):
    answer = 0
    INF = int(1e9)

    distance = [INF] * (N + 1)
    distance[1] = 0

    graph = [[INF] * (N + 1) for _ in range(N + 1)]
    for i in road:
        graph[i[0]][i[1]] = min(graph[i[0]][i[1]], i[2])
        graph[i[1]][i[0]] = min(graph[i[1]][i[0]], i[2])

    q = deque()
    q.append(1)

    while q:
        now = q.popleft()
        for next in range(1, N + 1):
            if graph[now][next] != INF and distance[next] > distance[now] + graph[now][next]:
                q.append(next)
                distance[next] = distance[now] + graph[now][next]

    for i in range(len(distance)):
        if distance[i] <= K:
            answer += 1
    return answer

if __name__ == '__main__':
    N_1 = 5
    road_1 = [
        [1, 2, 1],
        [2, 3, 3],
        [5, 2, 2],
        [1, 4, 2],
        [5, 3, 1],
        [5, 4, 2]
    ]
    K_1 = 3

    N_2 = 6
    road_2 = [
        [1, 2, 1],
        [1, 3, 2],
        [2, 3, 2],
        [3, 4, 3],
        [3, 5, 2],
        [3, 5, 3],
        [5, 6, 1]
    ]
    K_2 = 4

    print(solution(N_1, road_1, K_1))
    print(solution(N_2, road_2, K_2))