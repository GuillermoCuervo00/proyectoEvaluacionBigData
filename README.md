# Proyecto Big Data - Bicicorunha

Este proyecto consiste en dos scripts que interactúan con la API de Bicicorunha y una base de datos MongoDB. Los scripts permiten consultar datos en tiempo real y exportarlos en formatos útiles como CSV y Parquet.

## Estructura del proyecto

- **`api_to_mongo.py`**: Consulta la API de Bicicorunha a intervalos regulares y almacena los datos en MongoDB.
- **`export_mongo_data.py`**: Recupera los datos desde MongoDB y los exporta en formatos CSV y Parquet.
- **`environment.yml`**: Archivo de configuración del entorno Conda con todas las dependencias necesarias.

---

## Requisitos previos

1. **Python 3.8 o superior**.
2. **Conda**: Para la gestión de entornos.
3. **MongoDB Atlas**: Servidor de base de datos MongoDB configurado.
4. **Docker (opcional)**: Para ejecutar el proyecto en contenedores.

---

## Configuración inicial

### 1. Clona este repositorio
```bash
git clone https://github.com/tu_usuario/proyectoBigData.git
cd proyectoBigData

2. Crea y activa el entorno Conda

conda env create -f environment.yml
conda activate proyectoBigData

3. Configura MongoDB Atlas

    Asegúrate de tener una base de datos y una colección en MongoDB Atlas.
    Actualiza las credenciales y configuraciones en los scripts (api_to_mongo.py y export_mongo_data.py):
        username
        password
        cluster_name
        database_name
        collection_name

4. Instala motores adicionales (opcional)

Para exportar en formato Parquet:

conda install -c conda-forge pyarrow

Uso del proyecto
1. Ejecutar el Script 1: API a MongoDB

Este script consulta la API a intervalos regulares y almacena los datos en MongoDB.

python api_to_mongo.py

2. Ejecutar el Script 2: Exportación de datos

Este script recupera los datos de MongoDB y los guarda en CSV y Parquet.

python export_mongo_data.py

Los archivos exportados estarán en el directorio actual:

    data_bicicorunha.csv
    data_bicicorunha.parquet

Despliegue con Docker (opcional)
1. Construir la imagen Docker

docker build -t proyecto-bigdata .

2. Ejecutar el contenedor

docker run -d --name proyecto-bigdata proyecto-bigdata

3. Usar Docker Compose (MongoDB + Aplicación)

Crea un archivo docker-compose.yml para ejecutar MongoDB y los scripts juntos.
Notas importantes

    Control de errores: Ambos scripts manejan fallos de conexión a la API y la base de datos.
    Seguridad: Asegúrate de no compartir tus credenciales en repositorios públicos.
    Compatibilidad: Prueba el proyecto en otros sistemas antes de desplegarlo.

Licencia

Este proyecto está licenciado bajo la MIT License. Consulta el archivo LICENSE para más información.
