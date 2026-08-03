import matplotlib.pyplot as plt

def plot_signal(signal1, signal2, time):
  plt.figure(figsize=(12,6))

  plt.plot(time, signal1, label="EMG Channel 1")
  plt.plot(time, signal2, label="EMG Channel 2")

  plt.xlabel("Time(s)")
  plt.ylabel("Amplitude")
  plt.title("EMG Signals over Time")
  plt.grid(True)
  plt.legend()
  

def plot_features(rms1, rms2, time_rms, mav1, mav2, time_mav):
    fig, axes = plt.subplots(2, 1, figsize=(12,6), sharex=True, sharey=True)

    axes[0].plot(time_rms, rms1, label="RMS EMG Channel 1")
    axes[0].plot(time_rms, rms2, label="RMS EMG Channel 2")
    axes[0].set_xlabel("Time(s)")
    axes[0].set_ylabel("Amplitude")
    axes[0].set_title("RMS EMG values over Time")
    axes[0].grid(True, alpha=0.3)
    axes[0].legend()

    axes[1].plot(time_mav, mav1, label="MAV EMG Channel 1")
    axes[1].plot(time_mav, mav2, label="MAV EMG Channel 2")
    axes[1].set_title("MAV EMG values over Time")
    axes[1].grid(True, alpha=0.3)
    axes[1].legend()
    

  

def plot_cor(lags, correlation, fs, delay_samples):
  lags_ms = lags * fs /1000

  plt.figure(figsize=(12,4))
  plt.plot(lags_ms, correlation)

  delay_ms = delay_samples * fs /1000
  plt.axvline(
        delay_ms,
        linestyle="--",
        label=f"Detected delay = {delay_ms:.2f} ms")

  plt.xlabel("Time (ms)") 
  plt.ylabel("Normalized correlation")
  plt.title("Correlation of EMG signals across different lag times")
  plt.grid(True)

  
      


