def power(n:float, k:int):
    assert n >= 0 and isinstance(float(n),float),'The number must be positive number'
    assert k >= 0 and isinstance(k,int),'The number of exponent must be greater than 0 and is integer'
    if k == 0:
        return n
    else:
        return n*power(n,k-1)
    
print(power(3,3))