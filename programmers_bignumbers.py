import heapq
    
def solution(number, k):
    answer = ''
    
    # 숫자로 바꿔준다.
    num2int = [[ch[0], int(ch[1])] for ch in enumerate(number)]
    print(num2int)

    # heap으로 min을 pop시킨다.
    while(1):
        i=k
        if i == k:
            break

        num2int.pop()
    print(num2int)

    # 큰 숫자로 정렬을 먼저한다. 
    int2num = [str(i) for i in num2int]
    # print(int2num)

    answer = "".join(int2num)
    # print(answer)

    return answer

if __name__ == '__main__':
    nums = ['1924', '1231234', '4177252841', '7921']
    k = [2, 3, 4, 2]

    for num, k_i in zip(nums, k):
        print(solution(num, k_i)) # 94, 3234, 775841, 92