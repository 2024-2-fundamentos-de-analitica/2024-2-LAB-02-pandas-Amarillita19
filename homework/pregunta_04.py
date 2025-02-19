import pandas as pd

def pregunta_04():
    df = pd.read_csv("files/input/tbl0.tsv", sep="\t")
    return df.groupby("c1")["c2"].mean().sort_index()

# Prueba
print("Pregunta 04:\n", pregunta_04())
