import numpy as np

def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
    # Convert inputs to NumPy arrays
    X_mat = np.array(X)
    y_vec = np.array(y)
    
    # Calculate theta using the Normal Equation: (X^T * X)^(-1) * X^T * y
    theta = np.linalg.inv(X_mat.T @ X_mat) @ X_mat.T @ y_vec
    
    # Round results to 4 decimal places
    return np.round(theta, 4).tolist()