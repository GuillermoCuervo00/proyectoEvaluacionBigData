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

for doc in collection.find().limit(10):
    print(doc)
