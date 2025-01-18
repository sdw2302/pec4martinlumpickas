import pandas as pd

def ex5(df: pd.DataFrame) -> pd.DataFrame:
    """
    Ejericio 5 de la PEC4
    """
    print("\nEx5\n")
    #ordeno el dataframe y regenero los indices para tener las posiciones
    df = df.sort_values(by='time').reset_index(drop=True)

    ciclistas_ucsc_raw = df[df['club_clean'] == 'UCSC']
    nombres_ciclistas_ucsc = ciclistas_ucsc_raw['biker']

    print(f"Los ciclistas de la UCSC son:\n{nombres_ciclistas_ucsc}\n")

    ciclistas_ucsc_sorted_by_time = ciclistas_ucsc_raw.sort_values(by='time')
    ciclista_ucsc_best_time = ciclistas_ucsc_sorted_by_time['biker'].iloc[0]
    print(f"El ciclista de la UCSC que ha hecho el mejor tiempo es: {ciclista_ucsc_best_time}\n")

    ciclista_ucsc_best_time_data = df[
        df['dorsal'] == ciclistas_ucsc_sorted_by_time['dorsal'].iloc[0]]
    posicion_best_ciclista_ucsc = ciclista_ucsc_best_time_data.index[0] + 1

    print(f"Posicion en que ha quedado el mejor ciclista de UCSC: {posicion_best_ciclista_ucsc}\n")

    porcentaje_best_ciclista_ucsc = (posicion_best_ciclista_ucsc / len(df)) * 100
    print(f"El porcentaje que representa es: {porcentaje_best_ciclista_ucsc:.2f}%")

    return df
