#bai1.Create an array and traverse
def traverse(array):
    for el in array:
        print(el)

#bai2.Access individual elements through indexes
def accessThroughIndex(array,index):
    print(array[index])

#bai3.Append any value to the array using append() method
def appendToArray(array,value):
    array.append(value)

#bai4.Insert value in an array using insert() method
def insertToArray(array,value):
    array.insert(0,value)

#bai5.Extend python array using extend method
def extendArray(array,newArray):
    array.extend(newArray)

#bai6.Add items from list into array using fromlist() method
def addItems(array,items):
    array.fromlist(items)

#bai7.Remove any array element using remove() method
def removeArray(array,value):
    array.remove(value)

#bai8.Remove last array element using pop() method
def removeLastOfArray(array):
    array.pop()

#bai9.Fetch any element through its index using index() method
def findIndex(array,value):
    return array.index(value)

#bai10.Reverse a python array using reverse() method
def reverseArray(array):
    array.reverse()

#bai11.Get array buffer information through buffer_info() method
def bufferInfoArray(array):
    return array.buffer_info()

#bai12.Check for number of occurrences of an element using count() method
def countInArray(array,value):
    return array.count(value)

#bai13.Convert array to string using toString() method
def convertString(array):
   resultStr= ""
   for el in array:
       resultStr +=str(el)
    return resultStr

#bai14.Convert array to a python list with same elements using tolist() method
def convertList(array):
    return array.toList()

#bai15.Append a string to char array using fromstring() method
def appendStrongToCharArray(array,tmpStr):
    return np.append(array,[tmpStr],axis=0)

#bai16.Slice elements from an array
def sliceArray(array,fristE1,lastE1):
    return array[fristE1:lastE1]
     
    
    
    
