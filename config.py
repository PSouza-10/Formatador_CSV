COL_NAME = 'v36a'
ID_COL = 'ID'

INPUT_PATH = 'samples/Exemplo2.csv'
FILENAME = INPUT_PATH.split('/')[-1]
OUTPUT_PATH = f'outputs/{FILENAME}'

DEDUPE_THROUGH_COLUMNS = ['nome','cpf']
IDENTIFIER_SEPARATOR = '_'

DELIMITER = ','