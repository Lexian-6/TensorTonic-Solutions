import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Returns: dict with 'mean', 'median', 'mode' as floats.
    """
    counts = Counter(x)
    return {'mean': np.mean(x), 'median': np.median(x), 'mode': max(counts, key=lambda x: counts[x])}