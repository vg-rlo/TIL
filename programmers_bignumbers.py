import heapq
    
def solution(number, k):
    answer = ''
    
    # 숫자로 바꿔준다.
    num2int = [int(ch) for ch in number]

    # heap으로 min을 pop시킨다.
    for i in range(k):
        heapq.heappop(num2int)
        
    # 큰 숫자로 정렬을 먼저한다. 
    int2num = [str(i) for i in sorted(num2int, reverse=True)]
    # print(int2num)

    answer = "".join(int2num)
    # print(answer)

    return answer

if __name__ == '__main__':
    nums = ['1924', '1231234', '4177252841']
    k = [2, 3, 4]

    for num, k_i in zip(nums, k):
        print(solution(num, k_i))