# Proyecto_Preguntados
Etermax, una franquicia de entretenimiento de plataformas y una de las marcas más exitosas de la división de Gaming, ha decidido desarrollar su famoso juego de preguntas y respuestas "Preguntados" en Python. Han contactado a los alumnos de la UTN para realizar este desarrollo.

Requerimientos para la APROBACION:

1. INICIO DEL JUEGO:
   - Al presionar el boton 'Iniciar' en el menu, se debera mostrar una pregunta aleatoria de las que se encuentran en el archivo preguntas.cvs.
   - El usuario tendra tres posibles opciones de respuesta.
   - Si responde correctamente, pasara a la siguiente pregunta.
   - Si responde incorrectamente, perdera una de sus tres oportunidades.
2. FIN DE LA PARTIDA:
   - Cuando el jugador pierda todas sus posibilidades, se debera pedir su nombre.
   - El nombre, junto con su puntaje y la fecha actual, se guardaran en el archivo partidas.json.
3. TOP 10 PARTIDAS:
   - Se debe poder acceder al TOP 10 de partidas con mayores puntajes desde el juego, mostrando los datos de quien realizo cada partida.

TODAS LAS PANTALLAS DEL JUEGO DEBEN CONTAR CON AL MENOS UNA IMAGEN.

INTEGRACION PARA LA PROMOCION:
Se requiere agregar musica, sonidos, y al menos dos de las siguientes integraciones.
1. CONFIGURACION DEL JUEGO:
   - Agregar un boton en el menu principal que permita acceder a la configuracion.
   - En la configuracion, se podra activar o desactivar la musica, ademas de ajustar su volumen.
2. SISTEMA DE TIEMPO:
   - Agregar un sistema de tiempo al juego.
   - Si se acaba el tiempo establecido, la partida se terminara automaticamente.
3. ESTADISTICAS DE PREGUNTAS:
   Agregar en el archivo preguntas.cvs los siguientes datos para cada pregunta:
   - Porcentaje de aciertos.
   - Cantidad de fallos.
   - Cantidad de aciertos.
   - Cantidad de veces preguntada.
4. AGREGAR PREGUNTAS:
   - Agregar un boton en el menu principal que permita agregar preguntas al juego.
   - Las preguntas pueden agregarse de manera individual o indicando el PATH de otro archivo CSV que contega los datos a agregar.
5. MODIFICAR OPCIONES DE JUEGO:
   - Agregar un boton en el menu principal que permita modificar opciones de juego.
   - Las opciones modificables deben de ser la cantidad de puntos por pregunta, la cantidad de oportunidades, la cantidad de respuestas posibles (nunca mayor a la cantidad maxima de respuestas) y, en caso 
     de que haya, el tiempo disponible.
   
