from pymongo import MongoClient
import pandas as pd

# Credenciales y URI
username = "gcuervobarc"
password = "hbn6Bd50EUeUhVu7"
cluster_name = "cluster0.ke4mf.mongodb.net"
database_name = "bicis"
collection_name = "corunha"

# Construir el URI
uri = f"mongodb+srv://{username}:{password}@{cluster_name}/?retryWrites=true&w=majority"

# Conexión a MongoDB
client = MongoClient(uri)
db = client[database_name]
collection = db[collection_name]

def export_data():
    """
    Exporta los datos de MongoDB a un DataFrame de pandas y los guarda en CSV y Parquet.
    """
    # Campos requeridos
    fields = {
        "_id": 0,  # Excluye el campo _id
        "id": 1,
        "name": 1,
        "timestamp": 1,
        "free_bikes": 1,
        "empty_slots": 1,
        "uid": 1,
        "last_updated": 1,
        "slots": 1,
        "normal_bikes": 1,
        "ebikes": 1
    }

    # Recuperar datos desde MongoDB
    documents = list(collection.find({}, fields))
    if not documents:
        print("No hay datos en la colección.")
        return

    # Crear DataFrame
    df = pd.DataFrame(documents)

    # Guardar en CSV
    csv_filename = "data_bicicorunha.csv"
    df.to_csv(csv_filename, index=False)
    print(f"Datos exportados a CSV: {csv_filename}")

    # Guardar en Parquet
    parquet_filename = "data_bicicorunha.parquet"
    df.to_parquet(parquet_filename, index=False)
    print(f"Datos exportados a Parquet: {parquet_filename}")

if __name__ == "__main__":
    export_data()
