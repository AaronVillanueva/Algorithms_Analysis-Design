print("Inserta arbol")
x=[11,6,8,19,4,10,5,17,43,49,31]
util="     "
class Nodo:
    def __init__(self,numero,nivel):
        self.menor=None
        self.mayor=None
        self.numero=numero
        self.nivel=nivel

    def agregar(self,nuevo):
        if (self.numero<nuevo and self.mayor==None):
            self.mayor=Nodo(nuevo,self.nivel+1)
        if (self.numero>nuevo and self.menor==None):
            self.menor=Nodo(nuevo,self.nivel+1)
        if(self.numero<nuevo and self.mayor!=None):
            self.mayor.agregar(nuevo)
        if (self.numero > nuevo and self.menor != None):
            self.menor.agregar(nuevo)

    def printHorizontal(self):
        print(("   "*self.nivel)+str(self.numero))
        if(self.menor!=None):
            self.menor.printHorizontal()
        if (self.mayor != None):
            self.mayor.printHorizontal()
    def printVertical(self):


arbol=Nodo(x[0],0)
x.pop(0)
for i in x:
    arbol.agregar(i)
arbol.printHorizontal()
