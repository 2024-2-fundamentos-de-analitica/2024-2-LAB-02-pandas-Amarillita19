import pandas as pd

def pregunta_06():
    df = pd.read_csv("files/input/tbl1.tsv", sep="\t")
    return sorted(df["c4"].str.upper().unique())

# Prueba
print("Pregunta 06:\n", pregunta_06())
