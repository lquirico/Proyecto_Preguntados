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
    titulo_surface = fuente_ajustes.render("Ajustes", True, DORADO)
    pantalla.blit(titulo_surface, (ancho // 2 - titulo_surface.get_width() // 2, 50))

    # Opciones de Ajustes
    opciones_ajustes = ["Volumen", "Agregar Preguntas"]
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
                    mostrar_volumen(pantalla)  # Mostrar el menú de volumen
                    esperando_seleccion = False
                elif (alto // 2 + 20) < y <= (alto // 2 + 60):
                    print("Agregar Preguntas seleccionado")
                    mostrar_menu_agregar_preguntas(pantalla, mostrar_ajustes)  # Mostrar menú de agregar preguntas
                    esperando_seleccion = False

def mostrar_volumen(pantalla):
    pantalla.fill(NEGRO)
    
    # Título de Volumen
    titulo_surface = fuente_predeterminada.render("Ajustes de Volumen", True, DORADO)
    pantalla.blit(titulo_surface, (ancho // 2 - titulo_surface.get_width() // 2, 50))

    # Opciones de Volumen
    opciones_volumen = ["Activar/Desactivar", "Subir Volumen", "Bajar Volumen"]
    y_offset = (alto - len(opciones_volumen) * 50) // 2

    # Cargar imágenes de las flechas
    flecha_arriba = pygame.image.load('flecha_arriba.png')
    flecha_abajo = pygame.image.load('flecha_abajo.png')
    flecha_arriba = pygame.transform.scale(flecha_arriba, (30, 30))
    flecha_abajo = pygame.transform.scale(flecha_abajo, (30, 30))



    # Dimensiones de las flechas
    flecha_ancho, flecha_alto = flecha_arriba.get_size()
     # Lista de rectángulos de las opciones
    rects_opciones = []

    for i, opcion in enumerate(opciones_volumen):
        texto_surface = fuente_ajustes.render(opcion, True, BLANCO)
        x_pos_texto = (ancho - texto_surface.get_width()) // 2
        
        # Dibujar el texto
        pantalla.blit(texto_surface, (x_pos_texto, y_offset))

        if "Subir" in opcion:
            flecha_x = x_pos_texto + texto_surface.get_width() + 10  # Posición horizontal de la flecha
            flecha_y = y_offset + (texto_surface.get_height() // 2) - 8  # Posición vertical de la flecha hacia arriba
            pygame.draw.polygon(pantalla, BLANCO, [(flecha_x, flecha_y), (flecha_x + 10, flecha_y - 10), (flecha_x + 20, flecha_y)])  # Dibuja una flecha hacia arriba
        elif "Bajar" in opcion:
            flecha_x = x_pos_texto + texto_surface.get_width() + 10  # Posición horizontal de la flecha
            flecha_y = y_offset + (texto_surface.get_height() // 2) + 4  # Ajusta este valor para reducir el espacio entre las flechas
            pygame.draw.polygon(pantalla, BLANCO, [(flecha_x, flecha_y), (flecha_x + 10, flecha_y + 10), (flecha_x + 20, flecha_y)])  # Dibuja una flecha hacia abajo
        # Guardar el rectángulo de la opción
        rects_opciones.append(pygame.Rect(x_pos_texto, y_offset, texto_surface.get_width() + 40, texto_surface.get_height()))

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
                    mostrar_ajustes(pantalla)  # Volver al menú anterior
                    return
                for i, rect in enumerate(rects_opciones):
                    if rect.collidepoint(x, y):
                        if i == 0:
                            activar_desactivar_volumen()
                        elif i == 1:
                            ajustar_volumen(10)  # Subir volumen
                        elif i == 2:
                            ajustar_volumen(-10)  # Bajar volumen
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_9:
                    ajustar_volumen(10)  # Subir volumen
                elif evento.key == pygame.K_0:
                    ajustar_volumen(-10)  # Bajar volumen
# Funciones para manejar el volumen
volumen_activo = True
volumen_nivel = 100  # Nivel de volumen inicial (puede ser de 0 a 100)

def activar_desactivar_volumen():
    global volumen_activo
    volumen_activo = not volumen_activo
    pygame.mixer.music.set_volume(volumen_nivel / 100.0 if volumen_activo else 0)

def ajustar_volumen(cambio):
    global volumen_nivel
    volumen_nivel = max(0, min(100, volumen_nivel + cambio))
    if volumen_activo:
        pygame.mixer.music.set_volume(volumen_nivel / 100.0)

# Funciones para agregar preguntas

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