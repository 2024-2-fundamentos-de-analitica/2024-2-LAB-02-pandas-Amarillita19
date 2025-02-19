import pandas as pd

def pregunta_07():
    df = pd.read_csv("files/input/tbl0.tsv", sep="\t")
    return df.groupby("c1")["c2"].sum().sort_index()

# Prueba
print("Pregunta 07:\n", pregunta_07())
