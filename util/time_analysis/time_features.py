import numpy as np


def features_windowed(signal, fs, window_ms = 250, overlap = 0.5):
    window_size = int(fs * window_ms /1000)
    step = int(window_size * (1 - overlap))
    
    rms_values = []
    mav_values = []

    for start in range(0, len(signal) - window_size, step):
      window = signal[start:start + window_size]

      rms_values.append(np.sqrt(np.mean(window**2)))
      mav_values.append(np.mean(np.abs(window)))


    return np.array(rms_values), np.array(mav_values)
  
