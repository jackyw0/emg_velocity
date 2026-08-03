import matplotlib.pyplot as plt
from ..freq_analysis.fft import spectrogram
import numpy as np


def plot_freq(freq1, mag1, freq2, mag2):
  plt.figure(figsize=(12, 6))
  plt.plot(freq1, mag1, label="EMG Channel 1")
  plt.plot(freq2, mag2, label="EMG Channel 2")
  plt.xlabel("Frequency (hz)")
  plt.ylabel("Magnitude")
  plt.title("Frequency Spectrum")
  plt.grid(True, alpha=0.3)
  plt.legend()
  plt.tight_layout()


def plot_freq_overtime(time_cen1, median_freq1, time_cen2, median_freq2, signal, stft, spectrogram_data):
  fig, axes = plt.subplots(2, 1, figsize=(12, 6))

  axes[0].plot(time_cen1, median_freq1, label="EMG Channel 1 Median Freq overtime")
  axes[0].plot(time_cen2, median_freq2, label="EMG Channel 2 Median Freq overtime")
  axes[0].set_xlabel("Time (s)")
  axes[0].set_ylabel("Median Frequency (hz)")
  axes[0].set_title("Median Frequency Over Time")
  axes[0].grid(True, alpha=0.3)
  axes[0].legend()

  mesh = axes[1].pcolormesh(stft.t(len(signal)), stft.f, 10 * np.log10(spectrogram_data + 1e-10), shading="gouraud")
  axes[1].set_xlabel("Time (s)")
  axes[1].set_ylabel("Frequency (hz)")
  axes[1].set_title("Spectrogram using Short-Time Fourier Transform")
  axes[1].grid(True)
  fig.colorbar(mesh, ax=axes[1], label="Power(dB)")

  plt.tight_layout()