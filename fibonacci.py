'''
https://leetcode.com/problems/fibonacci-number/description/
1 1 2 3 5 8
'''
import timeit

recursivecode = '''
def recursiveway(n):
    if n == 1 or n == 2:
        return 1
    else:
        return recursiveway(n-1) + recursiveway(n-2)
recursiveway(20)
'''

iterativecode = '''
def iterativeway(n):
    arr = [1, 1]
    if (n == 1 or n == 2):
        return 1
    for _ in range(n-2):
        arr.append(arr[-1] + arr[-2])
    return arr[-1]
iterativeway(20)
'''

kstore : dict = {1: 1, 2: 1}

def memoization(n):
    global kstore
    if n in kstore.keys():
        return kstore[n]
    else:
        x1 = kstore[n-1] if n-1 in kstore.keys() else memoization(n-1)
        kstore[n-1] = x1
        x2 = kstore[n-2] if n-2 in kstore.keys() else memoization(n-2)
        kstore[n-2] = x2

        return x1 + x2
memoization(20)


if __name__ == "__main__":
    """
    Output:
    
    Executing code 10000 times to get statistically accurate results:
    Recursive code takes: 33.4439451 seconds
    Iterative code takes: 0.06786699999999968 seconds
    Memoization code takes: 0.007335900000001061 seconds
    """
    n = 10000
    print(f"Executing code {n} times to get statistically accurate results:")
    print(f"Recursive code takes: {timeit.timeit(stmt= recursivecode, number= 10000)} seconds")
    print(f"Iterative code takes: {timeit.timeit(stmt= iterativecode, number= 10000)} seconds")
    print(f"Memoization code takes: {timeit.timeit(stmt= 'memoization(20)', number= 10000, globals=globals())} seconds")