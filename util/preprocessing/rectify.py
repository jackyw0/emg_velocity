import numpy as np

def rectify(signal: np.ndarray) -> np.ndarray:
    return np.abs(signal)