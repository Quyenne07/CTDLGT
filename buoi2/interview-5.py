def printUnorderedPairs2(arrayA,arrayB):
    for i in range(len(arrayA)):
        for j in range(len(arrayB)):
            for k in range(0,100000):
                print(str(arrayA[i])+","+str(arrayB[j]))

import array
myArray1 = array.array('i',[2,2,3,4,4])
myArray2 = array.array('i',[1,2,3,4,5])
printUnorderedPairs2(myArray1,myArray2)