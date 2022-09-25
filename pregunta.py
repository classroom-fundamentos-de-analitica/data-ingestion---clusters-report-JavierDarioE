"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import re
import pandas as pd


def ingest_data():
    with open("./clusters_report.txt", "r") as text_file:
        header = re.split(r"\s{2,}", text_file.readline().strip())
        line_2 = re.split(r"\s{2,}", text_file.readline().strip())
        header[1] += " " + line_2[0]
        header[2] += " " + line_2[1]
        header = [i.replace(" ", "_").lower() for i in header]
        body = re.split(r"\n\s{3}(?=\d)", text_file.read())
    body.pop(0)
    body = [re.split(r"\s{2,}", row, 3) for row in body]
    for row in body:
        row[2] = row[2].replace(" %", "").replace(",", ".")
        row[3] = re.sub(r"\s+", " ", row[3].replace(".", "").strip())
    data_types_dict = {'cluster': int,
                       'cantidad_de_palabras_clave': int,
                       'porcentaje_de_palabras_clave': float,
                       'principales_palabras_clave': str}
    df = pd.DataFrame(body, columns=header)
    df = df.astype(data_types_dict)
    return df
