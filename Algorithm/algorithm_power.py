def power(a, n):
    ans = 1
    for _ in range(n):
        ans *= a

    return ans 

def recursive_power(a, n):
    if n == 1:
        return a
    return recursive_power(a, n-1)*a

def divide_conquer_power(a, n):
    if n == 0:
        return 1
    
    x = divide_conquer_power(a, n//2)

    if n % 2 == 0:
        return x * x
    
    else:
        return x * x * a


if __name__ == "__main__":
    import time 
    
    a = 234233240
    n = 10000

    # test 1
    start_time = time.process_time()
    try: 
        power(a,n)
    except:
        print("연산 불가")
    end_time = time.process_time()
    print(f"time elapsed: {int(round((end_time-start_time)*1000))}ms")

    # test 2
    start_time = time.process_time()
    try: 
        recursive_power(a,n)
    except:
        print("연산 불가")   
    end_time = time.process_time()
    print(f"time elapsed: {int(round((end_time-start_time)*1000))}ms")

    # test 3
    start_time = time.process_time()
    try: 
        divide_conquer_power(a,n)
    except:
        print("연산 불가")   
    end_time = time.process_time()
    print(f"time elapsed: {int(round((end_time-start_time)*1000))}ms")