def factorial(n):
    if n == 1:
        return 1
    return n*factorial(n-1)

def calc_digit(num):
    digit = 0
    while True:
        # 더이상 나눠지지 않을때 break
        if num <= 0:
            break
        num //= 10
        digit += 1
    return digit

if __name__ == "__main__":
    num = int(input())
    num_list = []

    for i in range(num):
        num_list.append(int(input()))
    
    for n in num_list:
        print(calc_digit(factorial(n)))
