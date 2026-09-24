import numpy as np

def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    arr = np.array(matrix)
    
    if mode == 'row':
        means = np.mean(arr, axis=1)
    elif mode == 'column':
        means = np.mean(arr, axis=0)
    else:
        raise ValueError("Mode must be either 'row' or 'column'")
        
    return means.tolist()