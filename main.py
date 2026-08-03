from util.preprocessing.load_data import load_data
from util.preprocessing.remove_dc import remove_dc
import numpy as np
import matplotlib.pyplot as plt
from util.time_analysis.correlation import estimate_delay
from util.time_analysis.velocity import calculate_velocity
from util.plots.plot_signal_time import plot_signal, plot_cor, plot_features
from util.preprocessing.filters import bandpass, notch
from util.freq_analysis.fft import compute_fft, med_freq_window, spectrogram
from util.time_analysis.time_features import extract_features, features_windowed
from util.plots.plot_signal_freq import plot_freq, plot_freq_overtime


fs = 848



#read emg data
#read_emg()

filename = "data/emg_data_1785291094.csv"
df = load_data(filename)

#time_ms = df["time_ms"].values.astype(float)
#actual_fs = 1000 / np.mean(np.diff(time_ms))
#print("Actual sample rate:", actual_fs, "Hz")


#remove dc
signal1 = remove_dc(df["ch1_v"].values)
signal2 = remove_dc(df["ch2_v"].values)



time_samples = np.arange(len(signal1)) / fs

#estimate time delay between signals 
(
    delay_seconds,
    delay_samples,
    peak_correlation,
    correlation,
    lags
) = estimate_delay(signal1, signal2, fs)

print("Detected delay of samples:", delay_samples, "samples")
print("Detected delay in time:", delay_seconds * 1000, "ms")
print("Peak correlation:", peak_correlation)



#calculate velocity 
distance_m = 0.079
velocity = calculate_velocity(distance_m, delay_seconds)
print("Velocity", velocity, "m/s")


#filters: low-pass, high-pass, and notch

signal1 = notch(
  signal1, 
  fs=fs, 
  notch_freq = 60.0,
  quality = 10.0
)

signal2 = notch(
  signal2, 
  fs=fs, 
  notch_freq = 59.0,
  quality = 5.0
)


signal1 = bandpass(
    signal1,
    fs=fs,
    lowcut=20,
    highcut=420
)

signal2 = bandpass(
    signal2,
    fs=fs,
    lowcut=20,
    highcut=420
)






#extract features of signal & plot signal, rms 

features1 = features_windowed(signal1, fs)
features2 = features_windowed(signal2, fs)

rms1 = features1[0]
rms2 = features2[0]

mav1 = features1[1]
mav2 = features2[1]

plot_signal(signal1, signal2, time_samples)

time_rms = np.arange(len(rms1)) / fs 
time_mav = np.arange(len(mav1)) / fs
plot_features(rms1, rms2, time_rms, mav1, mav2, time_mav)


#plot correlation
#plot_cor(lags, correlation, fs, delay_samples)



#extract frequency spectrum
(freq1, mag1) = compute_fft(signal1, fs)
(freq2, mag2) = compute_fft(signal2, fs)

#extract median frequency overtime
(time_cen1, median_freq1) = med_freq_window(signal1, fs)
(time_cen2, median_freq2) = med_freq_window(signal2, fs)

 


#plot frequency spectrum & median freq overtime
plot_freq(freq1, mag1, freq2, mag2)

#spectrogram and stft
(stft1, spectrogram_data1) = spectrogram(fs, signal1)
plot_freq_overtime(time_cen1, median_freq1, time_cen2, median_freq2, signal1, stft1, spectrogram_data1)
plt.show();










