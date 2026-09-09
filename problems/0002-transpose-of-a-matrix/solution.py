def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    trans = [[a[i][j] for i in range(len(a))] for j in range(len(a[0]))]
    return trans 