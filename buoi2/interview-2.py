def printPairs(array):
    for i in array:
        for j in array:
            print(str(i)+","+str(j))

import array
myArray = array.array('i',[2,2,3,4,4])
printPairs(myArray)