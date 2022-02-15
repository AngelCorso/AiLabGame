import csv

datos=[["Clase","Altura","Peso","No de pie"]]

Ingresar = input("Desea ingresar datos? Y / N ")
while (Ingresar == "Y"):
    x=[]
    Clase = input("Ingresa H o M ")
    Altura = input("Ingresa altura en cm ")
    Peso = input("Ingresa el peso en Kg ")
    No_pie = input("Ingresa el No de calzado ")
    if ((len(Clase) >0) and (len(Altura)>0) and (len(Peso)>0) and (len(No_pie)>0)):
        x.append(Clase)
        x.append(Altura)
        x.append(Peso)
        x.append(No_pie)
        datos.append(x)
    else:
        print("Datos incorrectos")
    Ingresar = input("Desea ingresar datos? Y /N ")
                             
archivo=open("db.csv","w")
with archivo:
    escritor=csv.writer(archivo)
    escritor.writerows(datos)

print("Escritura exitosa")
