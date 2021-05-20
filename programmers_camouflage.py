import math
from itertools import product
from functools import reduce

def multiply(arr):
        return reduce(lambda x, y: x * y, arr)

def solution(clothes):
    answer = 0

    kinds = list(set(list(zip(*clothes))[1])) # 옷 종류 
    clothes_dict = dict.fromkeys(kinds, [])

    if len(kinds) == 1:
        answer = len(clothes) 
        print(answer)
        return answer

    for i in clothes:
        clothes_dict[i[1]] = clothes_dict[i[1]] + [i[0]]
    # print('dict: ', clothes_dict)
    
    clothes_len = [len(clothes_dict[c]) for c in clothes_dict]
    print('length: ', clothes_len)

    answer = len(clothes) + multiply(clothes_len)# 조합의 수 구하기
    return answer

if __name__ == '__main__':
    tests = [
        [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]],
        [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]
        ] # 2차원 배열로 된 옷

    result = [solution(test) for test in tests]
    print(result)