def solution(brown, yellow):
    answer = []

    for y in range(1, int(yellow**(1/2))+1):
        if yellow % y == 0:
            quot = yellow // y 
            b = quot*2 + y*2 + 4 
            if b == brown:
                pattern = [quot, y]
                answer = [quot+2, y+2]
    # print(brown, '-', yellow,':',pattern)

    return answer

if __name__ == '__main__':
    browns = [10, 8, 24]
    yellows = [2, 1, 24]
    # answer = [4,3], [3,3], [8,6]

    for inp in zip(browns, yellows):
        print(solution(inp[0], inp[1]))