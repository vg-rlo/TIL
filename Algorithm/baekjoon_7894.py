# 재귀 알고리즘 대신 단순 for loop
# 수학식 활용 - log, 곱셈 대신 덧셈
# Time over solved
# 참고 블로그 - https://prod.velog.io/@inwooleeme/%EB%B0%B1%EC%A4%80-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-7894%EB%B2%88-%ED%81%B0-%EC%88%98
# 참고 블로그 - https://lifedev0.tistory.com/78
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

# def calc_digit(n):
#     if n == 1:
#         return log10(1)
#     return log10(n)+calc_digit(n-1)


if __name__ == "__main__":
    num = int(sys.stdin.readline())
    # num = int(input())
    for i in range(num):
        log_sum = 0
        n = int(sys.stdin.readline())
        for i in range(1, n+1):
            log_sum += log10(i)
        print(int(log_sum)+1)

        # Wrong
        # print(ceil(log_sum)) 

    # Time over
    # for n in num_list:
    #     print(calc_digit(factorial(n)))
    #     print(ceil(log10(factorial(n))))