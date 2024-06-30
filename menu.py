import pygame
from config import *

def dibujar_menu(pantalla):
    pantalla.fill(NEGRO)
    
    global posiciones_y, indice_seleccionado

    pantalla.blit(imagen_preguntados, (pos_x_preguntados, pos_y_preguntados))
    
    posiciones_y.clear()
    for i, (icono, pos_x) in enumerate([(icono_iniciar, pos_x_iniciar), (icono_top10, pos_x_top10),
                                        (icono_ajustes, pos_x_ajustes),
                                        (icono_salir, pos_x_salir)]):
        pos_y = pos_y_preguntados + imagen_preguntados.get_height() + (i * espacio_entre_opciones) + 50
        posiciones_y.append((pos_x, pos_y, icono.get_width(), icono.get_height()))
        
        x, y = pygame.mouse.get_pos()
        if pos_x <= x <= pos_x + icono.get_width() and pos_y <= y <= pos_y + icono.get_height():
            pygame.draw.rect(pantalla, DORADO, (pos_x - 10, pos_y - 10, icono.get_width() + 20, icono.get_height() + 20), 3)
        
        pantalla.blit(icono, (pos_x, pos_y))
    
    pygame.display.flip()
