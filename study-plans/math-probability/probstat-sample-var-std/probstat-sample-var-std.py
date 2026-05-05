import numpy as np

def sample_var_std(x):
    """
    Returns: dict with 'variance' and 'std_dev' as floats.
    """
    variance = float(np.var(x, ddof=1))
    std_dev = float(np.std(x, ddof=1))
    return {'variance': variance, 'std_dev': std_dev}