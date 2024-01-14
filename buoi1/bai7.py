def sumOfDigits(n):
    assert n >= 0 and int(n) == n, 'The number must be positive integer only'
    if n >= 0 and n < 10:
        return n
    else:
        return sumOfDigits(int(n/10))+ n%10
    
print(sumOfDigits(193))