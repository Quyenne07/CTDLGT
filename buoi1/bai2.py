def firstMethod():
    secondMethod()
    print('I am the first Method')

def secondMethod():
    thirdMethod()
    print('I am the second Method')

def thirdMethod():
    fourMethod()
    print('I am the third Method')

def fourMethod():
    print('I am the fourth Method')

firstMethod()
    
