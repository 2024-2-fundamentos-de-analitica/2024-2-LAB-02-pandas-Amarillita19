import pandas as pd

def pregunta_03():
    df = pd.read_csv("files/input/tbl0.tsv", sep="\t")
    return df["c1"].value_counts().sort_index()

# Prueba
print("Pregunta 03:\n", pregunta_03())
