from turtle import * 
import random
# crear ventana 
ventana = Screen()
ventana.bgcolor("blue")
ventana.title("Mi primer Juego")

# Primer contrincante aparecer el puntero
def tortuga():
    puntero = Turtle("turtle")
    puntero.color("green")
    puntero.penup()
    xdato= random.choice([20, -100, 200, 50, 60, -50, -200 ])
    ydato=random.choice([20, -100, 200, 50, 60, -50, -200 ])
    puntero.goto(xdato, ydato)

    # necesito movimientos de la tortuga 
    def arriba():
        puntero.setheading(90)
        puntero.forward(50)
    def abajo():
        puntero.setheading(270)
        puntero.forward(50)
    def derecha():
        puntero.setheading(0)
        puntero.forward(50)
    def izquierda():
        puntero.setheading(180)
        puntero.forward(50)

    # escuchar a los teclados 
    listen()
    onkeypress(arriba, "Up")
    onkeypress(abajo, "Down")
    onkeypress(izquierda, "Left")
    onkeypress(derecha, "Right")

# Contrincante
def contrincante():
    puntero = Turtle("turtle")
    puntero.color("yellow")
    puntero.penup()
    xdato= random.choice([90, -100, 20, 50, 60, -50, -200 ])
    ydato=random.choice([40, -100, 300, -50, 60, -80, -200 ])
    puntero.goto(xdato, ydato)

    # necesito movimientos de la tortuga 
    def arriba():
        puntero.setheading(90)
        puntero.forward(50)
    def abajo():
        puntero.setheading(270)
        puntero.forward(50)
    def derecha():
        puntero.setheading(0)
        puntero.forward(50)
    def izquierda():
        puntero.setheading(180)
        puntero.forward(50)

    # escuchar a los teclados 
    listen()
    onkeypress(arriba, "w")
    onkeypress(abajo, "s")
    onkeypress(izquierda, "a")
    onkeypress(derecha, "d")

contrincante()
tortuga()
# para no cerrar la ventana 
done()