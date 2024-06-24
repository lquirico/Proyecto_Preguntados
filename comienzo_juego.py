import pygame
import sys
import os
import json
from datetime import datetime

pygame.init()

# Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AMARILLO = (255, 255, 0)

# Tamaño pantalla
PANTALLA_TAMAÑO = (600, 1000)
TAMAÑO_PREGUNTA = (380, 160)

# Coordenadas botones
button_A = pygame.Rect(195, 641, 215, 78)
button_B = pygame.Rect(195, 744, 215, 78)
button_C = pygame.Rect(195, 841, 215, 78)

# Configurar la pantalla
ancho, alto = 600, 1000  # Tamaño de pantalla ajustado
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Menú de Pygame")

# Posiciones
posiciones_y = []

# Colores
DORADO = (201, 169, 41)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
BLANCO = (255, 255, 255)

# Opciones del menú
opciones = ["Iniciar Juego", "Top 10 Puntajes", "Ajustes", "Salir"]
indice_seleccionado = None  # None para indicar que ninguna opción está seleccionada inicialmente

# Margen superior e inferior
margen_superior = 50
margen_inferior = 50
espacio_entre_opciones = 150

# Cargar imágenes
icono_iniciar = pygame.image.load('INICIAR.png')
icono_top10 = pygame.image.load('TOP 10.png')
icono_ajustes = pygame.image.load('AJUSTES.png')
icono_salir = pygame.image.load('SALIR.png')

# Redimensionar imágenes a un tamaño mayor (300x100 píxeles)
icono_iniciar = pygame.transform.scale(icono_iniciar, (300, 100))
icono_top10 = pygame.transform.scale(icono_top10, (300, 100))
icono_ajustes = pygame.transform.scale(icono_ajustes, (300, 100))
icono_salir = pygame.transform.scale(icono_salir, (300, 100))

# Ajustar posición de cada opción del menú
pos_x_iniciar = ancho // 2 - icono_iniciar.get_width() // 2 - 12  # Mover iniciar 10 píxeles a la izquierda
pos_x_top10 = ancho // 2 - icono_top10.get_width() // 2 - 15  # Mover top 10 15 píxeles a la izquierda y luego 15 a la derecha
pos_x_ajustes = ancho // 2 - icono_ajustes.get_width() // 2 - 15  # Mover ajustes 15 píxeles a la izquierda
pos_x_salir = ancho // 2 - icono_salir.get_width() // 2 - 15  # Mover salir 15 píxeles a la izquierda

# Dibujar menú
def dibujar_menu():
    pantalla.fill(NEGRO)
    
    global posiciones_y, indice_seleccionado  # Asegurarse de usar las variables globales
    
    posiciones_y.clear()
    for i, (icono, pos_x) in enumerate([(icono_iniciar, pos_x_iniciar), (icono_top10, pos_x_top10),
                                        (icono_ajustes, pos_x_ajustes), (icono_salir, pos_x_salir)]):
        # Centrar verticalmente cada opción
        pos_y = alto // 2 - icono.get_height() // 2 + i * espacio_entre_opciones
        
        posiciones_y.append((pos_x, pos_y, icono.get_width(), icono.get_height()))
        
        # Verificar si el mouse está sobre esta opción
        x, y = pygame.mouse.get_pos()
        if pos_x <= x <= pos_x + icono.get_width() and pos_y <= y <= pos_y + icono.get_height():
            # Dibujar rectángulo dorado alrededor de la opción
            pygame.draw.rect(pantalla, DORADO, (pos_x - 10, pos_y - 10, icono.get_width() + 20, icono.get_height() + 20), 3)
        
        pantalla.blit(icono, (pos_x, pos_y))
    
    pygame.display.flip()

