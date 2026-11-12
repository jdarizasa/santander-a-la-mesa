"""
Modulo de extracción de datos desde una API pública de la pagina de datos.gov.co
"""

import requests
import pandas as pd

BASE_URL = "https://www.datos.gov.co/resource/{dataset_id}.json"
DATASET_ID = "uejq-wxrr"

WHERE = "departamento = 'Santander' AND a_o = 2025"

def fetch_santander_2025(dataset_id, where_clause):
    url = BASE_URL.format(dataset_id=dataset_id)
    
    # 1. Contar filas primero para saber si hay que paginar
    count_resp = requests.get(url, params={"$select": "count(*)", "$where": where_clause})
    count_resp.raise_for_status()
    total = int(count_resp.json()[0]["count"])
    print(f"Filas que cumplen el filtro: {total}")

    if total == 0:
        return pd.DataFrame()

    # 2. Paginar de 1000 en 1000
    frames = []
    limit = 1000
    offset = 0
    while offset < total:
        params = {
            "$where": where_clause,
            "$limit": limit,
            "$offset": offset,
            "$order": ":id",  # orden estable para que la paginación no repita ni omita filas
        }
        resp = requests.get(url, params=params)
        resp.raise_for_status()
        chunk = pd.DataFrame(resp.json())
        if chunk.empty:
            break
        frames.append(chunk)
        offset += limit
        print(f"Descargadas {offset if offset < total else total} de {total}")

    return pd.concat(frames, ignore_index=True) if frames else pd.DataFrame()

df = fetch_santander_2025(DATASET_ID, WHERE)
print(df.shape)
print(df.head())

df.to_parquet("ecv.parquet", engine='pyarrow')