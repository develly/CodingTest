#-*- encoding: utf-8 -*-
# 더 맵게, Heap 알고리즘, []

import heapq

def solution(scoville, K):
    answer = 0
    scoville.sort() # return None
    scoville = list(filter(lambda x: x < K, scoville))

    if not len(scoville): return answer
    
    for i in range(len(scoville)-1):
        if scoville[0] >= K:
            break
        else : 
            heapq.heappush(scoville, heapq.heappop(scoville) + heapq.heappop(scoville) * 2)
            answer += 1    
    
    if scoville[0] < K:
        return -1
    
    return answer

if __name__ == "__main__":
    scoville = [1, 2, 3, 9, 10, 12]
    K = 7
    answer = solution(scoville, K)
    print(answer)
