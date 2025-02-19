import pandas as pd

def pregunta_01():
    df = pd.read_csv("files/input/tbl0.tsv", sep="\t")
    return len(df)

# Prueba
print("Pregunta 01:", pregunta_01())