def main():
    global indice_seleccionado
    reloj = pygame.time.Clock()
    corriendo = True

    while corriendo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = evento.pos
                for i, (pos_x, pos_y, width, height) in enumerate(posiciones_y):
                    if pos_x <= x <= pos_x + width and pos_y <= y <= pos_y + height:
                        indice_seleccionado = i
                        if indice_seleccionado == 0:
                            print("Iniciar Juego seleccionado")
                            inicio_juego()
                            # Aquí se podría llamar a la función para iniciar el juego
                        elif indice_seleccionado == 1:
                            mostrar_puntajes(pantalla,pygame.font.SysFont("Arial", 30))
                            print("Top 10 Puntajes seleccionado")
                            # Mostrar el TOP 10 de puntajes
                        elif indice_seleccionado == 2:
                            print("Ajustes seleccionado")
                            # Mostrar la pantalla de ajustes
                        elif indice_seleccionado == 3:
                            corriendo = False
        
        dibujar_menu()
        reloj.tick(30)

    pygame.quit()
    sys.exit()

def parse_csv(nombre_archivo: str):
    lista_preguntas = []
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            primer_linea = archivo.readline().replace("\n", "")
            lista_claves = primer_linea.split(",")

            for linea in archivo:
                linea_aux = linea.replace("\n", "")
                lista_valores = linea_aux.split(",")
                diccionario_aux = {lista_claves[i]: lista_valores[i] for i in range(len(lista_claves))}
                lista_preguntas.append(diccionario_aux)
        return lista_preguntas
    else:
        print("ARCHIVO NO ENCONTRADO")
        return []

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

def guardar_puntajes(nombre, puntos):
    fecha_hoy = datetime.now().strftime("%Y-%m-%d")
    entrada = {"nombre": nombre, "puntos": puntos, "fecha": fecha_hoy}
    
    if os.path.exists("puntajes.json"):
        with open("puntajes.json", "r", encoding="utf-8") as archivo:
            puntajes = json.load(archivo)
    else:
        puntajes = []

    puntajes.append(entrada)
    puntajes = sorted(puntajes, key=lambda x: x["puntos"], reverse=True)[:10]

    with open("puntajes.json", "w", encoding="utf-8") as archivo:
        json.dump(puntajes, archivo, ensure_ascii=False, indent=4)

def pedir_nombre(pantalla, fuente):
    nombre = ""
    pedir_nombre = True

    while pedir_nombre:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    pedir_nombre = False
                elif evento.key == pygame.K_BACKSPACE:
                    nombre = nombre[:-1]
                else:
                    nombre += evento.unicode

        pantalla.fill(NEGRO)
        texto = fuente.render("Ingrese su nombre: " + nombre, True, BLANCO)
        pantalla.blit(texto, (100, 500))
        pygame.display.flip()

    return nombre

def mostrar_puntajes(pantalla, fuente):
    if os.path.exists("puntajes.json"):
        with open("puntajes.json", "r", encoding="utf-8") as archivo:
            puntajes = json.load(archivo)
    else:
        puntajes = []

    pantalla.fill(NEGRO)
    y_offset = 50
    for puntaje in puntajes:
        texto = f"{puntaje['nombre']}: {puntaje['puntos']} puntos (Fecha: {puntaje['fecha']})"
        superficie_texto = fuente.render(texto, True, BLANCO)
        pantalla.blit(superficie_texto, (50, y_offset))
        y_offset += 50
        if y_offset > 900:
            break
    pygame.display.flip()
    pygame.time.wait(10000)  # Esperar 10 segundos antes de regresar al menú principal
    main()

