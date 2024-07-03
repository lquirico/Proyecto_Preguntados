from ajustes import *
from constantes import *
from top_10 import *
import pygame
import sys
from datetime import datetime
import random



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



pygame.init()



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# Dibujar menú
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

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------




def main():
    global indice_seleccionado
    reloj = pygame.time.Clock()
    corriendo = True
    icono = pygame.image.load("image/WhatsApp Image 2024-06-20 at 21.59.16.jpeg")
    pygame.display.set_caption("Juego preguntados")
    pygame.display.set_icon(icono)
    fuente_puntaje_boton = pygame.font.SysFont("Arial", 20)

    pygame.mixer.music.load(ruta_musica_fondo)
    pygame.mixer.music.set_volume(0.5)  # Ajusta el volumen de la música
    pygame.mixer.music.play(-1)  # -1 indica que la música se reproducirá en bucle
    press_space_button()
    while corriendo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False
            elif evento.type == pygame.MOUSEMOTION:
                x, y = evento.pos
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = evento.pos
                for i, (pos_x, pos_y, width, height) in enumerate(posiciones_y):
                    if pos_x <= x <= pos_x + width and pos_y <= y <= pos_y + height:
                        indice_seleccionado = i
                        if indice_seleccionado == 0:
                            print("Iniciar Juego seleccionado")
                            pygame.mixer.music.stop() 
                            inicio_juego()
                            pygame.mixer.music.play(-1)
                            # Aquí se podría llamar a la función para iniciar el juego
                        elif indice_seleccionado == 1:
                            mostrar_puntajes(pantalla,fuente_puntaje_boton)
                            print("Top 10 Puntajes seleccionado")
                            # Mostrar el TOP 10 de puntajes
                        elif indice_seleccionado == 2:
                            mostrar_ajustes(pantalla)
                            print("Ajustes seleccionado")
                            # Mostrar la pantalla de ajustes
                        elif indice_seleccionado == 3:
                            corriendo = False
        dibujar_menu(pantalla)
        reloj.tick(30)
    pygame.mixer.music.stop()  # Detener la música al salir del juego
    pygame.quit()
    sys.exit()




