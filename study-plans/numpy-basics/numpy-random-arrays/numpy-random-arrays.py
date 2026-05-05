import numpy as np

def generate_random_array(shape, kind, seed):
    """
    Returns: 2D ndarray of float64 random values
    """
    # # Modern Solution:
    # rng = np.random.default_rng(seed=seed)
    # if kind == 'uniform':
    #     return rng.random(shape, dtype=np.float64)
    # return rng.standard_normal(shape, dtype=np.float64)
    np.random.seed(seed)
    if kind == 'uniform':
        return np.random.random(shape)
    return np.random.standard_normal(shape)