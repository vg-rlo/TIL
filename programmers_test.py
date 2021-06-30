import numpy as np

def solution(answers):
    answer = 0
    supoja = [[1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]]
    correct = []
    # ext_spj = []
        
    for spj in supoja:    
        ext_quot = len(spj) // len(answers) # 정수배 
        
        # 정수배 0일 때 = answers 길이가 spj보다 크거나 같을 때 
        if ext_quot == 0:
            ext_spj = spj + (ext_quot-1)*spj # 배수만큼 연장
            ext_remain = len(spj) % len(answers) 
            ext_spj = ext_spj + spj[:ext_remain] # 나머지만큼 연장
            print('answers 길이가 더 크거나 같을 때: ',ext_spj)
            
        # 정수배가 0보다 클 때 = answers 길이가 spj보다 작을 때 
        else:
            ext_spj = spj[:len(answers)] # 슬라이싱
            print('answers 길이가 더 작을 때: ',ext_spj)
    
        # 각 원소끼리 정답 원소와 비교 
        ext_arr = np.array(ext_spj)
        ans_arr = np.array(answers)
        ans = ans_arr[ext_arr == ans_arr]

        correct.append(len(ans))
        print(correct)

    correct_arr = np.array(correct)
    print(correct_arr)
    correct_arr = np.where(correct_arr > 0)[0] + np.array(1) # tuple
    print(correct_arr)
    
    answer = correct_arr.tolist()
    answer = sorted(answer)
    # print(sorted(answer))

    return answer
