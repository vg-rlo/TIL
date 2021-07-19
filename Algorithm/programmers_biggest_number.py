import heapq
    
def solution(number, k):
    answer = ''
    
    # k까지 슬라이싱 후, 그 중 가장 큰 수의 Index 추출
    num2int = [int(num) for num in number]
    max_idx = num2int.index(max(num2int[:k]))
    num2int = num2int[max_idx:]
    remain_k = k - max_idx    
    # print(num2int)
    # print(f"남은 제거 가능 개수: {remain_k}개")

    i = 0
    while(1):
        # 제거 가능 개수가 0개이면 break
        if remain_k == 0 or i == len(num2int)-1:
            break
        
        if num2int[i] < num2int[i+1]:
            num2int.pop(i)
            remain_k -= 1
        else:
            i += 1
    # print(num2int)

    answer = "".join(map(str, num2int))
    return answer

if __name__ == '__main__':
    nums = ['1924', '1231234', '4177252841', '7921']
    k = [2, 3, 4, 2]

    for num, k_i in zip(nums, k):
        print(solution(num, k_i)) # 94, 3234, 775841, 92