# Create a 3x3x3 matrix using lists with jumbled inputs
matrix = [
    [
        [1, 2, 3],  # 1st 2D slice (first layer)
        [4, 5, 6],
        [7, 8, 9]
    ],
    [
        [10, 11, 12],  # 2nd 2D slice (second layer)
        [13, 14, 15],
        [16, 17, 18]
    ],
    [
        [19, 20, 21],  # 3rd 2D slice (third layer)
        [22, 23, 24],
        [25, 26, 27]
    ]
]

# Print the entire 3D matrix
print("3D Matrix:")
for layer in matrix:
    print(layer)

# Print the 2D matrices (slices) along the first axis
print("\n2D slices along the first axis:")
for i in range(len(matrix)):
    print(f"Slice {i}: {matrix[i]}")

# Print the 2D matrices (slices) along the second axis
print("\n2D slices along the second axis:")
for i in range(3):
    slice_2d = [[matrix[x][i][y] for y in range(3)] for x in range(3)]
    print(f"Slice {i}: {slice_2d}")

# Print the 2D matrices (slices) along the third axis
print("\n2D slices along the third axis:")
for i in range(3):
    slice_2d = [[matrix[x][y][i] for y in range(3)] for x in range(3)]
    print(f"Slice {i}: {slice_2d}")
