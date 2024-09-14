
matrix = [[[1, 2, 3],[4, 5, 6],[7, 8, 9]],[[10, 11, 12],[13, 14, 15],[16, 17, 18]],[[19, 20, 21],[22, 23, 24],[25, 26, 27]]]

print("Slicing the first two rows and two columns from the first 2D layer (matrix[0][:2][:2]):")
print(matrix[0][:2][:2])  # Output: [[1, 2], [4, 5]]


print("\nSlicing the second element of the second row from all layers (matrix[:][1][1]):")
print([matrix[i][1][1] for i in range(3)])  # Output: [5, 14, 23]

print("\nSlicing first and second layers (matrix[:2]):")
print(matrix[:2])  # Output: Two layers (1st and 2nd)

print("\nSlicing the third column from all layers (matrix[:][:][2]):")
print([matrix[i][j][2] for i in range(3) for j in range(3)])  # Output: [[3, 6, 9], [12, 15, 18], [21, 24, 27]]

print("\nSlicing the second row from the second and third layers (matrix[1:3][1]):")
print(matrix[1:3][1])  # Output: [[13, 14, 15], [22, 23, 24]]

print("\nSlicing the first two elements from each row in the third layer (matrix[2][:][:2]):")
print(matrix[2][:][:2])  # Output: [[19, 20], [22, 23], [25, 26]]

