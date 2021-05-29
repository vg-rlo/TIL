def solution(scoville: list, K: int):
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
