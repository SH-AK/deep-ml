import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
    arr = np.array(a)
    
    # Check if total elements in the original matrix match the required shape size
    if arr.size != new_shape[0] * new_shape[1]:
        return []
    
    # Reshape and convert back to a standard Python list
    return arr.reshape(new_shape).tolist()