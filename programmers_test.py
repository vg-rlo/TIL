import numpy as np

def solution(answers):
    answer = 0
    supoja = [[1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]]
    correct = []
    # ext_spj = []
        
    for spj in supoja:    
<<<<<<< HEAD
        ext_quot = len(spj) // len(answers) # 정수배 
        
        # 정수배 0일 때 = answers 길이가 spj보다 크거나 같을 때 
        if ext_quot == 0:
            ext_spj = spj + (ext_quot-1)*spj # 배수만큼 연장
            ext_remain = len(spj) % len(answers) 
            ext_spj = ext_spj + spj[:ext_remain] # 나머지만큼 연장
            print('answers 길이가 더 크거나 같을 때: ',ext)
            
        # 정수배가 0보다 클 때 = answers 길이가 spj보다 작을 때 
        else:
            ext = spj[:len(answers)] # 슬라이싱
            print('answers 길이가 더 작을 때: ',ext)
    
        # 각 원소끼리 정답 원소와 비교 
        ext_arr = np.array(ext)
        ans_arr = np.array(answers)
        ans = ans_arr[ext_arr == ans_arr]
=======
        extend_ans = []
        extend_len = len(spj) // len(answers) # 1, 1, 2
        if extend_len == 0:
            extend_ans = extend_ans[:len(answers)]
        else:
            extend_ans = answers + (extend_len-1)*answers
        extend_len = len(spj) % len(answers)
        extend_ans = extend_ans + answers[:extend_len]
    #     print(extend_ans)

        extend_ans = np.array(extend_ans)
        spj = np.array(spj)
        ans = spj[spj == extend_ans]
    #     print(ans)
    #     print('--')
>>>>>>> e9d51852d5907a5eaef097a972c824a0373a93b5
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
