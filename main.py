import os
import pandas as pd
import config

alphabet = [chr(i) for i in range(97,123)]

folders = ['outputs','samples','duplicates']

for f in folders:
    if not os.access(f,mode=1):
        os.mkdir(f)


def get_identifier(row):
    identifier = ''
    last_col = row.columns[-1]
    for col in row.columns:
        append = config.IDENTIFIER_SEPARATOR  if col != last_col else '' 

        identifier += f'{row[col].values[0]}{append}'
    return identifier

def extract_cols_from_string(string:str,col_prefix:str):
    cols = {}

    for idx,i in enumerate(string.split('|')):
        id = str(idx+1)

        for char,p in zip(alphabet,i.split(':')):
            part = p.strip()
            cols[f'{col_prefix}_{id}{char}'] = part
        
    return cols

df = pd.read_csv(config.INPUT_PATH,delimiter=config.DELIMITER)

if config.ID_COL:
    df = df.set_index(config.ID_COL)


new_df_args = {config.ID_COL: []} if config.ID_COL else {}
filtered_df = pd.DataFrame(new_df_args)

duplicates = pd.DataFrame(new_df_args)
if config.ID_COL:
    filtered_df = filtered_df.set_index(config.ID_COL)
    duplicates = duplicates.set_index(config.ID_COL)
removed = 0



inserted_identifiers = []



for ID in df.index:
    row_data = df.loc[[ID]]
    row_identifier = get_identifier(row_data)
    
    
    if not row_identifier in inserted_identifiers:
        inserted_identifiers.append(row_identifier)
        filtered_df = filtered_df.append(row_data)
    else:
        duplicates = duplicates.append(row_data)
        removed+=1


other_cols = filtered_df.copy()

del other_cols[config.COL_NAME]

duplicates.to_csv(f'duplicates/{config.FILENAME}')

new_df = pd.DataFrame(new_df_args)

if config.ID_COL:
    new_df = new_df.set_index(config.ID_COL)

for ID,v in zip(filtered_df.index, filtered_df[config.COL_NAME]):
    this_idx_cols = other_cols.loc[[ID]]
   
    
    new_cols = extract_cols_from_string(v,config.COL_NAME)
    for c in new_cols:
        if c != config.ID_COL:
            this_idx_cols[c] = new_cols[c]

    
    new_df = new_df.append(this_idx_cols)

new_df.to_csv(config.OUTPUT_PATH)
