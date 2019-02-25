import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfile
from tkinter.ttk import Progressbar
import tkinter.scrolledtext as tkText

import os
from pip._internal import main as pipmain

import pip

def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])

def matriz(carga):
    tamaño=len(arrayA)
    carga.step(0)
    arrayC=[
       [0 for i in range(tamaño)]
       for j in range(tamaño)]
    carga.step(10)
    contador=0
    for i in range(tamaño):
        carga.step(89/tamaño)
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
    ventana = tk.Toplevel(pantalla)
    carga = tk.ttk.Progressbar(ventana,maximum=100)
    textoA=tkText.ScrolledText(ventana)
    textoB=tkText.ScrolledText(ventana)
    textoA.grid(column=0,row=1)
    textoB.grid(column=2,row=1)
    carga.grid(column=1, row=0)
    res = matriz(carga)
    carga.step(100)
    textoA.insert(INSERT,res)

def stras():
    print("ree")

def nuclear():
    print("reee")
    install(numpy)

pantalla=tk.Tk()
pantalla.title("Matrix Multiplication")



bA=tk.Button(pantalla,text="Archivo A",command=archivoA)
bB=tk.Button(pantalla,text="Archivo B",command=archivoB)
bC=tk.Button(pantalla,text="Listo",command=iniciar)
bNuclear=tk.Button(pantalla,text="Nuclear Numpy",command=nuclear)
txtA=tkText.ScrolledText(pantalla)
txtB=tkText.ScrolledText(pantalla)

bA.grid(column=0,row=0,padx=5,pady=15)
bB.grid(column=3,row=0,padx=5,pady=5)
bC.grid(column=1,row=2,padx=5,pady=5)
bNuclear.grid(column=1,row=3,padx=5,pady=5)
txtA.grid(column=0,row=1,padx=5,pady=5)
txtB.grid(column=3,row=1,padx=5,pady=5)

#entradaA= open(bA.)
#txtA.insert(INSERT,entradaA)
pantalla.mainloop()
