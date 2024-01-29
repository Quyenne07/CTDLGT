def foo(li):
    product = 1
    for i in li:
        product *= i
    print("Sum="+str(sum(li))+",Product="+str(product))

myList= [1,2,3,4]
foo(myList)