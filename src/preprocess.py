import pandas as pd

def preprocess_data(file_path):
    # Load and preprocess dataset
    df = pd.read_csv(file_path, delimiter=r'\s+')
    new_column_names = ["Date(YYYY/MM/DD)", "Time(UTC)", "Latitude(deg)", "Longitude(deg)",
                        "Depth(km)", "Magnitude(ergs)", "Magnitude_type", "No_of_Stations", 
                        "Gap", "Close", "RMS", "SRC", "EventID"]
    df.columns = new_column_names
    ts = pd.to_datetime(df["Date(YYYY/MM/DD)"] + " " + df["Time(UTC)"])
    df = df.drop(["Date(YYYY/MM/DD)", "Time(UTC)"], axis=1)
    df.index = ts
    return df
