import requests
import pandas as pd
import logging
import difflib

# Configuración de logging
logging.basicConfig(filename='consulta_libros.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Función para realizar la consulta y procesar los resultados
def consulta_libro(isbn, subtitulo):
    """
    Consulta la información de un libro en la API de Porrúa utilizando el ISBN y un subtítulo.
    Args:
        isbn (str): El ISBN del libro a consultar.
        subtitulo (str): El subtítulo del libro para encontrar la coincidencia más cercana.
    Returns:
        dict or None: Un diccionario con la información del libro si se encuentra una coincidencia cercana,
                      de lo contrario, None. El diccionario contiene las siguientes claves:
                      - "title": El título del libro.
                      - "url": La URL del libro en el sitio de Porrúa.
                      - "price": El precio del libro.
                      - "detail": Detalles adicionales del libro.
                      - "editorial": La editorial del libro.

    """
    # Definir la URL y parámetros
    url = f"https://porrua.mx/suggestedsearch/Index/suggestedsearch/?q={isbn}&_=1729900306096"
    response = requests.get(url)
    
    # Verificar que la respuesta sea exitosa
    if response.status_code != 200:
        logging.error(f"No se pudo acceder a la API para ISBN: {isbn}")
        return None
    
    # Cargar datos de la respuesta JSON
    datos = response.json()
    productos = datos.get("producto", [])
    
    # Si no hay productos en la respuesta
    if not productos:
        logging.warning(f"No se encontraron productos para ISBN: {isbn}")
        return None

    # Encontrar el producto más cercano al subtítulo
    titulos = [prod.get("title", "") for prod in productos]
    mejor_coincidencia = difflib.get_close_matches(subtitulo, titulos, n=1)
    
    # Verificar si se encontró una coincidencia cercana
    if mejor_coincidencia:
        for producto in productos:
            if producto["title"] == mejor_coincidencia[0]:
                return {
                    "title": producto.get("title"),
                    "url": producto.get("url"),
                    "price": producto.get("price"),
                    "detail": producto.get("detail"),
                    "editorial": producto.get("editorial")
                }
    else:
        logging.warning(f"No se encontró coincidencia cercana para ISBN: {isbn}")

    return None

# Función para procesar el archivo Excel
def procesar_excel(archivo_entrada, archivo_salida):
    df = pd.read_excel(archivo_entrada)
    resultados = []

    for index, row in df.iterrows():
        isbn = row.get("ISBN")
        subtitulo = row.get("Subtitulo")
        if not isbn or not subtitulo:
            continue
        
        logging.info(f"Consultando ISBN: {isbn} - Subtitulo: {subtitulo}")
        resultado = consulta_libro(isbn, subtitulo)
        
        if resultado:
            resultados.append({
                "ISBN": isbn,
                "Subtitulo": subtitulo,
                "Title": resultado["title"],
                "URL": resultado["url"],
                "Price": resultado["price"],
                "Detail": resultado["detail"],
                "Editorial": resultado["editorial"]
            })
            logging.info(f"Agregado>>> {resultado}")

    # Guardar los resultados en un nuevo archivo Excel
    df_resultados = pd.DataFrame(resultados)
    df_resultados.to_excel(archivo_salida, index=False)
    logging.info(f"Resultados guardados en el archivo: {archivo_salida}")

# Ejecución principal
if __name__ == "__main__":
    procesar_excel('archivo.xlsx', 'porrua.xlsx')
    logging.info("Proceso completado.")
