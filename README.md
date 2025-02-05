# Porrúa API Book Information Script

Este proyecto tiene como objetivo consultar información de libros en la API de Porrúa utilizando el ISBN y un subtítulo para encontrar coincidencias cercanas. El script procesa un archivo Excel de entrada con los datos de los libros y guarda los resultados en un nuevo archivo Excel.

## Estructura del Proyecto

- `porrua_api.py`: Script principal que realiza las consultas a la API de Porrúa y procesa los resultados.

## Requisitos

- Python 3.x
- Pandas
- Requests
- Difflib
- Un archivo Excel con los datos de los libros

## Instalación

1. Clona el repositorio:
    ```sh
    git clone https://github.com/ThunrazAuza/ejemplo-api-porrua
    cd tu_repositorio
    ```

2. Instala las dependencias:
    ```sh
    pip install -r requirements.txt
    ```

## Uso

1. Asegúrate de tener un archivo Excel con los datos de los libros. El archivo debe contener al menos dos columnas: `ISBN` y `Subtitulo`.

2. Ejecuta el script `porrua_api.py`:
    ```sh
    python porrua_api.py
    ```

3. El script procesará el archivo `archivo.xlsx` y guardará los resultados en un nuevo archivo llamado `porrua.xlsx`.

## Configuración de Logging

El script utiliza el módulo `logging` para registrar información sobre el proceso de consulta. Los registros se guardan en un archivo llamado `consulta_libros.log`.

## Funciones Principales

### `consulta_libro(isbn, subtitulo)`

Consulta la información de un libro en la API de Porrúa utilizando el ISBN y un subtítulo.

- **Args:**
  - `isbn` (str): El ISBN del libro a consultar.
  - `subtitulo` (str): El subtítulo del libro para encontrar la coincidencia más cercana.

- **Returns:**
  - `dict` or `None`: Un diccionario con la información del libro si se encuentra una coincidencia cercana, de lo contrario, `None`.

### `procesar_excel(archivo_entrada, archivo_salida)`

Procesa un archivo Excel de entrada y guarda los resultados en un nuevo archivo Excel.

- **Args:**
  - `archivo_entrada` (str): La ruta del archivo Excel de entrada.
  - `archivo_salida` (str): La ruta del archivo Excel de salida.

## Ejecución Principal

El script se ejecuta automáticamente cuando se llama directamente. Procesa el archivo `archivo.xlsx` y guarda los resultados en `porrua.xlsx`.

```python
if __name__ == "__main__":
    procesar_excel('archivo.xlsx', 'porrua.xlsx')
    logging.info("Proceso completado.")
```

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o envía un pull request para discutir cualquier cambio que te gustaría realizar.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.