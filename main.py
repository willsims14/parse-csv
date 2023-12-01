import pandas as pd
import os

from utils import parse_worker_config

config = parse_worker_config()
COLS_TO_SEARCH = config['cols_to_search']
STRING_TO_SEARCH_FOR = config['string_to_search_for']

csv_files = [f for f in os.listdir("./data") if f.endswith(".csv")]
for filename in csv_files:
    print(filename)
    filepath = os.path.join('data/', filename)
    df = pd.read_csv(filepath)
    for col in COLS_TO_SEARCH:
        temp_df = df.loc[df[col] == STRING_TO_SEARCH_FOR]
        val = temp_df.iloc[0, 0]
        print(f"  * Found string `{STRING_TO_SEARCH_FOR}` in column `{col}` at ID: {val}")
        # print("  * Row ID: " + str(val))
