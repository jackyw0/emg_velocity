import numpy as np


def envelope(
        signal: np.ndarray,
        fs: float,
        window_seconds: float = 0.2
    ) -> np.ndarray:
          window_samples = int(fs * window_seconds)

          if window_samples < 1:
              raise ValueError("Window must contain at least one sample")

          kernel = np.ones(window_samples) / window_samples

          return np.convolve(signal, kernel, mode="same")