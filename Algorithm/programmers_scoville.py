# using heapq
from heapq import heappop


def solution(scoville: list, K: int):
    '''
    scoville: 스코빌 지수(맵기 정도) 
    K: 임계값 
    mixed_scoville: 최소와 2번째로 작은 스코빌 지수의 합
    cnt_mixed: 섞은 회수
    max_mixed: 섞은 후의 최대 scoville
    '''
    import heapq
    import copy

    cnt_mixed = 0
    mixed_scoville = 0
    heapq.heapify(scoville)
    
    while(1):
        # if len(scoville) != 0:
        min_scoville = heapq.heappop(scoville)
        # print('s0: ', scoville)

        if min_scoville >= K:
            return cnt_mixed
        elif len(scoville) == 0 and min_scoville < K:
            return -1
        else:
            sec_scoville = heapq.heappop(scoville)
            mixed_scoville = min_scoville + 2*sec_scoville
            # print('s1: ', scoville)
            heapq.heappush(scoville, mixed_scoville)
            # print('s2: ', scoville, ' len: ', len(scoville))

            cnt_mixed += 1

if __name__ == '__main__':
    s = [[1,2,3,9,10,12], [0, 0], [1,2], [1,2,3], [7, 1], [3, 4], [4, 4], [3, 3], [1,5], [2,3,7,10,15]]
    k = 7
    for i in s:
        print(solution(i, k))
