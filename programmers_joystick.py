import numpy as np

# 코드 문제점: 좌우로 이동할 때 한 쪽 방향으로만 움직이는 것은 아니다.
def solution(name):
    """
    ▲ - 다음 알파벳
    ▼ - 이전 알파벳 (A에서 아래쪽으로 이동하면 Z로)
    ◀ - 커서를 왼쪽으로 이동 (첫 번째 위치에서 왼쪽으로 이동하면 마지막 문자에 커서)
    ▶ - 커서를 오른쪽으로 이동
    """

    move_cnt = 0 # 이동횟수 총합
    leftright_cnt = 0 # 좌우 이동횟수 총합 
    updown_cnt = 0 # 상하 이동횟수 총합

    ord_A = ord('A')
    ord_Z = ord('Z')

    # ord(ch) - ord('A')
    move_up = np.array([[ord(chr)-ord_A, 1] if chr != 'A' else [ord(chr)-ord_A, 0] for chr in name])
    # print(move_up)

    # A가 아닌 경우를 모두 세기 
    notA_nums = int(np.sum(move_up, axis=0)[1])
    # print('A가 아닌 경우의 총 개수: ', notA_nums)

    # 아래로 움직여야하는 횟수 세기
    move_down = ord_Z - ord_A + 1 - move_up[:, 0]
    # print(move_down)

    # 위로 움직여야하는 횟수 세기
    move_up = move_up[:, 0]
    # print(move_up)
    
    # 각 글자마다 최소 상하이동 횟수 리스트
    updown_min = [min(u, d) for u, d in zip(move_up, move_down)]
    print('updown_min: ', updown_min)
    
    # 위아래로 움직여야하는 횟수 총합
    updown_cnt = int(np.sum(updown_min)) # 리스트 총합 
    # print('상하 이동횟수 총합: ', updown_cnt)

    # 좌우로 움직여야하는 최소 횟수 세기 
    notA_idx = [i for i in range(1, len(updown_min)) if updown_min[i] != 0]
    notA_len = len(updown_min)
    # print(notA_idx)

    left = 0 
    right = 0
    now_idx = 0
    
    while(1):
        if len(notA_idx) == 0:
            break
        
        right = notA_idx[0] - now_idx
        left = notA_len - notA_idx[0] + now_idx
        # print(left, right)

        if right >= left:
            leftright_cnt = leftright_cnt + left
            now_idx = left
        else:
            leftright_cnt = leftright_cnt + right
            now_idx = right

        now_idx = notA_idx.pop(0)

    # print('좌우 이동횟수 총합: ', leftright_cnt)

    move_cnt = leftright_cnt + updown_cnt # - 1 # 좌우 볼때 1부터 봤으니까 1 빼줘야함
    return move_cnt

if __name__ == '__main__':
    test_list = ['JAZ', 'JEROEN', 'JAN', 'ABAAAAAAAAABB', 'JABBBBAAAAAAAABAA', 'A', 'Z', 'AAZ', 'ZZZAAAZ', 'ABBBAAAAABB'] 
    # answer = 11, 56, 23, 7, 27, 0, 1, 2, 8, 12
    for test in test_list:
        result = solution(test)  
        print(result)
        print('----------')