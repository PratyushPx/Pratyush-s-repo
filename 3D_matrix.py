matrix = [[[1, 2, 3], [4, 5, 6],[7, 8, 9]],[[10, 11, 12],[13, 14, 15],[16, 17, 18]],[[19, 20, 21],[22, 23, 24], [25, 26, 27]]]


print("3D Matrix:")
for layer in matrix:
    print(layer)


print("\n2D slices along the first axis:")
for i in range(len(matrix)):
    print(f"Slice {i}: {matrix[i]}")


print("\n2D slices along the second axis:")
for i in range(3):
    slice_2d = [[matrix[x][i][y] for y in range(3)] for x in range(3)]
    print(f"Slice {i}: {slice_2d}")


print("\n2D slices along the third axis:")
for i in range(3):
    slice_2d = [[matrix[x][y][i] for y in range(3)] for x in range(3)]
    print(f"Slice {i}: {slice_2d}")
