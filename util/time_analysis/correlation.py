import numpy as np
from scipy.signal import correlate, correlation_lags
from util.preprocessing.remove_dc import remove_dc

def estimate_delay(signal1, signal2, fs, max_delay_ms=20):
  signal1 = np.array(signal1)
  signal2 = np.array(signal2)

  if signal1.shape != signal2.shape:
    raise ValueError("signals have different lengths")

  a = remove_dc(signal1)
  b = remove_dc(signal2)

  correlation = correlate(b, a, mode="full")
  lags = correlation_lags(len(a), len(b), mode="full")

  max_lag_samples = int(max_delay_ms * fs / 1000)
  valid = np.abs(lags) <= max_lag_samples

  denominator = np.linalg.norm(a) * np.linalg.norm(b)
  correlation = correlation / denominator

  correlation = correlation[valid]
  lags = lags[valid]

  best_index = np.argmax(correlation)

  peak_correlation = correlation[best_index]
  delay_samples = lags[best_index]
  delay_seconds = delay_samples / fs

  return delay_seconds, delay_samples, peak_correlation, correlation, lags