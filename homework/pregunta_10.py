import pandas as pd

def pregunta_10():
    df = pd.read_csv("files/input/tbl0.tsv", sep="\t")

    # Agrupar por c1 y concatenar los valores de c2 en una lista separada por ":"
    resultado = df.groupby("c1")["c2"].apply(lambda x: ":".join(map(str, sorted(x)))).reset_index()

    # Ajustar el formato para que `c1` sea el índice
    resultado.set_index("c1", inplace=True)

    return resultado

# Prueba
print("Pregunta 10:\n", pregunta_10())
