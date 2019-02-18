import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfile

def matriz():
    tamaño=len(arrayA)

    arrayC=[
       [0 for i in range(tamaño)]
       for j in range(tamaño)]
    contador=0
    for i in range(tamaño):
       for j in range(tamaño):
          for k in range(tamaño):
             contador+=1
             arrayC[i][j]+=arrayA[i][k]*arrayB[k][j]

    return (arrayC)

def crearMatriz(path):
    entrada = open(path)
    texto = entrada.readlines()
    array=[]
    for i in texto:
        fila = i.rstrip()
        fila = fila.split(",")
        fila = list(map(int, fila))
        array.append(fila)
    return array

def archivoA():
    path=askopenfile()
    path=((str(path).split("'")[1]))
    global arrayA
    arrayA=crearMatriz(path)
    txtA.insert(INSERT, arrayA)


def archivoB():
    path=askopenfile()
    path = ((str(path).split("'")[1]))
    global arrayB
    arrayB = crearMatriz(path)
    txtB.insert(INSERT, arrayB)


def iniciar():
    res=matriz()
    ventana=tk.Toplevel(pantalla)
    txtC=tk.Text(ventana)
    txtC.pack()
    txtC.insert(INSERT,res)



pantalla=tk.Tk()
pantalla.title("Matrix Multiplication")

bA=tk.Button(pantalla,text="Archivo A",command=archivoA)
bB=tk.Button(pantalla,text="Archivo B",command=archivoB)
bC=tk.Button(pantalla,text="Listo",command=iniciar)
txtA=tk.Text(pantalla)
txtB=tk.Text(pantalla)
bA.grid(column=0,row=0,padx=5,pady=15)
bB.grid(column=3,row=0,padx=5,pady=5)
bC.grid(column=2,row=2,padx=5,pady=5)
txtA.grid(column=0,row=1,padx=5,pady=5)
txtB.grid(column=3,row=1,padx=5,pady=5)

#entradaA= open(bA.)
#txtA.insert(INSERT,entradaA)
pantalla.mainloop()



