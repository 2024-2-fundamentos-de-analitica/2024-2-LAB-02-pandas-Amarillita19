import pandas as pd

def pregunta_13():
    # Cargar los archivos `tbl0.tsv` y `tbl2.tsv`
    tbl0 = pd.read_csv("files/input/tbl0.tsv", sep="\t")
    tbl2 = pd.read_csv("files/input/tbl2.tsv", sep="\t")

    # Unir `tbl0` y `tbl2` en base a la clave `c0`
    merged_df = pd.merge(tbl0, tbl2, on="c0")

    # Agrupar por `c1` y sumar `c5b`
    resultado = merged_df.groupby("c1")["c5b"].sum()

    return resultado

# Prueba
print("Pregunta 13:\n", pregunta_13())
