def submatrix(matrix, i, j):
    return [row[:j] + row[j+1:] for row in (matrix[:i] + matrix[i+1:])]

def determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        det = 0
        for j in range(len(matrix)):
            det += (-1) ** j * matrix[0][j] * determinant(submatrix(matrix, 0, j))
        return det

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#     m1 = (-1)**(1+1) 
#     for j in range(len(matrix)):
#         for k in range(len(matrix)):
#             if len(matrix)==1:
#                 return matrix[j][k]
#             elif len(matrix)==2:
#                 return matrix[j][k]*matrix[j][k]
#     if len(matrix)==1:
#         return matrix[0][0]
#     elif len(matrix)==2:
#         return matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
#     elif len(matrix)==3:
#         return (matrix[0][0]*matrix[1][1]*matrix[2][2]) + (matrix[0][1]*matrix[1][2]*matrix[2][0]) + (matrix[0][2]*matrix[1][0]*matrix[2][1]) - (matrix[0][2]*matrix[1][1]*matrix[2][0]) - (matrix[0][1]*matrix[1][0]*matrix[2][2]) - (matrix[0][0]*matrix[1][2]*matrix[2][1])
#     elif len(matrix)==4:
#         return 0
# #     return matrix
#     for i in matrix:
#         if len(matrix)==2:
#             return matrix[0]*matrix[3]-matrix[1]*matrix[2]
#         else:
#             pass
