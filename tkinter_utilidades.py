import json
import csv
from tkinter import Tk, filedialog

def abrir_archivo_csv():
    Tk().withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if not file_path:
        return

    try:
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            preguntas = []
            for row in reader:
                pregunta = {
                    "pregunta": row['pregunta'],
                    "opciones": [row['opcion1'], row['opcion2'], row['opcion3'], row['opcion4']],
                    "respuesta_correcta": row['respuesta_correcta']
                }
                preguntas.append(pregunta)

        with open('preguntas.json', 'r+') as file:
            data = json.load(file)
            data.extend(preguntas)
            file.seek(0)
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Error al leer el archivo CSV: {e}")
