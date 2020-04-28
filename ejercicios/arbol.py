import turtle

def Fractales(longitudRama,arbol):
    if longitudRama > 1:
        arbol.forward(longitudRama)
        arbol.right(20)
        Fractales(longitudRama-10,arbol)
        arbol.left(40)
        Fractales(longitudRama-10,arbol)
        arbol.right(20)
        arbol.backward(longitudRama)

def main():
    t = turtle.Turtle()
    miVentana = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("blue")
    Fractales(90,t)
    miVentana.exitonclick()

main()