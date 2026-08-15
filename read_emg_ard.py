import serial
import csv
import time
import os
from plot_emg_raw import plot_emg


def record_emg(port="/dev/tty.usbmodem101", baud=961200, duration_sec=15, folder="data"):
    ser = serial.Serial(port, baud, timeout=1)
    time.sleep(2)
    ser.reset_input_buffer()

    os.makedirs(folder, exist_ok=True)
    filename = os.path.join(folder, f"emg_data_{int(time.time())}.csv")

    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["time_ms", "ch1_v", "ch2_v"]) 
        start = time.time()

        while time.time() - start < duration_sec:
            line = ser.readline().decode(errors="ignore").strip()
            if line and line.count(",") == 2: 
                writer.writerow(line.split(","))

    ser.close()
    print(f"saved to {filename}")
    return filename

csv_filename = record_emg()

plot_emg(csv_filename)