def inicio_juego():
    lista_preguntas = parse_csv('preguntas.csv')
    if not lista_preguntas:
        return

    pantalla = pygame.display.set_mode(PANTALLA_TAMAÑO)
    icono = pygame.image.load("WhatsApp Image 2024-06-20 at 21.59.16.jpeg")
    pygame.display.set_caption("Juego preguntados")
    pygame.display.set_icon(icono)
    pygame.mixer.init()
    
    sonido = pygame.mixer.Sound("tic_tac.mp3")

    imagen_opcion_a = pygame.image.load("opcionA.jpeg")
    imagen_opcion_a_transformada = pygame.transform.scale(imagen_opcion_a, (300, 100))
    imagen_opcion_b = pygame.image.load("opcionB.jpeg")
    imagen_opcion_b_transformada = pygame.transform.scale(imagen_opcion_b, (305, 100))
    imagen_opcion_c = pygame.image.load("opcionC.jpeg")
    imagen_opcion_c_transformada = pygame.transform.scale(imagen_opcion_c, (300, 90))
    imagen_pregunta = pygame.image.load("pregunta.png")
    imagen_pregunta_tranformada = pygame.transform.scale(imagen_pregunta, (500, 300))

    fuente = pygame.font.SysFont("Arial", 30)
    fuente_respuesta = pygame.font.SysFont("Arial", 20)
    fuente_segundero = pygame.font.SysFont("Arial", 40)

    evento_tiempo = pygame.USEREVENT
    pygame.time.set_timer(evento_tiempo, 1000)
    segundero = 30
    puntos = 0
    pregunta_actual = 0
    intentos = 3  # Contador de intentos

    flag_run = True
    flag_sonido = True

    while flag_run:
        if flag_sonido:
            sonido.play()
            flag_sonido = False
        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                flag_run = False
            elif evento.type == pygame.MOUSEMOTION:
                x, y = evento.pos
            if evento.type == evento_tiempo:
                segundero -= 1
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if button_A.collidepoint(evento.pos):
                    if lista_preguntas[pregunta_actual]["respuesta_correcta"] == "a":
                        puntos += 50
                        segundero = 30
                        pregunta_actual = (pregunta_actual + 1) % len(lista_preguntas)
                        sonido.stop()
                        sonido.play()
                    else:
                        puntos -= 50
                        intentos -= 1
                elif button_B.collidepoint(evento.pos):
                    if lista_preguntas[pregunta_actual]["respuesta_correcta"] == "b":
                        puntos += 50
                        segundero = 30
                        pregunta_actual = (pregunta_actual + 1) % len(lista_preguntas)
                        sonido.stop()
                        sonido.play()
                    else:
                        puntos -= 50
                        intentos -= 1
                elif button_C.collidepoint(evento.pos):
                    if lista_preguntas[pregunta_actual]["respuesta_correcta"] == "c":
                        puntos += 50
                        segundero = 30
                        pregunta_actual = (pregunta_actual + 1) % len(lista_preguntas)
                        sonido.stop()
                        sonido.play()
                    else:
                        puntos -= 50
                        intentos -= 1

        pantalla.fill(NEGRO)
        texto_segundero = fuente_segundero.render(str(segundero), False, BLANCO)
        texto_puntos = fuente.render(f"Puntos: {puntos}", False, BLANCO)
        texto_intentos = fuente.render(f"Intentos: {intentos}", False, BLANCO)
        pantalla.blit(imagen_pregunta_tranformada, (50, 350))
        pantalla.blit(imagen_opcion_a_transformada, (120, 630))
        pantalla.blit(imagen_opcion_b_transformada, (120, 730))
        pantalla.blit(imagen_opcion_c_transformada, (120, 830))
        pantalla.blit(icono, (0, 0))
        pantalla.blit(texto_segundero, (35, 340))
        pantalla.blit(texto_puntos, (450, 50))
        pantalla.blit(texto_intentos, (450, 100))

        pregunta = lista_preguntas[pregunta_actual]["pregunta"]
        respuesta_a = lista_preguntas[pregunta_actual]["respuesta_a"]
        respuesta_b = lista_preguntas[pregunta_actual]["respuesta_b"]
        respuesta_c = lista_preguntas[pregunta_actual]["respuesta_c"]

        carta_pregunta = pygame.Surface(TAMAÑO_PREGUNTA)
        blit_text(carta_pregunta, pregunta, (10, 10), fuente, BLANCO)
        pantalla.blit(carta_pregunta, (105, 420))

        blit_text(pantalla, respuesta_a, (button_A.x + 10, button_A.y + 20), fuente_respuesta, BLANCO)
        blit_text(pantalla, respuesta_b, (button_B.x + 10, button_B.y + 20), fuente_respuesta, BLANCO)
        blit_text(pantalla, respuesta_c, (button_C.x + 10, button_C.y + 20), fuente_respuesta, BLANCO)

        pygame.display.update()

        if intentos == 0 or pregunta_actual == len(lista_preguntas) - 1:
            sonido.stop()  # Detener la música
            nombre = pedir_nombre(pantalla, fuente)
            guardar_puntajes(nombre, puntos)
            mostrar_puntajes(pantalla, fuente)
            flag_run = False

    main()

main()
pygame.quit()
