from itertools import product

def solution(numbers, target):
    '''
    완전탐색법
    cases: 덧셈/뺄셈 부호의 전체 케이스 
    count: number와 같은 결과가 덧셈 결과로 나오는 경우의 수
    '''
    cases = []
    for _ in range(len(numbers)):
        cases.append([-1, 1])
    cases = list(product(*cases))
    # print(cases)
    
    count = 0
    for case in cases:
        s = 0
        for i in range(len(numbers)):
            s += case[i] * numbers[i]
        if s == target:
            count += 1
    return count

if __name__ == '__main__':
    nums = [[1,1,1,1,1], [1,1,1]]
    tgt = [3, 1] 
    # answer = 5, 3
    for inp in zip(nums, tgt):
        print(solution(inp[0], inp[1]))