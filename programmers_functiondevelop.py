from math import ceil as ceil 

def funcDevelop(progresses: list, speeds: list):
    answer = []
    power =  int # 일률(power): 힘 x 속도 
    nums = len(progresses) # 작업량 

    remain = [100-i for i in progresses] # 남은 작업 %
    date = [ceil(r/s) for r, s in zip(remain, speeds)] # 필요 일수

    i = 1 
    done = 1
    state = date[0]
    while(1):
        if date[i] <= state:
            done += 1 
        else: 
            answer.append(done)
            state = date[i]
            done = 1        
        i += 1
        # iterations가 전체 progresses 다 고려하면 break
        if i == nums: 
            answer.append(done)
            break   
        # print(done)
    return answer

if __name__ == '__main__': # program started
    p1 = [93, 30, 55]
    p2 = [95, 90, 99, 99, 80, 99]
    s1 = [1, 30, 5]
    s2 = [1, 1, 1, 1, 1, 1]

    print(funcDevelop(p1, s1))
    print(funcDevelop(p2, s2))
