import pandas as pd
import matplotlib.pyplot as plt
import os

from util.preprocessing.load_data import load_data
from util.time_analysis.correlation import estimate_delay
from util.time_analysis.velocity import calculate_velocity



def plot_emg(filename):
    df = pd.read_csv(
        filename,
        header=None,
        names=["time_ms", "ch1_v", "ch2_v"],
        skiprows=1,           # skip the first corrupted row
        on_bad_lines="skip"
    )

    fig, axes = plt.subplots(2, 1, figsize=(12, 6), sharex=True)

    axes[0].plot(df["time_ms"], df["ch1_v"], color="tab:blue", linewidth=0.7)
    axes[0].set_ylabel("Channel 1 (V)")
    axes[0].set_title("EMG signal — Channel 1")
    axes[0].grid(True, alpha=0.3)

    axes[1].plot(df["time_ms"], df["ch2_v"], color="tab:orange", linewidth=0.7)
    axes[1].set_ylabel("Channel 2 (V)")
    axes[1].set_xlabel("Time (ms)")
    axes[1].set_title("EMG signal — Channel 2")
    axes[1].grid(True, alpha=0.3)

    plt.tight_layout()

    base_name = os.path.basename(filename).replace(".csv", ".png")  # strip any existing folder path
    output_name = os.path.join("plot_images_raw", base_name)
    plt.savefig(output_name, dpi=150)
    plt.show()




