import heapq
def calculation(val1, val2):
    return val1 + (val2 * 2)

def solution(scoville, k):
    count = 0
    heapq.heapify(scoville)

    while scoville[0] <= k:
        if len(scoville) > 1:
            first = heapq.heappop(scoville)
            second = heapq.heappop(scoville)
            heapq.heappush(scoville, calculation(first, second))
            count += 1
        else:
            return -1
    return count

if __name__ == '__main__':
    scoville = [1, 2, 3, 9, 10, 12]
    k = 7

    print(solution(scoville, k))