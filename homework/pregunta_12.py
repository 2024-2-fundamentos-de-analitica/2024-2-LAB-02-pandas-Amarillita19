import pandas as pd

def pregunta_12():
    df = pd.read_csv("files/input/tbl2.tsv", sep="\t")

    # Crear la nueva columna `c5` combinando `c5a` y `c5b` separadas por `":"`
    df["c5"] = df["c5a"] + ":" + df["c5b"].astype(str)

    # Agrupar por `c0` y concatenar los valores de `c5` ordenados, separados por `","`
    resultado = df.groupby("c0")["c5"].apply(lambda x: ",".join(sorted(x))).reset_index()

    return resultado

# Prueba
print("Pregunta 12:\n", pregunta_12())
