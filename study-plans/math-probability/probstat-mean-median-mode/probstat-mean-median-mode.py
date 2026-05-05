import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Returns: dict with 'mean', 'median', 'mode' as floats.
    """
    counts = Counter(x)
    for i in counts:
        if counts[i] == max(counts.values()):
            return {'mean': np.mean(x), 'median': np.median(x), 'mode': i}