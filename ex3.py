import pandas as pd
import matplotlib.pyplot as plt

def minutes_002040(time: str) -> str:
    """
    Asigna 00, 20 o 40 minutos a los tiempos proporcionados en formato HH:MM:SS,
    redondeandolos a menor y guardando en formato HH:MM
    
    Ejemplo:
    minutes_002040("06:19:59") -> "06:00"
    """
    split_time = time.split(":") #separo el tiempo en 3 partes
    hours = split_time[0] #guardo la hora
    mins = split_time[1] #guardo los minutos

    if int(mins) < 20: #cambio los minutos a 00, 20 o 40 dependiendo del caso
        mins = "00"
    elif int(mins) < 40:
        mins = "20"
    else:
        mins = "40"

    return f"{hours}:{mins}" #devuelvo el resultado

def ex3(df: pd.DataFrame, generate_histogram: bool) -> pd.DataFrame:
    """
    Ejericio 3 de la PEC4
    """
    print("\nEx3\n")
    df['time_grouped'] = df['time'].apply(minutes_002040) #aplico la funcion creada al dataframe
    print(f"15 primeros valores del DataFrame\n{df.head(15)}\n")

    #creo el dataframe agrupado por la nueva columna time_grouped
    grouped_df = df.groupby('time_grouped').size().reset_index(name='num_ciclistas')
    print(f"Valores de DataFrame agrupado\n{grouped_df}")

    if generate_histogram:
        #genero el histograma
        plt.bar(grouped_df['time_grouped'], grouped_df['num_ciclistas'])
        plt.xlabel('Tiempo HH:MM')
        plt.ylabel('Numero de ciclistas')
        plt.title('Histograma Ex3')
        plt.xticks(rotation=45) #giro los tiempos 45 grados para mejorar la legibilidad
        plt.show()

    return df
