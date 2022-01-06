# https://data-marketing-bk.tistory.com/44
from collections import deque

def dfs(graph, root):
    need_visit = [root]
    visited = []

    while need_visit:
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
            # print(f"node: {node}, {graph[node]}")
            for adj_node in graph[node]:
                need_visit.append(adj_node)
    return list(visited)

def recursive_dfs(graph, start, visited = []):
    visited.append(start)

    for node in graph[start]:
        if node not in visited:
            recursive_dfs(graph, node, visited)
    return list(visited)

def bfs(graph, root): 
    need_visit = deque([root])
    visited = []

    while need_visit:
        node = need_visit.popleft()
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
    return list(visited)


if __name__ == "__main__":
    import sys
    from collections import defaultdict

    node, edge, root = map(int, sys.stdin.readline().split(" "))
    # print(f"node, edge, root: {node} {edge} {root}")

    graph = defaultdict(list)
    for _ in range(int(edge)):
        n, e = map(int, sys.stdin.readline().split(" "))
        graph[n].append(e) # 단방향
        graph[e].append(n) # 양방향
    
    # 간선의 번호 순서대로 방문
    for n in graph.keys():
        graph[n].sort()
    # print(graph)
    
    # print(dfs(graph, root))
    dfs_result = " ".join(map(str, recursive_dfs(graph, root)))
    bfs_result = " ".join(map(str, bfs(graph, root)))
    print(f"{dfs_result}")
    print(f"{bfs_result}")