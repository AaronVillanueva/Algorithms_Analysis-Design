#Autor Jaime Aaron
def radix(lista,index):
  lista0=[]
  lista1=[]
  lista2=[]
  lista3=[]
  lista4=[]
  lista5=[]
  lista6=[]
  lista7=[]
  lista8=[]
  lista9=[]
  for i in lista:
    dig=digito(i,index)
    if(dig==0):
      lista0.append(dig)
    if(dig==1):
      lista1.append(dig)
    if(dig==2):
      lista2.append(dig)
    if(dig==3):
      lista3.append(dig)
    if(dig==4):
      lista4.append(dig)
    if(dig==5):
      lista5.append(dig)
    if(dig==6):
      lista6.append(dig)
    if(dig==7):
      lista7.append(dig)
    if(dig==8):
      lista8.append(dig)
    if(dig==9):
      lista9.append(dig)

  lista=lista0+lista1+lista2+lista3+lista4+lista5+lista6+lista7+lista8+lista9
  radix(lista,index+1)



def digito(numero,digito):
  for i in range(digito):
    numero=numero//10
  return numero
