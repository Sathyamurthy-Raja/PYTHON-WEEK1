def determinant(matrix):
    return int(matrix[0][0]) * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1]) - int(matrix[0][1]) * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0]) + int(matrix[0][2]) * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])

matrixa = [[1,2,3],[4,5,6],[7,8,9]]
result = determinant(matrixa)
print("Determinant :",result)







