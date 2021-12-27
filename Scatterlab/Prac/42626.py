import heapq
def calculation(n, m):
    if n > m:
        n, m = m, n
    return n + (m * 2)

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while scoville[0] < K:
        if len(scoville) > 1:
            first = heapq.heappop(scoville)
            sec = heapq.heappop(scoville)
            heapq.heappush(scoville, calculation(first, sec))
            answer += 1
        else:
            return -1
    return answer

if __name__ == '__main__':
    scoville = [1, 2, 3, 9, 10, 12]
    k = 7
    print(solution(scoville, k))