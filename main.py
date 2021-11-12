import pandas as pd
import config

alphabet = [chr(i) for i in range(97,123)]

def extract_cols_from_string(string:str,col_prefix:str):
    cols = {}

    for idx,i in enumerate(string.split('|')):
        id = str(idx+1)

        for char,p in zip(alphabet,i.split(':')):
            part = p.strip()
            cols[f'{col_prefix}_{id}{char}'] = part
        
    return cols

df = pd.read_csv(config.INPUT_PATH)
df = df.set_index(config.ID_COL)

other_cols = df.copy()
del other_cols[config.COL_NAME]

new_df = pd.DataFrame({config.ID_COL: []})
new_df = new_df.set_index(config.ID_COL)

for ID,v in zip(df.index,df[config.COL_NAME]):
    this_idx_cols = other_cols.loc[[ID]]
    new_cols = extract_cols_from_string(v,config.COL_NAME)

    for c in new_cols:
        if c != config.ID_COL:
            this_idx_cols[c] = new_cols[c]

    
    new_df = new_df.append(this_idx_cols)

new_df.to_csv(config.OUTPUT_PATH)
