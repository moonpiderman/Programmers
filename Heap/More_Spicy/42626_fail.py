import heapq
def func_scoville(first, second) :
    mix_scoville = first + (second * 2)
    return mix_scoville

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while scoville :
        first = heapq.heappop(scoville)
        if first < K and len(scoville) >= 1:
            second = heapq.heappop(scoville)
            heapq.heappush(scoville, func_scoville(first, second))
            answer += 1
        else :
            break

    # 싹 다 돌렸는데 scoville 이 K를 넘지 못할 때
    if scoville == None :
        if first < K :
            answer = -1
    return answer

if __name__ == '__main__' :
    scoville = [1, 2, 3, 9, 10, 12]
    k = 7
    print(solution(scoville, k))