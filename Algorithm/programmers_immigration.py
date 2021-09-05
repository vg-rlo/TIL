# 입국심사
def solution(n, times):
    answer = 0
    left = 1
    right = max(times)*n
    
    while True:
        # 이분탐색의 종료 조건
        # 검색 범위 더이상 없는 경우 break
        if left >= right:
            answer = left
            break
        
        # print(left, right) 
        mid = (left+right)//2
        last = 0
        
        # 주어진 시간(mid) 동안 각 심사관은 몇 명을 상대하는지 계산
        for time in times:
            last += mid//time
            # print('change last: ', last)
        
        # 심사한 명수가 목표 명수(n) 보다 크면 right를 mid값으로 줄인다.
        if last >= n:
            right = mid
            # print('change right: ', right)
        # 심사한 명수가 목표 명수(n) 보다 작으면 left를 mid+1값으로 키운다.
        else:
            left = mid+1
            # print('change left: ', left)        
    return answer


if __name__ == '__main__':
    nn = [6, 6, 5]
    ttimes = [[7, 10], [7, 2, 3, 4], [1, 1, 5, 6, 3]]
    
    for inp in zip(nn, ttimes):
        print(solution(inp[0], inp[1]))
        print('---------')
