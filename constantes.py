import pygame
#---------------------------------------------
#Colores
# Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AMARILLO = (255, 255, 0)


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# Tamaño pantalla
PANTALLA_TAMAÑO = (600, 1000)
TAMAÑO_PREGUNTA = (380, 160)



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# Coordenadas botones
button_A = pygame.Rect(195, 641, 215, 78)
button_B = pygame.Rect(195, 744, 215, 78)
button_C = pygame.Rect(195, 841, 215, 78)


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# Configurar la pantalla
ancho, alto = 600, 1000  # Tamaño de pantalla ajustado
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Menú de Pygame")


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# Posiciones
posiciones_y = []


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# Colores
DORADO = (201, 169, 41)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
BLANCO = (255, 255, 255)


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# Opciones del menú
opciones = ["Iniciar Juego", "Top 10 Puntajes", "Ajustes", "Salir"]
indice_seleccionado = None  # None para indicar que ninguna opción está seleccionada inicialmente


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# Margen superior e inferior
margen_superior = 50
margen_inferior = 50
espacio_entre_opciones = 130


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# Cargar imágenes
icono_iniciar = pygame.image.load('image/iniciar.png')
icono_top10 = pygame.image.load('image/top10.png')
icono_ajustes = pygame.image.load('image/ajustes.png')
icono_salir = pygame.image.load('image/salir.png')


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# Redimensionar imágenes a un tamaño mayor (300x100 píxeles)
icono_iniciar = pygame.transform.scale(icono_iniciar, (300, 100))
icono_top10 = pygame.transform.scale(icono_top10, (300, 100))
icono_ajustes = pygame.transform.scale(icono_ajustes, (300, 100))
icono_salir = pygame.transform.scale(icono_salir, (300, 100))


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# Ajustar posición de cada opción del menú
pos_x_iniciar = ancho // 2 - icono_iniciar.get_width() // 2 - 12  # Mover iniciar 10 píxeles a la izquierda
pos_x_top10 = ancho // 2 - icono_top10.get_width() // 2 - 15  # Mover top 10 15 píxeles a la izquierda y luego 15 a la derecha
pos_x_ajustes = ancho // 2 - icono_ajustes.get_width() // 2 - 15  # Mover ajustes 15 píxeles a la izquierda
pos_x_salir = ancho // 2 - icono_salir.get_width() // 2 - 15  # Mover salir 15 píxeles a la izquierda
