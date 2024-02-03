import json
import csv
from datetime import datetime

# Cambia 'data.json' por la ruta a tu archivo JSON.
input_filename = 'data.json'
# Cambia 'data.csv' por la ruta y nombre del archivo CSV que deseas crear.
output_filename = 'data.csv'

def parse_iso_datetime(date_str):
    """Convierte una fecha en formato ISO 8601 a un formato legible sin 'T' y sin milisegundos."""
    date_obj = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
    return date_obj.strftime('%Y-%m-%d %H:%M:%S')

# Leer el archivo JSON
with open(input_filename, 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# Crear el archivo CSV
with open(output_filename, 'w', newline='', encoding='utf-8') as csv_file:
    # Suponiendo que todos los registros tienen la misma estructura y las mismas claves
    # Tomamos las claves del primer registro para los encabezados
    fieldnames = list(data[0]['fields'].keys()) if data else []

    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    # Escribir los encabezados
    writer.writeheader()

    # Escribir los datos
    for entry in data:
        # Parsear la fecha antes de escribir la fila
        entry['fields']['fecha'] = parse_iso_datetime(entry['fields']['fecha'])
        writer.writerow(entry['fields'])
