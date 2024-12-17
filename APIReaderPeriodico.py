import requests
import pandas as pd
import schedule
import time
import os
from pymongo import MongoClient


# URL da API
api_url = "http://api.citybik.es/v2/networks/bicicorunha"
# Credenciales y URI
username = "gcuervobarc"
password = "hbn6Bd50EUeUhVu7"
cluster_name = "cluster0.ke4mf.mongodb.net"
database_name = "bicis"  # Cambia esto al nombre de tu base de datos si es necesario
collection_name = "corunha"

# Construir el URI
uri = f"mongodb+srv://{username}:{password}@{cluster_name}/?retryWrites=true&w=majority"

# Conexión
client = MongoClient(uri)
db = client[database_name]
collection = db[collection_name]

tiempo_consulta_segundos=5
tiempo_consulta_minutos=60*tiempo_consulta_segundos

def fetch_data(api_url):
    """
    Obtén datos dunha API e devólveos en formato JSON.
    """
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Lanza unha excepción se a resposta non é exitosa
        return response.json()  # Devólve os datos en formato JSON
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acceder á API: {e}")
        return None

def process_data(data):
    """
    Procesa os datos da API e retorna un DataFrame cos campos relevantes.
    """
    # Extraer información das estacións
    stations = data.get("network", {}).get("stations", [])
    records = []
    for station in stations:
        records.append({
            "id": station.get("id"),
            "name": station.get("name"),
            "timestamp": station.get("timestamp"),
	    "free_bikes": station.get("free_bikes"),
	    "empty_slots": station.get("empty_slots"),
	    "uid": station.get("uid"),
	    "last_updated": station.get("last_updated"),
	    "slots": station.get("slots"),
	    "normal_bikes": station.get("normal_bikes"),
	    "ebikes": station.get("ebikes")
        })
    return pd.DataFrame(records)

def update_and_display():
    """
    Obtén datos da API, actualízaos e refresca a pantalla coas novas informacións.
    """
    # Obter datos da API
    data = fetch_data(api_url)
    if data:
        # Procesar os datos nun DataFrame
        df = process_data(data)
        
        # Limpar a consola e mostrar o DataFrame
        os.system('clear' if os.name == 'posix' else 'cls')  # Limpa a pantalla
        print("Datos de Bicicoruña (Actualizado cada ",tiempo_consulta_minutos," segundos):")
        print(df.to_string(index=False))  # Mostra o DataFrame sen índices
        
        data_to_insert = df.to_dict(orient="records")
        
        try:
            result = collection.insert_many(data_to_insert)
            print("Docuemntos insertados")
        except Exception as e:
            print("Error ERROR EEERROOOOOOOOR", e)
        
    else:
        print("Non foi posible obter os datos da API.")

def main():
    # Programar a actualización cada 5 segundos
    schedule.every(tiempo_consulta_minutos).seconds.do(update_and_display)

    # Executar o scheduler
    print("Iniciando actualización en tempo real (cada ",tiempo_consulta_minutos," segundos). Preme Ctrl+C para saír.")
    update_and_display()  # Executar inmediatamente antes de entrar no bucle
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