#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def inicio_juego():
    """Esta funcion da inicio al juego bliteando las imagenes con los botones y toda la logica para el juego, 
    una vez finalizado el juego y guardado y mostrado los 10 mejores puntos vuelve al menu principal
    """
    lista_preguntas = parse_csv('data/preguntas.csv')
    if not lista_preguntas:
        return
    random.shuffle(lista_preguntas)
    pantalla = pygame.display.set_mode(PANTALLA_TAMAÑO)
    icono = pygame.image.load("image/WhatsApp Image 2024-06-20 at 21.59.16.jpeg")
    pygame.display.set_caption("Juego preguntados")
    pygame.display.set_icon(icono)
    pygame.mixer.init()
    
    sonido_error = pygame.mixer.Sound("sound/error_fallo.mp3")

    sonido = pygame.mixer.Sound("sound/tic_tac.mp3")

    imagen_opcion_a = pygame.image.load("image/opcionA.jpeg")
    imagen_opcion_a_transformada = pygame.transform.scale(imagen_opcion_a, (300, 100))
    imagen_opcion_b = pygame.image.load("image/opcionB.jpeg")
    imagen_opcion_b_transformada = pygame.transform.scale(imagen_opcion_b, (305, 100))
    imagen_opcion_c = pygame.image.load("image/opcionC.jpeg")
    imagen_opcion_c_transformada = pygame.transform.scale(imagen_opcion_c, (300, 90))
    imagen_pregunta = pygame.image.load("image/pregunta.png")
    imagen_pregunta_tranformada = pygame.transform.scale(imagen_pregunta, (500, 300))

    fuente_puntaje = pygame.font.SysFont("Arial",20)
    fuente_texto = pygame.font.SysFont("Arial", 30)
    fuente_respuesta = pygame.font.SysFont("Arial", 20)
    fuente_segundero = pygame.font.SysFont("Arial", 40)

    evento_tiempo = pygame.USEREVENT
    pygame.time.set_timer(evento_tiempo, 1000)
    segundero = 15
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
                sonido.stop()
            elif evento.type == pygame.MOUSEMOTION:
                x, y = evento.pos
            if evento.type == evento_tiempo:
                segundero -= 1
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if button_A.collidepoint(evento.pos):
                    if lista_preguntas[pregunta_actual]["respuesta_correcta"] == "a":
                        actualizar_estadisticas(lista_preguntas[pregunta_actual],True)
                        pregunta_actual += 1
                        puntos += 50
                        segundero = 15
                        sonido.stop()
                        sonido.play()
                    
                    else:
                        puntos -= 50
                        actualizar_estadisticas(lista_preguntas[pregunta_actual], False)
                        intentos -= 1
                        sonido_error.play()
                    
                elif button_B.collidepoint(evento.pos):
                    if lista_preguntas[pregunta_actual]["respuesta_correcta"] == "b":
                        actualizar_estadisticas(lista_preguntas[pregunta_actual],True)
                        pregunta_actual += 1
                        puntos += 50
                        segundero = 15
                        sonido.stop()
                        sonido.play()

                    else:
                        puntos -= 50
                        actualizar_estadisticas(lista_preguntas[pregunta_actual], False)
                        intentos -= 1
                        sonido_error.play()
                    
                elif button_C.collidepoint(evento.pos):
                    if lista_preguntas[pregunta_actual]["respuesta_correcta"] == "c":
                        actualizar_estadisticas(lista_preguntas[pregunta_actual],True)
                        pregunta_actual += 1
                        puntos += 50
                        segundero = 15
                        sonido.stop()
                        sonido.play()
                    
                    else:
                        puntos -= 50
                        actualizar_estadisticas(lista_preguntas[pregunta_actual], False)
                        intentos -= 1
                        sonido_error.play()

            if segundero == 0:
                    actualizar_estadisticas(lista_preguntas[pregunta_actual], False)
                    pregunta_actual += 1
                    segundero = 15
                    intentos -= 1
                    puntos -= 50
                    sonido_error.play()
                    sonido.stop()
                    sonido.play()
        pantalla.fill(NEGRO)
        texto_segundero = fuente_segundero.render(str(segundero), False, BLANCO)
        texto_puntos = fuente_texto.render(f"Puntos: {puntos}", False, BLANCO)
        texto_intentos = fuente_texto.render(f"Intentos: {intentos}", False, BLANCO)
        pantalla.blit(imagen_pregunta_tranformada, (50, 350))
        pantalla.blit(imagen_opcion_a_transformada, (120, 630))
        pantalla.blit(imagen_opcion_b_transformada, (120, 730))
        pantalla.blit(imagen_opcion_c_transformada, (120, 830))
        pantalla.blit(icono, (0, 0))
        pantalla.blit(texto_segundero, (35, 340))
        pantalla.blit(texto_puntos, (430, 880))
        pantalla.blit(texto_intentos, (430, 910))
        
        if intentos == 0 or pregunta_actual >= len(lista_preguntas) :
            pregunta_actual = 0
            sonido.stop()  # Detener la música
            nombre = pedir_nombre(pantalla, fuente_puntaje)
            guardar_estadisticas("data\preguntas.csv",lista_preguntas)
            guardar_puntajes(nombre, puntos)
            mostrar_puntajes(pantalla, fuente_puntaje)
            flag_run = False

        pregunta = lista_preguntas[pregunta_actual]["pregunta"]
        respuesta_a = lista_preguntas[pregunta_actual]["respuesta_a"]
        respuesta_b = lista_preguntas[pregunta_actual]["respuesta_b"]
        respuesta_c = lista_preguntas[pregunta_actual]["respuesta_c"]
        carta_pregunta = pygame.Surface(TAMAÑO_PREGUNTA)
        blit_text(carta_pregunta, pregunta, (10, 10), fuente_texto, BLANCO)
        pantalla.blit(carta_pregunta, (105, 420))
        blit_text(pantalla, respuesta_a, (button_A.x + 10, button_A.y + 20), fuente_respuesta, BLANCO)
        blit_text(pantalla, respuesta_b, (button_B.x + 10, button_B.y + 20), fuente_respuesta, BLANCO)
        blit_text(pantalla, respuesta_c, (button_C.x + 10, button_C.y + 20), fuente_respuesta, BLANCO)

        pygame.display.update()



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


