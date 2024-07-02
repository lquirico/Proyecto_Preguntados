import pygame

ancho, alto = 600, 1000
posiciones_y = []
DORADO = (201, 169, 41)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
BLANCO = (255, 255, 255)
opciones = ["Iniciar Juego", "Top 10 Puntajes", "Ajustes", "Salir"]
indice_seleccionado = None
margen_superior = 50
margen_inferior = 50
espacio_entre_opciones = 150

posiciones_y =[]

# Rutas de los archivos de imágenes
ruta_icono_iniciar = 'iniciar.png'
ruta_icono_top10 = 'top10.png'
ruta_icono_ajustes = 'ajustes.png'
ruta_icono_salir = 'salir.png'
ruta_imagen_preguntados = 'preguntados.png'
ruta_fuente = 'cross_boxed.ttf'
# Ruta a la música de fondo
ruta_musica_fondo = 'musica_fondo.mp3'

# Volumen inicial de la música (de 0.0 a 1.0)
volumen_inicial = 0.5  # 50% del volumen máximo

# Cargar imágenes
icono_iniciar = pygame.image.load(ruta_icono_iniciar)
icono_top10 = pygame.image.load(ruta_icono_top10)
icono_ajustes = pygame.image.load(ruta_icono_ajustes)
icono_salir = pygame.image.load(ruta_icono_salir)
imagen_preguntados = pygame.image.load(ruta_imagen_preguntados)
icono_flecha_izquierda = pygame.image.load('flecha_izquierda.png')
flecha_arriba = pygame.image.load('flecha_arriba.png')
flecha_abajo = pygame.image.load('flecha_abajo.png')

# Escalar imágenes
icono_iniciar = pygame.transform.scale(icono_iniciar, (250, 100))
icono_top10 = pygame.transform.scale(icono_top10, (250, 100))
icono_ajustes = pygame.transform.scale(icono_ajustes, (250, 100))
icono_salir = pygame.transform.scale(icono_salir, (250, 100))
imagen_preguntados = pygame.transform.scale(imagen_preguntados, (700, 340))
icono_flecha_izquierda = pygame.transform.scale(icono_flecha_izquierda, (50, 50))

# Definir posiciones
pos_x_iniciar = ancho // 2 - icono_iniciar.get_width() // 2 - 15
pos_x_top10 = ancho // 2 - icono_top10.get_width() // 2 - 15
pos_x_ajustes = ancho // 2 - icono_ajustes.get_width() // 2 - 15
pos_x_salir = ancho // 2 - icono_salir.get_width() // 2 - 15
pos_x_preguntados = ancho // 2 - imagen_preguntados.get_width() // 2
pos_y_preguntados = 50
pos_x_flecha_izquierda = 20  
pos_y_flecha_izquierda = 20

# Fuentes
pygame.font.init()
fuente_predeterminada = pygame.font.Font(None, 36)
fuente_ajustes = pygame.font.Font('cross_boxed.ttf', 36)

def dibujar_flecha_retroceso(pantalla):
    pygame.draw.polygon(pantalla, BLANCO, [(20, 20), (40, 10), (40, 30)])  # Dibujar una flecha simple

def clic_en_flecha_retroceso(pos):
    x, y = pos
    return 10 <= x <= 40 and 10 <= y <= 30



