# find F at 'n' position
import time
start_time = time.time()
def fibonacci(n):
    alist = [None]*(n+1)
    alist[0] = 0
    alist[1] = 1
 
    for i in range(2,n+1):
        alist[i] = alist[i-1] + alist[i-2]
    return alist[n]

n = int(input())
print(fibonacci(n))
print("--- %s seconds ---" % (time.time() - start_time))