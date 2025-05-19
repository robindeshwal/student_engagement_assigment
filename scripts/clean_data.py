import os
import pandas as pd

INPUT_DIR = 'data/cleaned'
OUTPUT_DIR = 'data/cleaned'

for file in os.listdir(INPUT_DIR):
    if file.endswith('.csv'):
        path = os.path.join(INPUT_DIR, file)
        df = pd.read_csv(path)
        df.drop_duplicates(inplace=True)
        # df.fillna(method='ffill', inplace=True)
        df.ffill(inplace=True)
        
        if 'timestamp' in df.columns:
            df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')

        df.to_csv(os.path.join(OUTPUT_DIR, file), index=False)
        print(f"Cleaned and saved: {file}")