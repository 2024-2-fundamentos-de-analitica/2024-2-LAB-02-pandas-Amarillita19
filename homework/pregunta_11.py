import pandas as pd

def pregunta_11():
    df = pd.read_csv("files/input/tbl1.tsv", sep="\t")

    # Agrupar por `c0` y concatenar los valores de `c4` ordenados y separados por ","
    resultado = df.groupby("c0")["c4"].apply(lambda x: ",".join(sorted(x))).reset_index()

    return resultado

# Prueba
print("Pregunta 11:\n", pregunta_11())
