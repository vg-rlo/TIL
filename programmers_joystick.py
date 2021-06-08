from collections import deque

def joyStick(name):
    """
    ▲ - 다음 알파벳
    ▼ - 이전 알파벳 (A에서 아래쪽으로 이동하면 Z로)
    ◀ - 커서를 왼쪽으로 이동 (첫 번째 위치에서 왼쪽으로 이동하면 마지막 문자에 커서)
    ▶ - 커서를 오른쪽으로 이동
    """

    move_cnt = 0
    cnt = 0
    start = ord('A')
    end = ord('Z')

    # ord(ch)-start
    # 0이 아닌 원소를 찾기
    # name = deque(name) 
    name = [chr for chr in name]
    print(name)

    notA_idx = [i+1 if name[i] != 'A' else 0 for i in range(len(name))] # A면 0, 나머지는 index + 1
    print(notA_idx)

    while(1):
        # 리스트 길이가 다 0 이거나 모두 A 요소 이면 
        # if len(name_ord) == 0 or sum(name_ord) == 0:
        #     print('breakpoint:', len(name_ord))
        #     print('breakpoint:', sum(name_ord))
        #     break

        notA_right = min(notA_idx) # A가 아닌 요소까지 오른쪽으로 움직여야하는 커서 위치 
        notA_left = len(notA_idx) - max(notA_idx) + 1 # A가 아닌 요소까지 왼쪽으로 움직여야하는 커서 위치
        print(notA_right, notA_left)

        # 커서 이동의 결정
        # if name_ord[0] == 0 and name_ord == :
        # print(name_ord)
        break

        # move_up = ord(name_ord[0])-start
    #     if move_up != 0: 
    #         move_down = (end - start + 1) - move_up
    #         print(move_up, move_down)

    #     if move_up >= move_down:
    #         move_min = move_down
    #     else:
    #         move_min = move_up

    #     move_cnt = move_cnt + move_min
    #     print(move_cnt)

    # return move_cnt

if __name__ == '__main__':
    joyStick('JAZ')