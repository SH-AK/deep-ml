import numpy as np

def feature_scaling(data: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    # Calculate mean and standard deviation along columns (axis 0)
    mean = np.mean(data, axis=0)
    std = np.std(data, axis=0)
    
    # Calculate min and max along columns (axis 0)
    min_val = np.min(data, axis=0)
    max_val = np.max(data, axis=0)
    
    # Standardization: (X - mean) / std
    standardized_data = (data - mean) / std
    
    # Min-Max Normalization: (X - min) / (max - min)
    normalized_data = (data - min_val) / (max_val - min_val)
    
    # Round results to 4 decimal places
    standardized_data = np.round(standardized_data, 4)
    normalized_data = np.round(normalized_data, 4)
    
    return standardized_data, normalized_data