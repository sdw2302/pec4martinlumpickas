import pandas as pd
from faker import Faker as fk

def name_surname(df: pd.DataFrame) -> pd.DataFrame:
    """
    Genera nombres falsos para anonimizar los ciclistas en un DataFrame
    """
    fake = fk() #creo la instancia del faker
    for i in range(len(df)):
        df.loc[i, 'biker'] = fake.name() #genero los nombres falsos y cambiamos por los del df
    return df

def ex2(df: pd.DataFrame) -> pd.DataFrame:
    """
    Ejericio 2 de la PEC4
    """
    print("\nEx2\n")
    df = name_surname(df)

    print(f"DataFrame con los nombres cambiados:\n{df.head(5)}\n")

    df = df[df['time'] != '00:00:00'] #elimino los ciclistas que no participaron

    print(f"DataFrame sin los ciclistas que no participaron en la prueba:\n{df.head(5)}\n")

    print(f"Datos del ciclista con dorsal 1000:\n{df[df['dorsal'] == 1000]}")
    return df
