import pandas as pd

def cargar_datos(ruta):
    """Carga un dataset desde un archivo CSV."""
    return pd.read_csv(ruta)

def eliminar_nulos(df):
    """Elimina filas con valores nulos."""
    return df.dropna()

def normalizar_datos(df):
    """Normaliza columnas numéricas entre 0 y 1."""
    return (df - df.min()) / (df.max() - df.min())

def guardar_datos(df, ruta_salida):
    """Guarda el dataset preprocesado en un nuevo archivo CSV."""
    df.to_csv(ruta_salida, index=False)
