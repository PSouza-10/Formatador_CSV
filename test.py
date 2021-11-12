import pandas as pd
import config

print(pd.read_csv(config.OUTPUT_PATH).head())