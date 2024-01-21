def reverse(array):
    for i in range(0,int(len(array)/2)):
        other = len(array)-i-1
        temp = array[i]
        array[i]= array[other]
        array[other] = temp
    print(array)

import array
myArray = array.array('i',[2,2,3,4,4])
reverse(myArray)