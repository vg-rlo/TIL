def kNumber(array, commands):
    answer = []

    # 예상 arr_sliced값: [(3, [2, 6, 3, 7]), (1, [3]), (3, [5, 2, 6, 3, 7, 4])]
    arr_sliced = [(s[2], sorted(array[s[0]-1:s[1]])) for s in commands] 
    answer = [arr[i-1] for i, arr in arr_sliced]
    return answer

if __name__ == '__main__':
    arr1 = [1, 5, 2, 6, 3, 7, 4]
    cmd1 = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

    # 예상 return값: [5, 6, 3]
    print(kNumber(arr1, cmd1)) 

