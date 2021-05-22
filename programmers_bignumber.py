import itertools

def solution(numbers: list):
    answer = ''
    permuts = itertools.permutations(numbers, len(numbers))
    permuts_numbers = []

    for p in permuts:
        tostring = [str(i) for i in p]
        permuts_numbers.append("".join(tostring))

    answer = max(permuts_numbers)

    return answer

if __name__ == '__main__':
    numbers = [
        [6, 10, 2],         # result: 6210
        [3, 30, 34, 5, 9]   # result: 9534330
    ]

    result = [solution(num) for num in numbers]
    print(result)