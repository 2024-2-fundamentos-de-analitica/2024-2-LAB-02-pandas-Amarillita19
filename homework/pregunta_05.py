import pandas as pd

def pregunta_05():
    df = pd.read_csv("files/input/tbl0.tsv", sep="\t")
    return df.groupby("c1")["c2"].max().sort_index()

# Prueba
print("Pregunta 05:\n", pregunta_05())
