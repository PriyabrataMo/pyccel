#$ header function fib(int) results(int)
def fib(n) :
    if n < 2:
        result = n
        return result
    result = fib (n - 1) + fib (n - 2)
    return result
