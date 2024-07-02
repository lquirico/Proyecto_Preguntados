import pygame
import sys
import time
from config import *

def mostrar_top_10(pantalla, pantalla_anterior=None):
    pantalla.fill(NEGRO)

    font = pygame.font.Font('cross_boxed.ttf', 15)
    y_offset = 80

    # Título del TOP 10
    titulo_surface = font.render("TOP 10 Partidas", True, DORADO)
    pantalla.blit(titulo_surface, (ancho // 2 - titulo_surface.get_width() // 2, 20))
    
    # Mostrar cada partida en el TOP 10
    top_10 = cargar_top_10()
    for idx, partida in enumerate(top_10):
        nombre = partida['nombre']
        puntaje = partida['puntaje']
        fecha = partida['fecha']

        texto = f"{idx + 1}. {nombre} - Puntaje: {puntaje} - Fecha: {fecha}"
        texto_surface = font.render(texto, True, BLANCO)
        pantalla.blit(texto_surface, (ancho // 2 - texto_surface.get_width() // 2, y_offset))
        y_offset += 95

    pygame.display.flip()

    start_time = time.time()
    while time.time() - start_time < 10:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    if pantalla_anterior:
        pantalla_anterior(pantalla)

def cargar_top_10():
    # Esta función simula cargar los datos del top 10 desde algún archivo o base de datos
    return [
        {"nombre": "Jugador 1", "puntaje": 100, "fecha": "2024-06-23"},
        {"nombre": "Jugador 2", "puntaje": 90, "fecha": "2024-06-22"},
        {"nombre": "Jugador 3", "puntaje": 80, "fecha": "2024-06-21"},
        {"nombre": "Jugador 4", "puntaje": 70, "fecha": "2024-06-20"},
        {"nombre": "Jugador 5", "puntaje": 60, "fecha": "2024-06-19"},
        {"nombre": "Jugador 6", "puntaje": 50, "fecha": "2024-06-18"},
        {"nombre": "Jugador 7", "puntaje": 40, "fecha": "2024-06-17"},
        {"nombre": "Jugador 8", "puntaje": 30, "fecha": "2024-06-16"},
        {"nombre": "Jugador 9", "puntaje": 20, "fecha": "2024-06-15"},
        {"nombre": "Jugador 10", "puntaje": 10, "fecha": "2024-06-14"},
    ]

def main():
    pygame.init()
    pantalla = pygame.display.set_mode((ancho, alto))
    pygame.display.set_caption("Top 10 Partidas")

    while True:
        mostrar_top_10(pantalla, mostrar_menu_principal)

def mostrar_menu_principal(pantalla):
    pantalla.fill(NEGRO)
    font = pygame.font.Font(None, 36)
    titulo_surface = font.render("Menu Principal", True, DORADO)
    pantalla.blit(titulo_surface, (ancho // 2 - titulo_surface.get_width() // 2, alto // 2 - titulo_surface.get_height() // 2))
    pygame.display.flip()

if __name__ == "__main__":
    main()
