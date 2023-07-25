# comandos de turtle
```py
import turtle

# Crear un objeto Turtle
t = turtle.Turtle()

# Comandos de movimiento:
t.forward(distance)       # Mueve la tortuga hacia adelante la distancia especificada.
t.backward(distance)      # Mueve la tortuga hacia atrás la distancia especificada.
t.right(angle)            # Gira la tortuga hacia la derecha el ángulo especificado (en grados).
t.left(angle)             # Gira la tortuga hacia la izquierda el ángulo especificado (en grados).
t.circle(radius)          # Dibuja un círculo con el radio especificado.
t.goto(x, y)              # Mueve la tortuga a las coordenadas (x, y) sin dibujar una línea.
t.setx(x)                 # Establece la coordenada x de la posición de la tortuga.
t.sety(y)                 # Establece la coordenada y de la posición de la tortuga.
t.setheading(angle)       # Establece la dirección (ángulo) en la que mira la tortuga.
t.home()                 # Mueve la tortuga a su posición de inicio (0, 0) y establece su dirección a hacia arriba.

# Comandos de lápiz (pluma):
t.penup()                 # Levanta el lápiz, permitiendo que la tortuga se mueva sin dibujar.
t.pendown()               # Baja el lápiz, haciendo que la tortuga dibuje mientras se mueve.
t.pensize(width)          # Establece el ancho del lápiz de la tortuga.
t.pencolor(color)         # Establece el color del lápiz de la tortuga (por ejemplo, "red", "blue", "#FF0000", etc.).
t.fillcolor(color)        # Establece el color de relleno para formas llenadas.
t.begin_fill()            # Marca el comienzo del área de relleno.
t.end_fill()              # Marca el final del área de relleno y rellena la forma.
t.isdown()                # Devuelve True si el lápiz está abajo (dibujando), False si está levantado.

# Comandos de apariencia:
t.shape(shape)            # Cambia el ícono del puntero de la tortuga (opciones: "turtle", "classic", "arrow", etc.).
t.speed(speed)            # Establece la velocidad de la tortuga (1 es la más lenta, 10 es la más rápida).
t.resizemode(mode)        # Establece el modo de cambio de tamaño del puntero de la tortuga.
t.hideturtle()            # Oculta el puntero de la tortuga en la ventana.
t.showturtle()            # Muestra el puntero de la tortuga en la ventana.
t.turtlesize(stretch_wid=None, stretch_len=None, outline=None)  # Establece el tamaño del puntero de la tortuga.

# Comandos de color y relleno:
turtle.bgcolor(color)     # Establece el color de fondo de la ventana gráfica.
t.fillcolor(color)        # Establece el color de relleno para formas llenadas.
t.pencolor(color)         # Establece el color del lápiz de la tortuga.
t.color(color1, color2)   # Establece el color del lápiz y de relleno.
t.begin_fill()            # Marca el comienzo del área de relleno.
t.end_fill()              # Marca el final del área de relleno y rellena la forma.

# Comandos de control del dibujo:
turtle.title("Turtle Graphics")      # Establece el título de la ventana gráfica.
turtle.delay(delay)                 # Establece el retardo de animación en milisegundos.
turtle.tracer(n, delay=None)        # Controla la actualización de la ventana gráfica.
turtle.clear()                      # Borra todo el dibujo en la ventana.
turtle.clearscreen()                # Borra todo el dibujo y reinicia la ventana gráfica.
turtle.reset()                      # Borra todo y restablece la tortuga a su posición inicial.
turtle.undo()                       # Deshace el último comando de la tortuga.
turtle.isdown()                     # Devuelve True si el lápiz de la tortuga está abajo, False si está levantado.
turtle.isvisible()                  # Devuelve True si el puntero de la tortuga es visible, False si está oculto.
turtle.setworldcoordinates(llx, lly, urx, ury)  # Establece las coordenadas del sistema de coordenadas de la ventana.

# Eventos y control:
turtle.mainloop()                   # Mantiene la ventana gráfica abierta hasta que se cierre manualmente.
turtle.done()                       # Finaliza la ventana gráfica y espera hasta que se cierre.
turtle.bye()                        # Cierra la ventana gráfica y termina la aplicación.

turtle.listen()                     # Escucha eventos de teclado.
turtle.onkeypress(fun, key=None)    # Asigna una función para un evento de teclado específico.
turtle.onkeyrelease(fun, key=None)  # Asigna una función para un evento de teclado específico al soltar la tecla.
turtle.onclick(fun, btn=1, add=False)  # Asigna una función para el evento de clic del ratón.
turtle.ondrag(fun, btn=1, add=False)   # Asigna una función para el evento de arrastrar el ratón.
turtle.onrelease(fun, btn=1, add=False)  # Asigna una función para el evento de soltar el botón del ratón.

# Otros comandos:
turtle.screensize(canvwidth=None, canvheight=None, bg=None)  # Establece el tamaño de la pantalla de dibujo.
turtle.window_width()               # Devuelve el ancho de la ventana gráfica en píxeles.
turtle.window_height()              # Devuelve el alto de la ventana gráfica en píxeles.
turtle.setup(width, height, startx=None, starty=None)  # Configura el tamaño y posición de la ventana gráfica.
turtle.getscreen()                  # Devuelve la instancia de la ventana gráfica (Screen).
turtle.getturtle()                  # Devuelve la instancia de la tortuga actual (Turtle).

# Métodos de la clase Screen:
screen = turtle.Screen()
screen.title("Turtle Graphics")     # Establece el título de la ventana gráfica.
screen.bgcolor("lightblue")         # Establece el color de fondo de la ventana gráfica.
screen.setup(width=800, height=600) # Tamaño de la ventana en píxeles.
screen.screensize(800, 600)         # Tamaño del área de dibujo en píxeles.
screen.tracer(2, 0)                 # Controla la actualización de la ventana gráfica.
screen.delay(0)                     # Establece el retardo de animación en milisegundos.
screen.mainloop()                   # Mantiene la ventana gráfica abierta hasta que se cierre manualmente.

```