import pygame
import sys
from config import *
from menu import dibujar_menu
from top_10 import mostrar_top_10
from ajustes import*

def main():
    global indice_seleccionado
    pygame.init()
    pantalla = pygame.display.set_mode((ancho, alto))
    pygame.display.set_caption("Menú de Pygame")
    reloj = pygame.time.Clock()
    corriendo = True

    # Cargar y reproducir música de fondo en bucle
    pygame.mixer.music.load(ruta_musica_fondo)
    pygame.mixer.music.set_volume(0.5)  # Ajusta el volumen de la música
    pygame.mixer.music.play(-1)  # -1 indica que la música se reproducirá en bucle

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
                        elif indice_seleccionado == 1:
                            print("Top 10 Puntajes seleccionado")
                            mostrar_top_10(pantalla)
                        elif indice_seleccionado == 2:
                            print("Ajustes seleccionado")
                            mostrar_ajustes(pantalla)
                        elif indice_seleccionado == 3:
                            corriendo = False
        
        dibujar_menu(pantalla)
        reloj.tick(30)

    pygame.mixer.music.stop()  # Detener la música al salir del juego
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()  