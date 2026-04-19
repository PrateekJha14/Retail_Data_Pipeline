import pandas as pd

def extract_data(path):
    df = pd.read_csv(path)
    print("Extracted:", df.shape)
    return df

if __name__ == "__main__":
    df = extract_data("../data/raw/SampleSuperstore.csv")