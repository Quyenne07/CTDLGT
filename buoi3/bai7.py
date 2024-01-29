def rotateMatrix(matrix):
    n=len(matrix)
    for layer in range(n//2):
        first, last = layer,n-1-layer
        for i in range(first,last):
            #temp = top[i]
            temp = matrix[layer][i]
            #top[i]=left[i]
            matrix[layer][i]=matrix[-i-1][layer]
            #left[i]=bottom[i]
            matrix[-i-1][layer]=matrix[-layer-1][-i-1]
            #bottom[i]=right[i]
            matrix[-layer-1][-i-1]=matrix[i][-layer-1]
            #right[i]=temp
            matrix[i][-layer-1]=temp

if __name__=='__main__':
    matrix = ([[2,2,3],[3,3,4],[4,4,5]])
    rotateMatrix(matrix)
    for row in matrix:
        print(row)