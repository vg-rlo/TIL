# using heapq
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

    answer = 0
    cnt_mixed = 0
    mixed_scoville = 0
    scoville_copy = scoville.copy()

    # greedy탐색법으로 maximum mixed scoville이 K보다 작으면 return -1
    max_scoville = max(scoville_copy)
    scoville_copy.pop(scoville_copy.index(max_scoville))
    sec_scoville = max(scoville_copy)
    max_mixed = max_scoville + sec_scoville 
    if max_mixed < K:
        return -1
    
    while(1):
        # scoville내 원소가 모두 삭제거나 임계값 이상이면 break
        if len(scoville) == 0 or mixed_scoville >= K:
            break
        
        min_scoville = heapq.heappop(scoville)
        sec_scoville = heapq.heappop(scoville)
        
        mixed_scoville = mixed_scoville + min_scoville + sec_scoville
        cnt_mixed += 1

    return cnt_mixed

# using stack
def timeover(scoville: list, K: int):
    '''
    scoville: 스코빌 지수(맵기 정도) 
    K: 임계값
    answer: int or -1, 정답 
    mix_cnt: 섞은 회수
    '''
    answer = 0
    mixed_cnt = 0
    
    scoville = sorted(scoville)
    first_max = scoville[-1]
    second_max = scoville[scoville.index(first_max)-1]
    # print(first_max, second_max)
    
    if first_max + second_max < K:
        return -1
    else:    
        while(1): 
            if (min(scoville) >= K):
                break
            first_min = min(scoville)
            scoville.pop(scoville.index(first_min))
            second_min = min(scoville)
            scoville.pop(scoville.index(second_min))
            # print(scoville)
            
            mixed = first_min + (second_min*2)
            scoville += [mixed]
            mixed_cnt += 1
            # print(mixed_cnt)
            
        return mixed_cnt

if __name__ == '__main__':
    s = [1,2,3,9,10,12]
    k = 7
    print(solution(s, k))