class Mochila:
    def __init__(self, peso, capacidad):
        self.peso = peso
        self.capacidad = capacidad
         
     
    def meterObjeto(self, objeto):
        self.peso += objeto.peso
         
         
         
class Objeto:
    def __init__(self, peso, valor):
        self.peso = peso
        self.valor = valor
        self.valorporunidad = self.valor/self.peso
             
 
#algoritmo de ordenación por selección
def selectionsort(lista,tam):
        for i in range(0,tam-1):
            min=i
            for j in range(i+1,tam):
                if lista[min].valorporunidad > lista[j].valorporunidad:
                    min=j
            aux=lista[min]
            lista[min]=lista[i]
            lista[i]=aux
 
mochila = Mochila(0, 50)
 
objetos = []
objetos.append(Objeto(20, 3))
objetos.append(Objeto(50, 5))
objetos.append(Objeto(20, 8))
objetos.append(Objeto(10, 4))
objetos.append(Objeto(50, 1))
objetos.append(Objeto(60, 3))
objetos.append(Objeto(30, 5))
objetos.append(Objeto(70, 8))
objetos.append(Objeto(80, 1))
objetos.append(Objeto(15, 7))
 
 
selectionsort(objetos, len(objetos))
 
resultado = []
for i in range(len(objetos)):
    resultado.append(0)
 
 
i = len(objetos) - 1 #empezamos desde el final porque están ordenados de menor a mayor
while(mochila.peso < mochila.capacidad):
    objeto = objetos[i]
    if ((mochila.peso + objeto.peso) <= mochila.capacidad):
        resultado[i] = 1
        mochila.meterObjeto(objeto)
    else:
        resultado[i] = (mochila.capacidad - mochila.peso) / objeto.peso
        mochila.peso = mochila.capacidad
    i-=1
     
print ("Resultado: Fracciones de los objetos en la mochila: ")
for i in range(len(resultado)-1, -1, -1):
    print ("Objeto ", i, ": ", resultado[i])