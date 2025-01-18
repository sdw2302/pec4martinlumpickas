import pandas as pd

def ex1(df: pd.DataFrame) -> None:
    """
    Ejericio 1 de la PEC4
    """
    print("\nEx1\n")
    print(f"5 primeros valores del DataFrame:\n{df.head(5)}\n") #muestro los primeros 5 valores

    print(f"Numero de ciclistas que participaro en la prueba: {len(df)}\n")

    cols = ""
    for col in df.columns: #guardo todos los nombres de las columnas del df
        cols += col + ' '

    print(f"Columnas del dataframe: {cols}")
