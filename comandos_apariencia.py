import turtle
turtle.bgcolor("yellow")
t = turtle.Turtle()

t.shape("square") # usar opciones para icono de la tortuga "turtle", "square", "arrow", etc 
t.speed(10) #velocidad en milisegundo
t.forward(80)
t.right(90)
t.forward(80)

t.resizemode("auto")
t.right(200)
t.forward(100)
t.resizemode("user")
t.turtlesize(2, 2) # aumenta el tamano del pincel 
t.forward(100)
t.resizemode("noresize")
t.turtlesize(1)  #Vuelve a su normalidad 
t.forward(100)

# ocultar el puntero 
t.hideturtle()
t.left(180)
t.forward(100)

# mostrar el puntero 
t.showturtle()
t.goto(10, 200)
t.forward(40)

# comandos de color y relleno 
turtle.bgcolor("blue")
t.pencolor("green")  # color del borde
t.fillcolor("pink") # color del relleno del lapiz

# control de dibujo 
turtle.title("Mi primer Juego ") # titulo a la ventana 
turtle.delay(20) #retardo de la animación 
t.backward(20)

# borrar todo el dibujo
turtle.clear()
turtle.clearscreen()






turtle.done()
