import os
import pygame
import sys
import json
import csv
from tkinter import Tk, filedialog
from config import *
import time
from constantes import *
# Funciones relacionadas con pygame y UI

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def dibujar_flecha_retroceso(pantalla):
    pygame.draw.polygon(pantalla, BLANCO, [(10, 20), (30, 10), (30, 30)])  # Dibujar una flecha simple

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def clic_en_flecha_retroceso(pos):
    x, y = pos
    return 10 <= x <= 30 and 10 <= y <= 30



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


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


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def mostrar_volumen(pantalla):
    pantalla.fill(NEGRO)
    
    # Título de Volumen
    titulo_surface = fuente_predeterminada.render("Ajustes de Volumen", True, DORADO)
    pantalla.blit(titulo_surface, (ancho // 2 - titulo_surface.get_width() // 2, 50))

    # Opciones de Volumen
    opciones_volumen = ["Activar/Desactivar", "Subir Volumen", "Bajar Volumen"]
    y_offset = (alto - len(opciones_volumen) * 50) // 2

    # Lista de rectángulos de las opciones
    rects_opciones = []

    for i, opcion in enumerate(opciones_volumen):
        texto_surface = fuente_ajustes.render(opcion, True, BLANCO)
        x_pos_texto = (ancho - texto_surface.get_width()) // 2
        
        # Dibujar el texto
        pantalla.blit(texto_surface, (x_pos_texto, y_offset))

        if "Subir" in opcion:
            flecha_x = x_pos_texto + texto_surface.get_width() + 10  # Posición horizontal de la flecha de subir
            flecha_y = y_offset + (texto_surface.get_height() // 4) + 10  # Posición vertical de la flecha de subir (centrada verticalmente con un ajuste)
            pygame.draw.polygon(pantalla, BLANCO, [(flecha_x, flecha_y), (flecha_x + 10, flecha_y - 16), (flecha_x + 20, flecha_y)])  # Dibuja una flecha hacia arriba
        elif "Bajar" in opcion:
            flecha_x = x_pos_texto + texto_surface.get_width() + 10  # Posición horizontal de la flecha de bajar
            flecha_y = y_offset + (texto_surface.get_height() // 3) - 10  # Posición vertical de la flecha de bajar (centrada verticalmente con un ajuste)
            pygame.draw.polygon(pantalla, BLANCO, [(flecha_x, flecha_y), (flecha_x + 10, flecha_y + 17), (flecha_x + 20, flecha_y)])  # Dibuja una flecha hacia abajo
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


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



def blit_text(surface, text, pos, font, color=pygame.Color('black')):
    words = [word.split(' ') for word in text.splitlines()]
    space = font.size(' ')[0]
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, False, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]
                y += word_height
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]
        y += word_height


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def activar_desactivar_volumen():
    global volumen_activo
    volumen_activo = not volumen_activo
    pygame.mixer.music.set_volume(volumen_nivel / 100.0 if volumen_activo else 0)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def ajustar_volumen(cambio):
    global volumen_nivel
    volumen_nivel = max(0, min(100, volumen_nivel + cambio))
    if volumen_activo:
        pygame.mixer.music.set_volume(volumen_nivel / 100.0)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Funciones para agregar preguntas
def actualizar_estadisticas(pregunta, respuesta_correcta):
    """Esta funcion actualiza la estadistica que se encuentra en el csv al final de cada pregunta, sumando de a 1 la cantidad de aciertos y fallos
    y sacando el porcentaje de la cantidad de veces que fue preguntado y la cantidad de aciertos. 

    Args:
        pregunta (list[dict]): Recibe como argumento una lista de diccionario
        respuesta_correcta (bool): Si el bool recibido es True suma un acierto caso contrario suma a cantidad fallido de a 1
    """

    pregunta["cantidad_veces_preguntada"] += 1
    if respuesta_correcta:
        pregunta["cantidad_aciertos"] += 1
    else:
        pregunta["cantidad_fallos"] += 1

    if pregunta["cantidad_veces_preguntada"] > 0:
        pregunta["porcentaje_aciertos"] = (pregunta["cantidad_aciertos"] / pregunta["cantidad_veces_preguntada"]) * 100

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def guardar_estadisticas(nombre_archivo, lista_preguntas):
    """Esta funcion guarda los datos recolectados del juego, porcentaje de aciertos, 
    cantidad de fallos, cantidad de aciertos, cantidad de veces preguntada

    Args:
        nombre_archivo (str): nombre_archivo es el path donde se va a guardar el juego en el archivo csv
        lista_preguntas (list[dict]): Es una lista de diccionarios que se va a iterar para escribir los datos nuevos
    """
    fieldnames = ["pregunta", "respuesta_a", "respuesta_b", "respuesta_c", "respuesta_correcta", "porcentaje_aciertos", "cantidad_fallos", "cantidad_aciertos", "cantidad_veces_preguntada"]
    with open(nombre_archivo, 'w', newline='', encoding='utf-8') as archivo:
        writer = csv.DictWriter(archivo, fieldnames=fieldnames)
        writer.writeheader()
        for pregunta in lista_preguntas:
            writer.writerow(pregunta)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



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
                    agregar_preguntas_csv("data\preguntas.csv")
                    esperando_seleccion = False



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def agregar_pregunta_individual():
    """Esta funcion solicita una pregunta individual para ingresar al juego
    """
    lista_preguntas = parse_csv("data\preguntas.csv")
    pregunta = input("Ingrese la pregunta: ")
    respuesta_a, respuesta_b, respuesta_c = input("Ingrese la opción a: "), input("Ingrese la opción b: "), input("Ingrese la opción c: ")
    respuesta_correcta = input("Ingrese el número de la respuesta correcta (a, b ,c): ").lower()

    nueva_pregunta = {
        "pregunta": pregunta,
        "respuesta_a":respuesta_a,
        "respuesta_b":respuesta_b,
        "respuesta_c":respuesta_c,
        "respuesta_correcta": respuesta_correcta
    }

    lista_preguntas.append(nueva_pregunta)
    actualizar_csv(lista_preguntas, "data/preguntas.csv")

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def press_space_button():
    """Esta funcion crea una cortina animada como los juegos clasicos, una vez precionado el boton space el juego comienza y va al menu
    """

    #Carga de imagenes y escalado
    cortina_izquierda = pygame.image.load("image/11014.jpg")
    cortina_izquierda_transformada = pygame.transform.scale(cortina_izquierda,(600,1000))
    cortina_derecha = pygame.image.load("image/11014.jpg")
    cortina_derecha_transformada = pygame.transform.scale(cortina_derecha,(600,1000))
    # Obtener el tamaño de las cortinas por medio de get_rect, obteniendo el tamaño del rectangulo de la misma imagen
    cortina_rect_izquierda = cortina_izquierda_transformada.get_rect()
    cortina_rect_derecha = cortina_derecha_transformada.get_rect()
    
    # Configuración de las posiciones iniciales de las cortinas una arriba a la izquierda y otra en medio a 600px de x, topleft y 
    # top right son propiedades de la clase rect, topleft indica que la esquina superior izquierda comienza en 0  y top right indica
    #  que la esquina superior derecha comienza en 600
    cortina_rect_izquierda.topleft = (0, 0)
    cortina_rect_derecha.topright = (600, 0)

    fuente_press_space = pygame.font.SysFont("Arial", 20)
    fuente_desarrollado_por = pygame.font.SysFont("Arial",15)
    texto_press_space = fuente_press_space.render("press space to start", True, BLANCO)
    #rectangulo_texto obtiene el tamaño de rectangulo de texto_press_space y lo centra en las cordenadas indicadas como argumento en la 
    # funcion get_rect()
    rectangulo_texto = texto_press_space.get_rect(center=(300, 500))
    texto_desarrollo = fuente_desarrollado_por.render("Desarrollado por: Pedro Gabriel Paz, Lucia Quirico, Diego Javier Olivera", True, BLANCO)
    rectangulo_desarrollo = texto_desarrollo.get_rect(center = (300,950))
    flag_corriendo = True
    mostrar_texto = True
    abrir_cortinas = False
    ultimo_tiempo = time.time()

    while flag_corriendo:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag_corriendo = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                mostrar_texto = False
                abrir_cortinas = True


        if abrir_cortinas:
            if cortina_rect_izquierda.right > 0:
                cortina_rect_izquierda.x -= 1
            if cortina_rect_derecha.left < 600:
                cortina_rect_derecha.x += 1
            if cortina_rect_izquierda.right <= 0 and cortina_rect_derecha.left >= 600:
                flag_corriendo = False

        # Alternar la visibilidad del texto cada 2 segundos
        current_time = time.time()
        if not abrir_cortinas and current_time - ultimo_tiempo >= 0.5:
            mostrar_texto = not mostrar_texto
            ultimo_tiempo = current_time

        pantalla.fill(NEGRO)  # Limpiar la pantalla con un color negro
        pantalla.blit(cortina_izquierda_transformada, cortina_rect_izquierda)
        pantalla.blit(cortina_derecha_transformada, cortina_rect_derecha)
        pantalla.blit(texto_desarrollo, rectangulo_desarrollo)
        if mostrar_texto:
            pantalla.blit(texto_press_space, rectangulo_texto)
            
        pygame.display.update()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def actualizar_csv(lista_proyectos, nombre_archivo, manejo_archivo):
    """Esta funcion vuelve a comvertir la lista a un archivo csv para ser guardado, con ,keys()
    guarda en la primera fila las keys y luego comienza a guardar los valores

    Args:
        lista_proyectos (list[dict]): Recibe una lista de diccionarios 
        nombre_archivo (str): Nombre de archivo que tiene que ser actualizado
    """
    # Abrir el archivo CSV en modo escritura
    with open(nombre_archivo, 'w', newline='', encoding='utf-8') as archivo:
        
        # Defino los nombres de las columnas buscando en el primer diccionario todas las claves.
        columnas = lista_proyectos[0].keys()
        
        # Creo el escritor CSV con DicWriter que me permite escribir diccionarios
        escritor_csv = csv.DictWriter(archivo, fieldnames=columnas)
        
        escritor_csv.writeheader()  #writeheader() crea el encabezado
        
        #Itero y escribo los datos de cada proyecto en el archivo CSV
        for proyecto in lista_proyectos:
            escritor_csv.writerow(proyecto)
    
    print(f"El archivo {nombre_archivo} se ha actualizado correctamente.")

def sumar_csv_a_csv(lista_proyectos, nombre_archivo):
    """Esta funcion suma preguntas al archivo csv original del juego, escribiendo desde donde finaliza el archivo original
    omitiendo los encabazados por que ya estan en el archivo

    Args:
        lista_proyectos (list[dict]): Recibe una lista de diccionarios 
        nombre_archivo (str): Nombre del archivo que tiene al que le tiene que sumar las nuevas preguntas 
    """
    # Abrir el archivo CSV en modo añadir ('a')
    with open(nombre_archivo, 'a', newline='', encoding='utf-8') as archivo:
        # Defino los nombres de las columnas buscando en el primer diccionario todas las claves
        columnas = lista_proyectos[0].keys()
        
        # Creo el escritor CSV con DictWriter que me permite escribir diccionarios
        escritor_csv = csv.DictWriter(archivo, fieldnames=columnas)
        
        # Itero y escribo los datos de cada proyecto en el archivo CSV
        for proyecto in lista_proyectos:
            escritor_csv.writerow(proyecto)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def parse_csv(nombre_archivo: str):
    """Esta funcion convierte el contenido del archivo csv a una lista con diccionarios

    Args:
        nombre_archivo (str): recibe como argumento el path o ruta del archivo csv

    Returns:
        lista_preguntas(list[dict]): retorna una lista con diccionarios con el contenido del csv 
    """
    lista_preguntas = []
    columnas_requeridas = ["porcentaje_aciertos", "cantidad_fallos", "cantidad_aciertos", "cantidad_veces_preguntada"]

    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            reader = csv.DictReader(archivo)
            for row in reader:
                for columna in columnas_requeridas:
                    if columna not in row or row[columna] == '':
                        row[columna] = 0  # Establecer valor predeterminado
                diccionario_aux = {
                    "pregunta": row["pregunta"],
                    "respuesta_a": row["respuesta_a"],
                    "respuesta_b": row["respuesta_b"],
                    "respuesta_c": row["respuesta_c"],
                    "respuesta_correcta": row["respuesta_correcta"],
                    "porcentaje_aciertos": float(row["porcentaje_aciertos"]),
                    "cantidad_fallos": int(row["cantidad_fallos"]),
                    "cantidad_aciertos": int(row["cantidad_aciertos"]),
                    "cantidad_veces_preguntada": int(row["cantidad_veces_preguntada"])
                }
                lista_preguntas.append(diccionario_aux)
        return lista_preguntas
    else:
        print("ARCHIVO NO ENCONTRADO")
        return []

def agregar_preguntas_csv(ruta_csv_original):
    """Esta funcion agrega preguntas en grupo, ingresando un archivo csv

    Args:
        ruta_csv_original (str): Path csv del juego donde estan las preguntas originalmente
    """
    Tk().withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path == "":
        return

    try:
        lista_preguntas_nueva = parse_csv(file_path)
        sumar_csv_a_csv(lista_preguntas_nueva,ruta_csv_original)
        print("El archivo se ingreso correctamente")
    except:
        print("No se pudo ingresar el archivo")
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


