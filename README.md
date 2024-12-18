# Proyecto Big Data - Bicicorunha

Este proyecto consiste en dos scripts que interactúan con la API de Bicicorunha y una base de datos MongoDB en la nube (MongoDB Atlas). Los scripts permiten almacenar datos en tiempo real y exportarlos en formatos CSV y Parquet.
Requisitos previos

### Para ejecutar este proyecto necesitas tener:

    Python (versión 3.8 o superior).
    Conda (para gestionar el entorno virtual).
    Acceso a MongoDB Atlas con las credenciales configuradas.

### Instalación y configuración
1. Clonar el repositorio

Clona este repositorio en tu máquina local con el siguiente comando:

git clone https://github.com/GuillermoCuervo00/proyectoEvaluacionBigData.git


### 2. Configurar el entorno Conda

Crea y activa el entorno virtual con Conda a partir del archivo environment.yml:

conda env create -f environment.yml
conda activate proyectoBigData

### 3. Ejecución de los scripts
1. Insertar datos en MongoDB (APIReaderPeriodico.py)

El script APIReaderPeriodico.py consulta la API de Bicicorunha y almacena la información en la base de datos MongoDB Atlas cada 5 minutos. El proceso continuará ejecutándose indefinidamente hasta que se cancele manualmente.

Ejecuta el script con:

python APIReaderPeriodico.py

Nota: Para detener el proceso, usa Ctrl+C en la terminal.


2. Exportar datos desde MongoDB (DataBaseReader.py)

El script DataBaseReader.py lee los datos almacenados en MongoDB Atlas y los exporta a dos formatos: CSV y Parquet. Los archivos exportados se guardarán en la raíz del proyecto.

Ejecuta el script con:

python DataBaseReader.py

Una vez finalizada la ejecución, encontrarás los archivos exportados en la raíz del proyecto:

    data_bicicorunha.csv: Archivo con los datos en formato CSV.
    data_bicicorunha.parquet: Archivo con los datos en formato Parquet.

Estructura del proyecto

    APIReaderPeriodico.py: Script que consulta la API periódicamente e inserta los datos en MongoDB Atlas.
    DataBaseReader.py: Script que recupera los datos de MongoDB y los exporta en formatos CSV y Parquet.
    environment.yml: Archivo para crear el entorno virtual con Conda.
