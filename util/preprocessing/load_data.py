import pandas as pd

def load_data(filename):
    df = pd.read_csv(
        filename,
        header=None,
        names=["time_ms", "ch1_v", "ch2_v"],
        skiprows=1,
        on_bad_lines="skip"
    )
    return df