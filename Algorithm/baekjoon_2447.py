# 재귀 알고리즘
# 필사 블로그 - https://yeol2.tistory.com/38
def make_mat(pattern):
    mat = []
    for i in range(3*len(pattern)):
        if i//len(pattern) == 1:
            mat.append(pattern[i%len(pattern)]+" "*len(pattern)+pattern[i%len(pattern)])
        else:
            mat.append(pattern[i%len(pattern)]*3)
    return (list(mat))

if __name__ == "__main__":
    base_pattern = ["***", "* *", "***"]
    n = int(input())
    k = 0

    while (n != 3):
        # n = n//3
        n = int(n/3)
        k += 1

    for i in range(k):
        base_pattern = make_mat(base_pattern)
        
    for p in base_pattern:
        print(p)