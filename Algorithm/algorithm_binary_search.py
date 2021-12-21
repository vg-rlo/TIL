def binary_search(input_list, target):
    # binary search의 조건 - 입력 리스트가 정렬된 상태여야 합니다.
    input_list.sort()
    print(input_list)
    # left, right값을 구합니다. 
    left_idx = 0
    right_idx = len(input_list) - 1
    
    trial = 0
    while True:
        # mid값을 업데이트합니다.
        mid_idx = (left_idx + right_idx) // 2
        print(f"{trial}차 loop: {left_idx, mid_idx, right_idx}")
        # target 값을 찾으면 break
        if input_list[mid_idx] == target:
            break
        elif input_list[mid_idx] > target:
            right_idx = mid_idx - 1
        # input_list[mid_idx] < target
        else:
            left_idx = mid_idx + 1
        trial += 1
    return mid_idx

if __name__ == "__main__":
    lst = [1, 3, 4, 10, 11, 18, 20, 40, 50,13, 15]
    tar = 20

    print(f"target {tar} == answer {lst[binary_search(lst, tar)]}")