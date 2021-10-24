# 하노이 탐
# 문제 링크 - https://www.acmicpc.net/problem/11729
# 참고 블로그 - https://ddmix.blogspot.com/2014/12/cppalgo-8-recursion.html
# 접근방법 - 재귀

def hanoi_top(n, move_from, move_by, move_to):
    # 재귀 break 조건 - 기둥1의 원반이 1개 남았을 때
    if n == 1:
        print(f"{move_from} {move_to}")
    else:
        hanoi_top(n-1, move_from, move_to, move_by)
        print(f"{move_from} {move_to}")
        hanoi_top(n-1, move_by, move_from, move_to)


if __name__ == "__main__":
    num = int(input())

    # (이론) 최소 이동 횟수 = 2^(원반 갯수)-1
    print((2**num)-1)

    hanoi_top(num, 1, 2, 3)