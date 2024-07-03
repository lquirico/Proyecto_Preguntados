import pygame
import sys
import json
import csv
from tkinter import Tk, filedialog
from config import *

# Funciones relacionadas con pygame y UI

def dibujar_flecha_retroceso(pantalla):
    pygame.draw.polygon(pantalla, BLANCO, [(10, 20), (30, 10), (30, 30)])  # Dibujar una flecha simple

def clic_en_flecha_retroceso(pos):
    x, y = pos
    return 10 <= x <= 30 and 10 <= y <= 30

def mostrar_ajustes(pantalla):
    pantalla.fill(NEGRO)

    # Título de Ajustes
    titulo_surface = fuente_predeterminada.render("Ajustes", True, DORADO)
    pantalla.blit(titulo_surface, (ancho // 2 - titulo_surface.get_width() // 2, 50))

    # Opciones de Ajustes
    opciones_ajustes = ["Volumen", "Modificar", "Agregar Preguntas"]
    y_offset = (alto - len(opciones_ajustes) * 50) // 2  # Ajustar el valor para centrar verticalmente las opciones

    for i, opcion in enumerate(opciones_ajustes):
        texto_surface = fuente_ajustes.render(opcion, True, BLANCO)
        pantalla.blit(texto_surface, (ancho // 2 - texto_surface.get_width() // 2, y_offset))
        y_offset += 60  # Espacio entre opciones (puedes ajustar este valor)

    # Dibujar flecha de retroceso
    dibujar_flecha_retroceso(pantalla)

    pygame.display.flip()

    esperando_seleccion = True
    while esperando_seleccion:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = evento.pos
                if clic_en_flecha_retroceso((x, y)):
                    esperando_seleccion = False
                    return  # Regresar a la pantalla anterior
                elif (alto // 2 - 60) <= y <= (alto // 2 - 20):
                    print("Volumen seleccionado")
                    esperando_seleccion = False
                elif (alto // 2 - 20) < y <= (alto // 2 + 20):
                    print("Modificar seleccionado")
                    esperando_seleccion = False
                elif (alto // 2 + 20) < y <= (alto // 2 + 60):
                    print("Agregar Preguntas seleccionado")
                    mostrar_menu_agregar_preguntas(pantalla, mostrar_ajustes)  # Mostrar menú de agregar preguntas
                    esperando_seleccion = False
                    
def mostrar_menu_agregar_preguntas(pantalla, anterior):
    pantalla.fill(NEGRO)

    # Título de Agregar Preguntas
    titulo_surface = fuente_predeterminada.render("Agregar Preguntas", True, DORADO)
    pantalla.blit(titulo_surface, (ancho // 2 - titulo_surface.get_width() // 2, 50))

    # Opciones de Agregar Preguntas
    opciones_agregar = ["Pregunta individual", "Preguntas desde CSV"]
    y_offset = (alto - len(opciones_agregar) * 50) // 2  # Ajustar el valor para centrar verticalmente las opciones

    for i, opcion in enumerate(opciones_agregar):
        texto_surface = fuente_ajustes.render(opcion, True, BLANCO)
        pantalla.blit(texto_surface, (ancho // 2 - texto_surface.get_width() // 2, y_offset))
        y_offset += 60  # Espacio entre opciones (puedes ajustar este valor)

    # Dibujar flecha de retroceso
    dibujar_flecha_retroceso(pantalla)

    pygame.display.flip()

    esperando_seleccion = True
    while esperando_seleccion:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = evento.pos
                if clic_en_flecha_retroceso((x, y)):
                    esperando_seleccion = False
                    anterior(pantalla)  # Regresar a la pantalla anterior
                    return
                elif (alto // 2 - 60) <= y <= (alto // 2 - 20):
                    agregar_pregunta_individual()
                    esperando_seleccion = False
                elif (alto // 2 - 20) < y <= (alto // 2 + 20):
                    agregar_preguntas_csv()
                    esperando_seleccion = False

# Funciones para agregar preguntas

def agregar_pregunta_individual():
    pregunta = input("Ingrese la pregunta: ")
    opciones = [input("Ingrese la opción 1: "), input("Ingrese la opción 2: "), input("Ingrese la opción 3: ")]
    respuesta_correcta = input("Ingrese el número de la respuesta correcta (1-3): ")

    nueva_pregunta = {
        "pregunta": pregunta,
        "opciones": opciones,
        "respuesta_correcta": respuesta_correcta
    }

    try:
        with open('preguntas.json', 'r+') as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = []
            data.append(nueva_pregunta)
            file.seek(0)
            json.dump(data, file, indent=4)
    except FileNotFoundError:
        with open('preguntas.json', 'w') as file:
            json.dump([nueva_pregunta], file, indent=4)

def agregar_preguntas_csv():
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
                    "opciones": [row['opcion1'], row['opcion2'], row['opcion3']],
                    "respuesta_correcta": row['respuesta_correcta']
                }
                preguntas.append(pregunta)

        try:
            with open('preguntas.json', 'r+') as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError:
                    data = []
                data.extend(preguntas)
                file.seek(0)
                json.dump(data, file, indent=4)
        except FileNotFoundError:
            with open('preguntas.json', 'w') as file:
                json.dump(preguntas, file, indent=4)

    except Exception as e:
        print(f"Error al leer el archivo CSV: {e}")

# Función principal

def main():
    pygame.init()
    pantalla = pygame.display.set_mode((ancho, alto))
    pygame.display.set_caption("Mi Aplicación")

    corriendo = True
    while corriendo:
        mostrar_ajustes(pantalla)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False
                pygame.quit()
                sys.exit()
        # Lógica adicional para manejar eventos de usuario y cambiar de pantalla si es necesario

if __name__ == "__main__":
    main()
