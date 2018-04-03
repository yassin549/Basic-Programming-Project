# Added iterative solution
def fibonacci_iterative(n):
    if n <= 1: return n
    a, b = 0, 1
    for _ in range(n-1):
        a, b = b, a + b
    return b
# Updated on 2019-05-15 00:00:00