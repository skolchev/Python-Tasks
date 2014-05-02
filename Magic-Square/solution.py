def magic_square(matrix):
    length = len(matrix)
    total_sum = sum(matrix[0])

    # Check rows
    for row in matrix:
        if total_sum != sum(row):
            return False

    # Check columns
    for x in range(0, len(matrix)):
        column = [matrix[x][y] for y in range(0, len(matrix))]
        if total_sum != sum(column):
            return False

    # Check forward diagonal
    diagonal = [matrix[x][x] for x in range(length)]
    if sum(diagonal) != total_sum:
        return False

    # Check backward diagonal
    reverse_diagonal = [matrix[x][y] for x, y in zip(range(length), reversed(range(length)))]
    if sum(reverse_diagonal) != total_sum:
        return False

    return True
