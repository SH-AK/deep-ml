def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    num_features = len(vectors)
    if num_features == 0:
        return []

    num_observations = len(vectors[0])
    if num_observations <= 1:
        return [[0.0] * num_features for _ in range(num_features)]

    # Calculate means for each feature
    means = [sum(feature) / num_observations for feature in vectors]

    # Initialize covariance matrix
    cov_matrix = [[0.0] * num_features for _ in range(num_features)]

    # Compute pairwise sample covariance: Cov(X, Y) = sum((X_i - mean_X) * (Y_i - mean_Y)) / (n - 1)
    for i in range(num_features):
        for j in range(i, num_features):
            cov = sum(
                (vectors[i][k] - means[i]) * (vectors[j][k] - means[j])
                for k in range(num_observations)
            ) / (num_observations - 1)
            
            cov_matrix[i][j] = cov
            cov_matrix[j][i] = cov

    return cov_matrix