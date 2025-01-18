import pandas as pd

def clean_club(club: str) -> str:
    """
    Limpia los nombres de los clubs proporcionados de siguiente manera:
    
    - Convierte el nombre del club a mayúsculas
    - Reemplaza por nada los siguientes valores:
    'PEÑA CICLISTA ', 'PENYA CICLISTA ', 'AGRUPACIÓN CICLISTA ', 'AGRUPACION CICLISTA ',
    'AGRUPACIÓ CICLISTA ', 'AGRUPACIO CICLISTA ', 'CLUB CICLISTA ', 'CLUB '
    - Reemplaza por nada los siguientes valores cuando están en el inicio (expresión regular):
    'C.C. ', 'C.C ', 'CC ', 'C.D. ', 'C.D ', 'CD ', 'A.C. ', 'A.C ', 'AC ', 'A.D. ', 'A.D ', 'AD ',
    'A.E. ', 'A.E ', 'AE ', 'E.C. ', 'E.C ', 'EC ', 'S.C. ', 'S.C ', 'SC ', 'S.D. ', 'S.D ', 'SD '.
    - Reemplaza por nada los siguientes valores cuando están en el final:
    ' T.T.',' T.T',' TT',' T.E.',' T.E',' TE',' C.C.',' C.C',' CC',' C.D.',' C.D',' CD',' A.D.',
    ' A.D',' AD',' A.C.',' A.C',' AC'
    - Elimina posibles espacios en blanco al principio o al final de la cadena.
    """
    club = club.upper() #convierto el nombre del club a mayusculas

    #reemplazo por nada los siguientes valores
    a_eliminar = {'PEÑA CICLISTA ', 'PENYA CICLISTA ', 'AGRUPACIÓN CICLISTA ',
                 'AGRUPACION CICLISTA ', 'AGRUPACIÓ CICLISTA ', 'AGRUPACIO CICLISTA ',
                 'CLUB CICLISTA ', 'CLUB '}
    for x in a_eliminar:
        if x in club:
            club = club.replace(x, '')

    #reemplazo por nada los siguientes valores cuando estan en el inicio
    a_eliminar_inicio = {'C.C. ', 'C.C ', 'CC ', 'C.D. ', 'C.D ', 'CD ', 'A.C. ', 'A.C ',
                       'AC ', 'A.D. ', 'A.D ', 'AD ', 'A.E. ', 'A.E ', 'AE ', 'E.C. ',
                       'E.C ', 'EC ', 'S.C. ', 'S.C ', 'SC ', 'S.D. ', 'S.D ', 'SD '}
    for prefix in a_eliminar_inicio:
        if club.startswith(prefix):
            club = club.replace(prefix, '')

    #reemplazo por nada los siguientes valores cuando estan en el final
    a_eliminar_final = {' T.T.',' T.T',' TT',' T.E.',' T.E',' TE',' C.C.',' C.C',' CC',' C.D.',
                      ' C.D',' CD',' A.D.',' A.D',' AD',' A.C.',' A.C',' AC'}
    for suffix in a_eliminar_final:
        if club.endswith(suffix):
            club = club.replace(suffix, '')

    #elimino posibles espacios en blanco al principio o al final de la cadena
    club = club.strip()

    return club

def ex4(df: pd.DataFrame) -> pd.DataFrame:
    """
    Ejericio 4 de la PEC4
    """
    print("\nEx4\n")
    df['club_clean'] = df['club'].apply(clean_club) #aplico la funcion creada al dataframe

    print(f"15 primeros valores del DataFrame\n{df.head(15)}\n")

    #creo el dataframe agrupado por la nueva columna club_clean
    grouped_club_df = df.groupby('club_clean').size().reset_index(name='num_ciclistas')
    #creo el dataframe agrupado por la nueva columna club_clean
    grouped_club_df = grouped_club_df.sort_values('num_ciclistas', ascending=False)

    print(f"Valores de DataFrame agrupado y ordenado\n{grouped_club_df}")

    return df
