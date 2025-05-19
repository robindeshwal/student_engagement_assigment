import os
import pandas as pd

RAW_DIR = 'data/raw'
OUTPUT_DIR = 'data/cleaned'

os.makedirs(OUTPUT_DIR, exist_ok=True)

def load_csv():
    for filename in os.listdir(RAW_DIR):
        if filename.endswith('.csv'):
            path = os.path.join(RAW_DIR, filename)
            try:
                df = pd.read_csv(path)
                df.to_csv(os.path.join(OUTPUT_DIR, filename), index=False)
                print(f"Loaded and saved: {filename}")
            except Exception as e:
                print(f"Error loading {filename}: {e}")

if __name__ == '__main__':
    load_csv()