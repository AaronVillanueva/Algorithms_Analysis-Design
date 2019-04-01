import turtle as t
import math

class Nodo:
    def __init__(self,numero):
        self.numero=numero
        self.enlaces=[]
        self.visitado=False
        self.tipo="nada"
        self.x=None
        self.y=None

    def agregarNodo(self,nuevo):
        self.enlaces.append(nuevo)

    def agregarCoordenada(self,x,y):
        self.x=x
        self.y=y

    def enlacesAlista(self):
        lista=[]
        for i in self.enlaces:
            lista.append(Nodo(i).numero)
        return lista

    def getNumero(self):
        return self.numero

    def encontrarNodo(self,numeroEncuentra):
        if(self.numero==numeroEncuentra):
            return Nodo(self)

        else:
            listaObj=self.enlacesAlista()
            if(listaObj.count(numeroEncuentra)>0):
                index=0
                for i in listaObj:
                    if(i!=numeroEncuentra):
                        index+=1
                    else:
                        break
                nodoEncontrado=self.enlaces[index]
                return Nodo(nodoEncontrado)
            else:
                for i in self.enlaces:
                    Nodo(i).encontrarNodo(numeroEncuentra)

    def dibujar(self,t,tamaño,dist):
        t.penup()
        t.goto(self.x, self.y)
        t.pendown()
        t.pencolor="black"
        if(self.tipo=="nada"):
            t.fillcolor("white")
        elif(self.tipo=="activo"):
            t.fillcolor("green")
        elif(self.tipo=="visitado"):
            t.fillcolor("red")
        t.begin_fill()
        t.circle(tamaño)
        t.penup()
        
        tamEn=len(self.enlacesAlista())
        listaC=crearCoordenadas(tamEn,dist,self.x,self.y)
        if (tamEn > 0):
            for i in self.enlaces:
                nodo=Nodo(i)
                coordj = listaC.pop(0)
                nodo.agregarCoordenada(coordj[0], coordj[1])
                nodo.dibujar(t, tamaño, dist)



    def strLista(self):
        return self.enlaces

def leer(string):
    lista=string.split()
    for i in range(len(lista)):
        lista[i] = lista[i].replace("(", "")
        lista[i] = lista[i].replace(")", "")
        lista[i] = lista[i].split(",")

def dibujar():
    ventana=t.Screen()
    ventana.delay(10)
    d=t.Turtle()
    d.speed(10)
    #dibujaNodo(d,a10)
    arbol.dibujar(d,20,50)


    ventana.exitonclick()

def crearCoordenadas(num,dist,xi,yi):
    if(num!=0):
        lista=[]
        for i in range(num):
            angulo = math.radians(i * (360) / float(num))
            lista.append([dist*(xi+math.cos(angulo)),dist*(yi+math.sin(angulo))])

        return lista
    else:
        return False

def dibujaNodo(turtle,nodo):
    turtle.penup()
    turtle.goto(nodo.x,nodo.y)
    turtle.pendown()
    turtle.circle(10)


x=[11,6,8,19,4,10,5,17,43,49,31]

a=x.pop(0)
arbol=Nodo(a)
arbol.agregarCoordenada(0,0)
for i in x:
    arbol.agregarNodo(i)
a10=arbol.encontrarNodo(10)
a10.agregarNodo(5)
a10.agregarCoordenada(10,10)
dibujar()
print(a10.enlaces)
print(arbol.strLista())
