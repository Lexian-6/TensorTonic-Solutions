import numpy as np

def percentiles(x, q):
    """
    Returns: numpy array of percentile values.
    """
    # return np.array([np.percentile(x, quantile) for quantile in q], dtype=float)
    return np.percentile(x, q)