import numpy as np

def joyStick(name):
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
    updown_min = np.array([min(u, d) for u, d in zip(move_up, move_down)])
    # print('updown_min: ', updown_min)
    
    # 위아래로 움직여야하는 횟수 총합
    updown_cnt = int(np.sum(updown_min)) # 리스트 총합 
    print('상하 이동횟수 총합: ', updown_cnt)

    right_cnt = 1
    left_cnt = 1
    i = 1
    while(1):
        # print('idx: ', i)
        # A가 아닌 갯수만큼 모두 이동이 완료됐으면 루프 종료 
        if right_cnt == notA_nums or left_cnt == notA_nums or i == len(updown_min):
            leftright_cnt = i
            break
            
        if updown_min[i] != 0:
            # print(updown_min[i], ':', i)
            right_cnt += 1 

        if updown_min[len(updown_min)-i] != 0:
            # print('왼쪽', updown_min[len(updown_min)-i-1], ':', i)
            left_cnt += 1
            # print(left_cnt)
        i += 1

    print('좌우 최소 이동횟수: ', leftright_cnt)

    move_cnt = leftright_cnt + updown_cnt - 1 # 좌우 볼때 1부터 봤으니까 1 빼줘야함
    return move_cnt

if __name__ == '__main__':
    test_list = ['JAZ', 'JEROEN', 'JAN', 'ABAAAAAAAAABB', 'JABBBBAAAAAAAABAA']
    for test in test_list:
        result = joyStick(test)  
        print(result)