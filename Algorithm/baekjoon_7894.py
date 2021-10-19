# 재귀 알고리즘
# 수학식 활용 - log
# Time over
# 참고 블로그 - https://prod.velog.io/@inwooleeme/%EB%B0%B1%EC%A4%80-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-7894%EB%B2%88-%ED%81%B0-%EC%88%98
import sys # 입력
from math import factorial, log10, ceil # 팩토리얼, 상용로그, 올림

# def factorial(n):
#     if n == 1:
#         return 1
#     return n*factorial(n-1)

# def calc_digit(num):
#     digit = 0
#     while True:
#         # 더이상 나눠지지 않을때 break
#         if num <= 0:
#             break
#         num //= 10
#         digit += 1
#     return digit

def calc_digit(n):
    if n == 1:
        return log10(1)
    return log10(n)+calc_digit(n-1)


if __name__ == "__main__":
    num = int(sys.stdin.readline())
    # num = int(input())
    num_list = []

    for i in range(num):
        num_list.append(int(sys.stdin.readline()))
    
    for n in num_list:
        # Time over
        # print(calc_digit(factorial(n)))
        # print(ceil(log10(factorial(n))))
        print(ceil(calc_digit(n)))