import itertools

def solution(numbers: list):
    answer = ''
    
    num2str = list(map(str, numbers))

    num2str.sort(key = lambda x:x*3, reverse=True)
    answer = str(int(answer.join(num2str)))

    return answer

if __name__ == '__main__':
    numbers = [
        [6, 10, 2],         # result: 6210
        [3, 30, 34, 5, 9],  # result: 9534330
        [3, 33, 1, 330],    # result: 3333301
        [0, 1, 110, 10, 1000] # result: 11101010000
    ]

    result = [solution(num) for num in numbers]
    print(result)