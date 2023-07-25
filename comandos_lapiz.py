import turtle as tu 

t = tu.Turtle("turtle")

t.forward(90)
t.penup() #levantar lapiz
t.goto(50, 40)
t.forward(80)
# bajar el lapiz 
t.pendown()
t.forward(20)
# el ancho del lapiz 
t.pensize(5)
t.right(45)
t.forward(50)
# el color del lapiz 
t.pencolor("blue")
t.left(90)
t.forward(90)
# para rellenar el lapiz
t.fillcolor("pink")
t.left(45)
t.forward(80)

# iniciar el comienzo de color de relleno
t.begin_fill()
t.forward(45)
# fin del color de relleno
t.end_fill()
t.forward(10)

t.isdown() # devuelve True si el lapiz esta dibujando y false si no esta dibujando 








tu.done()
