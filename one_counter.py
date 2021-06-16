def oneCounter(num):
    answer = 0

    # 이진수로 변환
    num2bin = [format(i, 'b') for i in range(1, num+1)] 
    # num2bin = "{0:b}".format(num)
    # num2bin = bin(num) # 접두사 0b가 붙음
    # print(num2bin) 
    
    # str으로 변환 후 1 개수 세기
    one_cnt = [str(str(b).count('1')) for b in num2bin]
    same_cnt = ''.join(one_cnt).count(one_cnt[-1])
    # print(same_cnt)

    # 자기 자신은 개수에서 제외 
    return same_cnt - 1 

if __name__ == '__main__':
    numbers = [9, 3, 1, 8] # result: 3, 0, 0, 3
    for n in numbers:
        print(oneCounter(n))