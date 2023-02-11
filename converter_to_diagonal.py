from simple_iterator import SimpleIterator


class ConversionResult:
    result: bool
    matrix: list[list[float]]

    def __init__(self, result: bool, matrix: list[list[float]]):
        self.result = result
        self.matrix = matrix


def check_if_diagonal_predominant(matrix: list[list[float]]) -> bool:
    num_of_eq: int = 0
    for i in range(len(matrix)):
        abs_row_sum: float = 0
        for j in range(len(matrix)):
            abs_row_sum += abs(matrix[i][j])
        abs_row_sum -= abs(matrix[i][i])
        if abs(matrix[i][i]) < abs_row_sum:
            return False
        elif abs(matrix[i][i]) == abs_row_sum:
            num_of_eq += 1
    if num_of_eq == len(matrix):
        return False
    return True


def try_to_convert_to_diagonal_predominant(iterator: SimpleIterator) -> ConversionResult:
    new_matrix: list = [[] for i in range(iterator.n)]
    matrix = iterator.matrix
    for eq in matrix:
        max_in_row: float = max(list(map(abs, eq))[:-1:])
        mx_ind: int = 0
        for i in range(iterator.n):
            if abs(eq[i]) == max_in_row:
                mx_ind = i
                break
        if len(new_matrix[mx_ind]) > 0:
            return ConversionResult(False, [])
        new_matrix[mx_ind] = eq
    if check_if_diagonal_predominant(new_matrix):
        return ConversionResult(True, new_matrix)
    return ConversionResult(False, [])
