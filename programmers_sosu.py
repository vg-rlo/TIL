import itertools

def solution(numbers):
    '''
    numbers: 숫자 조합의 문자열 
    sosu_count: 소수인 숫자의 개수
    '''
    nums_lst = []
    sosu_count = 0
    
    for i in range(1, len(numbers)+1):
        tmp_lst = list((map(int, map(''.join, itertools.permutations(numbers, i)))))
        # print(tmp_lst)
        nums_lst = nums_lst + tmp_lst
        
    nums_lst = list(set(nums_lst))
    # print('전체 조합:', nums_lst)

    for num in nums_lst:
        if num <= 1:
            pass
            # print('1보다 같거나 작습니다.')
        else:
            for i in range(2, int(num**(1/2))+1):
                if num % i == 0:
                    break
            else:
                sosu_count += 1 
    
    return sosu_count

if __name__ == '__main__':
    nums = ['17', '011', '20']
    # answer = 3, 2, 1
    for n in nums:
        print(solution(n))