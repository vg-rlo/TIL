def solution(clothes):
    answer = 0

    kinds = list(set(list(zip(*clothes))[1])) # 옷 종류 
    clothes_dict = dict.fromkeys(kinds, []) # dictionary 생성(key: 옷 종류, value: 해당 종류의 옷들)

    clothe_kinds_lst = list(set(list(zip(*clothes))[1]))
    clothe_kinds_all = list(zip(*clothes))[1]

    for k in kinds:
        clothes_dict[k] = clothe_kinds_all.count(k)
    
    cnt_mul = 1
    for cnt in clothes_dict.values():
        cnt_mul = cnt_mul * (cnt+1)
    return cnt_mul -1

if __name__ == '__main__':
    tests = [
        [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]],
        [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]
        ] # 2차원 배열로 된 옷

    result = [solution(test) for test in tests]
    print(result)