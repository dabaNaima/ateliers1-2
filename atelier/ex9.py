def indixer(matrix,element):
    index=[]
    i,j=0,0
    while i < len(matrix):
        j=0
        while j<len(matrix[0]):
            if matrix[i][j]==element:
                index=[i+1,j+1]
            j+=1
        i+=1     
    return index 

matrix=[[1,3],[66,7]]

print("les indices  de 66 sont ,",indixer(matrix,66))

