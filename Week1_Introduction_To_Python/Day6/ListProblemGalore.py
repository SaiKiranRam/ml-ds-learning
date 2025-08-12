# Problem Statement - Finding maximum value in a 2 D list.


# def find_max_value(matrix):
#     max_value = matrix[0][0]
#     for row in matrix:
#         for elm in row:
#             if max_value < elm:
#                 max_value = elm
#     return max_value

def find_max_value(matrix):
    max_value = matrix[0][0]
    for row in matrix:
        max_value = max(max_value, max(row))
    return max_value



matrix = [
    [3, 7, 1, 2],
    [8, 5, 6, 4],
    [2, 1, 8, 9]
]

max_value = find_max_value(matrix)
print("\nMaximum Value:", max_value)