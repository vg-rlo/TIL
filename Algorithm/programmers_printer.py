from collections import deque

def solution(priors, location):
    answer = 0
    locations = []

    # priors = priorities
    priors = deque(priors)
    idx_priors = deque(list(range(len(priors))))
    
    i = 0
    while(1):
        # priorities의 원소가 0개이면 break
        if len(priors) == 0:
            break 

        # print(priors)
        # print(idx_priors)
        
        if priors[i] != max(priors):        # max가 아니면 뒤로 shift
            priors.append(priors.popleft()) # pop은 O(n), popleft는 O(1)
            idx_priors.append(idx_priors.popleft())
        
        else:
            priors.popleft()
            locations.append(idx_priors.popleft())

    # print(f'Final idx: {locations}')

    return locations.index(location)+1
    # return locations.index(location)

if __name__ == '__main__':
    priorities_inputs = [[2,1,3,2], [1,1,9,1,1,1]]  # 1~9로 표현하며 숫자가 클수록 중요하다는 뜻
    location_inputs = [2, 0]                        # 0 이상 (현재 대기목록에 있는 작업 수 - 1) 이하
    results = 0 

    results = [solution(priorities_inputs[i], location_inputs[i]) for i in range(len(location_inputs))]
    print(results)