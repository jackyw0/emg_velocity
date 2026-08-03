import numpy as np
import scipy.signal as sps
from scipy.signal import butter, sosfiltfilt, iirnotch






def bandpass(
        signal: np.ndarray,
        fs: float,
        lowcut: float,
        highcut: float,
        order: int = 4
) -> np.ndarray:
    
    if highcut >= fs/2:
        raise ValueError("highcut needs to be less than nyquist freq of {fs / 2} hz")
    
    sos = butter(
        order, [lowcut, highcut], btype = "bandpass", fs = fs, output = "sos"
    )
    return sosfiltfilt(sos, signal)


def notch( 
    signal: np.ndarray,
    fs: float, 
    notch_freq = 60.0,
    quality = 10.0

) -> np.ndarray:
    b, a = sps.iirnotch(notch_freq, quality, fs)

    return sps.filtfilt(b, a, signal)


