import math
from itertools import product

def solution(clothes):
    answer = 0

    kinds = list(set(list(zip(*clothes))[1])) # 옷 종류 
    clothes_dict = dict.fromkeys(kinds, [])

    for i in clothes:
        clothes_dict[i[1]] = clothes_dict[i[1]] + [i[0]]
    # print('dict: ', clothes_dict)
    
    answer = len(clothes_dict.keys()) # 조합의 수 구하기
    return answer

if __name__ == '__main__':
    clothes = [
        [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]],
        [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]
        ] # 2차원 배열로 된 옷

    result = [solution(c) for c in clothes]
    print(result)