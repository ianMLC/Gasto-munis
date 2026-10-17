import pandas as pd

from mcp_sinim import SINIMClient
from src.config import YEARS,COMMUNES,DATA_RAW,DATA_PROCESSED,GROUPS

client = SINIMClient(corrmon=True)

def descargar_grupo(nombre: str, forzar: bool = False) -> pd.DataFrame:
    """Descaga un grupo de variables del SINIM y guarda en raw
    
    Si el archivo ya existe y forzar es False, lo lee del disco.
    Agrega una columna 'variable' con el alias definido en GRUPOS.
    """
    ruta = DATA_RAW/f"{nombre}.parquet"
    
    if ruta.exists() and not forzar:
        print(f"{nombre} - leído desde disco 📂")
        return pd.read_parquet(ruta)
    
    variables = GROUPS[nombre]
    
    df = client.get(
        list(variables.keys()),
        years = YEARS,
        municipios=list(COMMUNES)
    )
    
    df["variable"] = df["code"].map(variables)   # <- esta línea

    DATA_RAW.mkdir(parents=True, exist_ok=True)
    df.to_parquet(ruta, index=False)
    print(f"{nombre} - parquet guardado ✅")
    return df
    
    

def descargar_todo(forzar: bool = False) -> pd.DataFrame:
    """Descarga todos los grupos y devuelve un solo DataFrame largo."""
    dfs = []
    
    for nombre in GROUPS:
        df = descargar_grupo(nombre, forzar=forzar)
        df["grupo"] = nombre
        dfs.append(df)
            
    return pd.concat(dfs, ignore_index=True)



def a_ancho(df: pd.DataFrame) -> pd.DataFrame:
    """Convierte el panel largo en ancho: una fila por comuna-año."""
    ancho = df.pivot_table(
        index=["cod_municipio", "nombre_municipio", "anio"],
        columns="variable",
        values="value",
        aggfunc="first",
    )
    ancho.columns.name = None
    return ancho.reset_index() 