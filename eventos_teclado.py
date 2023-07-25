import turtle 
t = turtle.Turtle("turtle")

# escuchar al teclado 
turtle.listen()
# crear funciones para mover con el teclado 
def arriba():
    t.setheading(90) # mueve la dirección con el angulo hacia donde dirigirá
    t.forward(20)

def abajo():
    t.setheading(270)
    t.forward(20)
def derecha():
    t.setheading(0)
    t.forward(20)

def izquierda():
    t.setheading(180)
    t.forward(20)

# usando las funciones para el teclado 

turtle.onkeypress(arriba, "Up")
turtle.onkeypress(abajo, "Down")
turtle.onkeypress(derecha, "Right")
turtle.onkeypress(izquierda, "Left")


turtle.onkeypress(arriba, "w")
turtle.onkeypress(abajo, "s")
turtle.onkeypress(derecha, "d")
turtle.onkeypress(izquierda, "a")


turtle.done()