import turtle
# usando la clase Turtle
t = turtle.Turtle("turtle")
# comandos de movimiento
t.forward(60) #moverse adelante- pixeles
t.backward(20) #moverse atras- pixeles
t.right(90) #moverse a la derecha- angulos 
t.forward(70)
t.left(90) #moverse a la izquierda - angulos 
t.forward(50) 

# creando figuras 
t.circle(70) # el valor es para el radio de la circunferencia

# mover la tortuga a un punto especifico 
t.goto(100, 300) # valores para "X" y "Y" 

# establecer coordenadas 
t.setx(300)
t.sety(-60) 

# angulo a donde mirará la tortuga
t.setheading(180) # el valor en grados 
# para mover la tortuga a su posición inicial 
t.home()




# para mantener abierto la ventana
turtle.done()