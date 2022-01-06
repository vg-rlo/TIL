# https://wwlee94.github.io/category/algorithm/bfs-dfs/travel-route/
from collections import defaultdict

def dfs(graph, start):
    route = []
    need_visit = [start]
    
    # 각 출발지를 두고 도착지 리스트를 순회
    while need_visit:
        node = need_visit[-1]
        if not graph[node]:
            route.append(need_visit.pop())
        else:
            need_visit.append(graph[node].pop(0))
    return route[::-1]

def solution(tickets):
    start = "ICN"
    graph = defaultdict(list)
    
    # 출발지, 도착지를 기준으로 graph 정의
    for departure, arrival in tickets:
        graph[departure].append(arrival)
        
    # 도착지를 이름 순으로 정렬
    for departure in graph.keys():
        graph[departure].sort()

    return dfs(graph, start)


if __name__ == '__main__':
    tickets_lst = [[["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]], \
        [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]], \
        [["ICN", "ATL"], ["ATL", "HND"], ["ATL", "IAD"], ['IAD', 'ATL']]]
    
    for i, tickets in enumerate(tickets_lst):
        print(solution(tickets))