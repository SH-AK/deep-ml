def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float] | int:
    if not a or len(a[0]) != len(b):
        return -1
    c = []
    for row in a:
        row_sum = sum(row[i] * b[i] for i in range(len(b)))
        c.append(row_sum)
        
    return c