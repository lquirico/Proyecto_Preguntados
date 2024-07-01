from constantes import *
import pygame
import sys
import os
import json
from datetime import datetime





def guardar_puntajes(nombre, puntos):
    """Esta funcion se encarga de guardar los puntajes del juego , guardando los datos en un diccionario, el nombre, los puntos y la fecha en la que se jugo
    verifica si el json existe y si es asi agrega el diccionario con el nombre y los puntos recibidos por argumento a la lista para ser guardados en el json
    y ser ordenados con el metodo sorted

    Args:
        nombre (str): nombre que se recibe de la funcion pedir_nombre para ser guardado en el diccionario que es guardado en la variable entrada 
        puntos (int|str): puntos recolectados de la funcion inicio_juego son los puntos que realizo el jugador, cada pregunta correcta vale 50 puntos
    """
    fecha_hoy = datetime.now().strftime("%d-%m-%Y")
    entrada = {"nombre": nombre, "puntos": puntos, "fecha": fecha_hoy}
    
    if os.path.exists("data/puntajes.json"):
        with open("data/puntajes.json", "r", encoding="utf-8") as archivo:
            puntajes = json.load(archivo)
    else:
        puntajes = []

    puntajes.append(entrada)
    puntajes = sorted(puntajes, key=lambda x: x["puntos"], reverse=True)[:10]

    with open("data/puntajes.json", "w", encoding="utf-8") as archivo:
        json.dump(puntajes, archivo, ensure_ascii=False, indent=4)


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def pedir_nombre(pantalla, fuente):
    """Esta funcion solicita el nombre del jugador en pantalla para ser ingresado por teclado y con enter ser enviado
    retornando el nombre del jugador

    Args:
        pantalla (class): Recibe como argumento la pantalla de pygame.display donde va ser bliteador para que se vea el texto ingresado 
        fuente (class): recibe pygame.font.Sysfont es la fuente del texto que va a tener 

    Returns:
        nombre(str): la funcion retornar el nombre que se ingreso
    """
    nombre = ""
    pedir_nombre = True
    imagen_game_over = pygame.image.load("image/gameover.jpeg")

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
        pantalla.blit(imagen_game_over,(80,70))
        pantalla.blit(texto, (100, 500))
        pygame.display.flip()

    return nombre


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def mostrar_puntajes(pantalla, fuente):
    """Esta funcion muestra los puntajes en pantalla

    Args:
        pantalla (class): pantalla donde se va a mostrar los puntajes
        fuente (class): fuente de pygame con la que se van a mostrar los puntajes
    """
    if os.path.exists("data/puntajes.json"):
        with open("data/puntajes.json", "r", encoding="utf-8") as archivo:
            puntajes = json.load(archivo)
    else:
        puntajes = []
    imagen_marco_top = pygame.image.load("image/marcoTop.png")
    imagen_marco_top_transformada = pygame.transform.scale(imagen_marco_top, (850,1050))
    imagen_top_10 = pygame.image.load("image/top10image.jpeg")
    imagen_top_10_transformada = pygame.transform.scale(imagen_top_10,(250,100))
    y_separacion = 300
    pantalla.fill(NEGRO)
    pantalla.blit(imagen_marco_top_transformada, (-105,0))
    pantalla.blit(imagen_top_10_transformada, (170,120))
    for puntaje in puntajes:
        texto = f"{puntaje['nombre']}: {puntaje['puntos']} puntos (Fecha: {puntaje['fecha']})"
        superficie_texto = fuente.render(texto, True, BLANCO)
        pantalla.blit(superficie_texto, (120, y_separacion))
        y_separacion += 50
        if y_separacion > 900:
            break
    
    
    pygame.display.update()
    pygame.time.wait(4000)  # Esperar 4 segundos antes de regresar al menú principal