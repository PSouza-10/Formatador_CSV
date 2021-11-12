# Formatador

Para rodar o script, primeiro edite o arquivo `config.py`, definindo os seguintes parâmetros:

```python
COL_NAME = 'v36a' # O nome da coluna para separar em outras, será utilizada como prefixo ( <nome da coluna>_<número>_<letra>) para gerar as novas colunas

ID_COL = 'ID' # A coluna usada como identificador (index) do dataframe

INPUT_PATH = 'samples/Exemplo2.csv' # Caminho do arquivo contendo os dados

FILENAME = INPUT_PATH.split('/')[-1] # Esta variável é gerada automáticamente, é o nome do arquivo

OUTPUT_PATH = f'outputs/{FILENAME}' # Caminho para salvar o csv transformado. Deixe dessa forma para criar um arquivo com o mesmo nome do INPUT dentro da pasta outputs
```

Após feito isso, no seu terminal dentro da pasta do projeto rode `python main.py`

O CSV transformado será salvo no caminho especificado por `OUTPUT_PATH`

Para confirmar a formatação, rode `python test.py`. Os dados do CSV transformado serão mostrados no terminal.
