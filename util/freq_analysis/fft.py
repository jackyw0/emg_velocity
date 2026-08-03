
from util.preprocessing.load_data import load_data
from util.preprocessing.remove_dc import remove_dc
from util.preprocessing.filters import bandpass


import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import ShortTimeFFT
from scipy.signal.windows import gaussian






def compute_fft(signal, fs):
    
    signal = signal - np.mean(signal)
    length_samples = len(signal)


    window = np.hanning(length_samples)
    windowed_signal = signal * window


    fft_values = np.fft.rfft(windowed_signal)


    frequencies = np.fft.rfftfreq(
        length_samples,
        d= 1 / fs
    )

    magnitude = (
        2.0
        / np.sum(window)
        * np.abs(fft_values)
    )

    return frequencies, magnitude

def compute_med_freq(freq, mag):
    power = mag ** 2
    cumulative_power = np.cumsum(power)
    total_power = cumulative_power[-1]

    median_freq_index = np.searchsorted(cumulative_power, total_power / 2)
    median_freq = freq[median_freq_index]

    return median_freq
   


def med_freq_window(signal, fs, window_ms = 250, overlap = 0.5):
    window_size = int(fs * window_ms /1000)
    step = int(window_size * (1 - overlap))
    
    median_freqs = []
    time_centers = []

    for start in range(0, len(signal) - window_size, step):
      window = signal[start:start + window_size]
      freq, mag = compute_fft(window, fs)
      median_freq = compute_med_freq(freq, mag)

      median_freqs.append(median_freq)
      time_centers.append((start + window_size / 2) / fs)

    return np.array(time_centers), np.array(median_freqs)


def spectrogram(
        fs, 
        signal
): 
    stft = ShortTimeFFT(gaussian(100, 20, sym=False), hop = 50, fs=fs)
    spectrogram_data = stft.spectrogram(signal)

    return stft, spectrogram_data

     
    







