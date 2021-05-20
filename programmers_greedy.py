# import operator as op 

def solution(n, lost, reserve):
    answer = 0
    available = []
    idx = 0 

    # reserve인 사람 중에 lost인 사람은 제외 
    tmp_lost = lost.copy()
    lost = [i for i in lost if i not in reserve]
    reserve = [i for i in reserve if i not in tmp_lost] 
    
    # 1의 값 가지거나, n값 가지는 경우는 둘 중 한 값만 가지므로 먼저 처리 
    if 1 in reserve:
        try:
            lost.pop(lost.index(2))
            reserve.pop(reserve.index(1))
        except:
            reserve.pop(reserve.index(1))

    if n in reserve:
        try:
            lost.pop(lost.index(n-1))
            reserve.pop(reserve.index(n))
        except:
            reserve.pop(reserve.index(n))
    
    while(1):
        # reserve로 확인할 값이 더이상 없는 경우 break
        if len(reserve) == 0:
            break 

        # add_i = op.add(reserve[idx], 1)
        # sub_i = op.sub(reserve[idx], 1)
        add_i = reserve[idx] + 1 # 실행 속도 더 빠름 
        sub_i = reserve[idx] - 1

        if add_i in lost and sub_i in lost:
            lost.pop(lost.index(sub_i))
        elif add_i not in lost and sub_i in lost:
            lost.pop(lost.index(sub_i))
        elif add_i in lost and sub_i not in lost:
            lost.pop(lost.index(add_i))

        reserve.pop(idx)
        
    answer = n - len(lost)
    return answer

if __name__ == '__main__':
    nums = [5, 5, 3, 5]                # 전체 학생의 수 
    losts = [[2,4], [2,4], [3], [1,2,3]]     # 체육복을 도난당한 학생들의 번호가 담긴 배열
    reserves = [[1,3,5], [3], [1], [2,3,4]]  # 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열
    result = []                      # 체육수업을 들을 수 있는 학생의 최댓값  

    for num, lost, reserve in zip(nums, losts, reserves):
        result.append(solution(num, lost, reserve))
    print(f'result: {result}')