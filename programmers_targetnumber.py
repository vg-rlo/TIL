def solution(numbers, target):
    # answer = 0
    cnt = 0
     
    for i in range(len(numbers)):
        change_numbers = numbers
        change_numbers[i] = -numbers[i]
        s = sum(change_numbers)
        print(change_numbers)

        if s == target:
            cnt += 1
                
    if sum(numbers) == target:
        cnt += 1

    return cnt

if __name__ == '__main__':
    nums = [1,1,1,1,1]
    tgt = 3 
    # answer = 5
    print(solution(nums, tgt))