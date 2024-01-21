def foo(array):
    sum = 0
    product = 1
    for i in array:
        sum += i
    for i in array:
        product *= i
    print("Sum = "+str(sum)+", Product ="+str(product))
import array
myArray = array.array('i',[2,2,3,4,4])
foo(myArray)