def solution(begin, target, words):
    answer = 0
    stacks = [begin]
    visit = [0]*len(words)

    if target not in words:
        return 0
    
    # bfs
    while stacks:
        stack = stacks.pop()
        if stack == target:
            return answer
        
        for i in range(len(words)):
            if len([j for j in range(len(words[i])) if words[i][j] != stack[j]]) == 1:
                if visit[i] != 0:
                    continue
                visit[i] = 1
                stacks.append(words[i])
        answer += 1
    return answer


if __name__ == '__main__':
    begin = "hit"
    target = "cog"
    words = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(solution(begin, target, words))