def solution(board, moves):
    """
    board: 게임에서의 격자 상태에 인형이 담긴 NxN 2차원 배열
    moves: 인형을 담는 Mx1 배열(M: NxN)
    cnt: 동일한 인형이 2개일 때 제거한 인형의 개수 총합
    """

    cnt = 0
    basket = []
    for m in moves:
        for b in range(len(board)):
            doll = board[b][m-1]
            if doll != 0:
                basket.append(doll)
                board[b][m-1] = 0
                if len(basket) >= 2:
                    if basket[-1] == basket[-2]:
                        basket.pop(-1)
                        basket.pop(-1)
                        cnt += 2
                break
    return cnt


if __name__ == '__main__':
    b = [[0, 0, 0, 0, 1],
         [0, 0, 1, 0, 3],
         [0, 2, 5, 0, 1],
         [4, 2, 4, 4, 2],
         [3, 5, 1, 3, 1]]
    m = [1, 5, 3, 5, 1, 2, 1, 4]

    print(solution(b, m))
