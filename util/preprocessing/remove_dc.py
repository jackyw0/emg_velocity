import numpy as np

def remove_dc(signal: np.ndarray):

    return signal - np.mean(signal)