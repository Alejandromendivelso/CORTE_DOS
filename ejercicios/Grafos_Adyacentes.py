import math 

class Grafo:
    def __init__(self):
        self.vertice = []
        self.matriz =[[None]*0 for i in range(0)]
   
    def esta_vrectices(self, v):
        if self.vertice.count(v) == 0:
            return False
        return True
    
    def Agregar(self, v):
        if self.esta_vrectices(v):
            return False
        self.vertice.append(v)

        Filas = columnas = len(self.matriz)
        matriz_aux = [[None]*(Filas+1) for i in range(columnas+1)]

        for f in range(Filas):
            for c in range(columnas):
                matriz_aux[f][c] = self.matriz[f][c]
        self.matriz = matriz_aux
        return True

    def Agregar_arista(self, inicio, fin, valor, dirigida):
        if not (self.esta_vrectices(inicio)) or not(self.esta_vrectices(fin)):
            return False
        self.matriz[(self.vertice.index(inicio))][(self.vertice.index(fin))] = valor

        if not dirigida:
            self.matriz[(self.vertice.index(fin))][(self.vertice.index(inicio))] = valor
        return True
    
    def Imprimir (self, i):
        cadena = "\n"

        for c in range(len(i)):
            cadena += "\t" + str(self.vertice[c])
        cadena +="  \n" + ("  -" * len(i)) 

        for f in range(len (i)):
            cadena += "\n" +str(self.vertice[f]) + " |"

            for c in range(len(i)):
                if f == c and (i[f][c] is None or i[f][c] == 0 ):
                    cadena += "\t" + "\\"
                else:
                    if i[f][c] is None:
                        cadena += "\t" + "x"
                    elif math.isinf(i[f][c]):
                        cadena += "\t" + "∞"
                    else:
                        cadena += "\t" + str(i[f][c])

        cadena += "\n"
        print(cadena) 


if __name__== '_main_':
    g = Grafo()

    g.Agregar("A")
    g.Agregar("B")
    g.Agregar("C")
    g.Agregar("D")
    g.Agregar("E")      
    g.Agregar("F")
    g.Agregar("G")

    g.Agregar_arista("A","B",5,True)
    g.Agregar_arista("A","D",4,True)
    g.Agregar_arista("A","E",2,True)
    g.Agregar_arista("B","C",1,False)
    g.Agregar_arista("B","E",1,True)
    g.Agregar_arista("C","D",3,False)
    g.Agregar_arista("C","F",5,True)
    g.Agregar_arista("D","E",3,True)
    g.Agregar_arista("D","F",4,True)
    g.Agregar_arista("E","F",8,True)

    g.Imprimir(g.matriz) 
    print("Esta es la matriz de adyacencia ")