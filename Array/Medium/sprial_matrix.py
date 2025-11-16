"""
print sprial matrix
there is one 2d array
1,2,3,4
5,6,7,8
9,10,11.12
13,14,15,16




output should be 1,2,3,4,8,12,16,15,14.13,9,5,6,7,11,10
"""
def sprialMatrix(matrix):
    startRow,endRow=0,matrix.len()-1
    startCol,endCol=matrix[0].len()-1
    while startRow<=endRow and startCol<=endCol:
        # first print outer col top col
        for j in range(endCol):
            print(matrix[0])
matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(sprialMatrix(matrix))