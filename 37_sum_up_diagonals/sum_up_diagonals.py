def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    column_len = len(matrix)
    left_diagonal = 0
    right_diagonal = 0

    for index in range(column_len):
        backwards_index = -1 * (index + 1)
        left_diagonal += matrix[index][index];
        right_diagonal += matrix[index][backwards_index];
    return left_diagonal + right_diagonal

# Some More Tests
# print(sum_up_diagonals([[1,2,3], [2,4,6], [3,6,9]]))
# print(sum_up_diagonals([[1,5], [2,10]]))
# print(sum_up_diagonals([[2,1], [9,8]]))