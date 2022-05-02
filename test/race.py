d = {1: 1, 2: 1}


def fib(n):
    if n <= 2:
        return
    fib(n - 1)
    d[n] = d[n - 1] + d[n - 2]
    return d[n]


print(fib(900))
