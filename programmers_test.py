import numpy as np

def solution(answers):
    supoja = [[1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]]
    # answers = [1,2,3]
    correct = []

    for spj in supoja:    
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
        correct.append(len(ans))

    correct = np.array(correct)
    # print(correct)
    # print()

    correct = np.where(correct > 0)[0] + np.array(1)# tuple
    # print(correct)

    answer = correct.tolist()
#     print(sorted(answer))

    return answer
