import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfile
import tkinter.scrolledtext as tkText

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
    txtA.delete("1.0", END)
    path=((str(path).split("'")[1]))
    global arrayA
    arrayA=crearMatriz(path)
    for i in arrayA:
        #print(i)
        txtA.insert(INSERT, i)
        txtA.insert(INSERT,"\n")


def archivoB():
    path=askopenfile()
    txtB.delete("1.0",END)
    path = ((str(path).split("'")[1]))
    global arrayB
    arrayB = crearMatriz(path)
    for i in arrayB:
        #print(i)
        txtB.insert(INSERT, i)
        txtB.insert(INSERT, "\n")


def iniciar():
    res=matriz()
    ventana=tk.Toplevel(pantalla)
    txtC=tkText.ScrolledText(ventana)
    txtD=tkText.ScrolledText(ventana)
    txtC.grid(column=0,row=0)
    txtD.grid(column=1,row=0)
    txtC.insert(INSERT,res)



pantalla=tk.Tk()
pantalla.title("Matrix Multiplication")

bA=tk.Button(pantalla,text="Archivo A",command=archivoA)
bB=tk.Button(pantalla,text="Archivo B",command=archivoB)
bC=tk.Button(pantalla,text="Listo",command=iniciar)
txtA=tkText.ScrolledText(pantalla)
txtB=tkText.ScrolledText(pantalla)
bA.grid(column=0,row=0,padx=5,pady=15)
bB.grid(column=3,row=0,padx=5,pady=5)
bC.grid(column=2,row=2,padx=5,pady=5)
txtA.grid(column=0,row=1,padx=5,pady=5)
txtB.grid(column=3,row=1,padx=5,pady=5)

#entradaA= open(bA.)
#txtA.insert(INSERT,entradaA)
pantalla.mainloop()
