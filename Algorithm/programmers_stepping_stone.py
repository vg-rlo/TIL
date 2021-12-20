from itertools import combinations

def solution(distance, rocks, n):
    '''
    distance(int): 출발지점에서 도착지점까지의 거리
    rocks(list): 바위들이 있는 위치
    n(int): 제거할 바위의 수
    '''
    answer = 0
    sorted_rocks = list(sorted(rocks))

    between_dist_min = []
    for i, j in combinations(rocks, 2):
        filtered_rocks = sorted_rocks[:]
        filtered_rocks.remove(i)
        filtered_rocks.remove(j)

        between_dist = []
        for idx, num in enumerate(filtered_rocks):
            # print(i, j)
            if idx == 0:
                between_dist.append(num)
            else:
                between_dist.append(num-filtered_rocks[idx-1])
                if idx == len(filtered_rocks)-1:
                    between_dist.append(distance-num)
        # print(between_dist)
        between_dist_min.append(min(between_dist))

    answer = max(between_dist_min)
    return answer