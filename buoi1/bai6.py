def fibonacci(n):
    assert n>=0 and int(n) == n, 'The number must be positive integer only!'
    if n in [1,2]:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
print(fibonacci(4))