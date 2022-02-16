# imports
import csv
from tkinter import *
from tkinter import messagebox as mss
import time

# --- window
ventana = Tk() # instanciar
ventana.geometry("400x300") # alterar el tamanio
ventana.title("Mi programa") # editar el titulo
ventana.config(bg="#C1B9B9") # editar el background
ventana.iconbitmap("icon.ico") # editar el icono de la aplicacion

# ---- database
database = ["user,password".split(','),
         "Shiavo,8917929aa".split(','),
         "Cañedo,Ailab".split(','),
         "Popa,7823a1".split(','),
         "Pepe,af3541a".split(','),
         "Juan,78272sa".split(','),
         "Carlos,fsdfadsf".split(','),
         "Francisco,fdfs".split(','),
         "José,fsfsaf".split(','),
         "Emelio,5454s".split(','),
         "Mikey,asak1".split(','),
         "Erich,898912".split(',')]


# ---- functions
def csv_writer(data, path="./example"):
    with open(path, "w") as fil:
        writer = csv.writer(fil)
        writer.writerows(database)
    print("File stored with success")

def csv_reader(path="./example.csv"):
    loadedData = []
    with open(path, 'r') as file:
        reader = csv.reader(file, delimiter=",", quotechar=",", quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            loadedData.append(row)
    return loadedData

def Val():
    T1 = E1.get() # obtiene los caracteres del E1
    T2 = E2.get()
    try:
        x = T1
        y = T2
        flag = False
        for row in loadedData:
            if(len(row) > 0):
                if(row[0] == x):
                    print('user found')
                    flag = True
                    if(row[1] == y):
                        ventana.config(bg="#1CA5D6") # editar el background
                        L1.config(bg="#1CA5D6")
                        L2.config(bg="#1CA5D6")
                        mss.showinfo(message="Bienvenido "+ x , title="Bienvenida")
                    else:
                        ventana.config(bg="#D61C1F") # editar el background
                        L1.config(bg="#D61C1F")
                        L2.config(bg="#D61C1F")
                        mss.showwarning(message="Contraseña incorrecta", title="Error")
        if flag == False:
            ventana.config(bg="#D61C1F") # editar el background
            L1.config(bg="#D61C1F")
            L2.config(bg="#D61C1F")
            mss.showerror(message="Usuario no encontrado", title="Error")
    except:
        print("Valor incorrecto")
        print("Se presiono el boton")
        mss.showerror(message="dato incorrecto", title="error")

def funcion_reset():
    ventana.config(bg="#C1B9B9") # editar el background
    L1.config(bg="#C1B9B9")
    L2.config(bg="#C1B9B9")
    E1.delete(0, END) # limpiar el text box
    E2.delete(0, END)

# ---- Entry data
csv_writer(database, path="fakeBd.csv")
loadedData = csv_reader(path="fakeBd.csv")

# text box
E1 = Entry(ventana)
E1.place(x=10, y=25)

# label
L1 = Label(ventana, text="Ingresa tu usuario: ")
L1.place(x=10, y=2)
L1.config(bg="#C1B9B9")

# text box
E2 = Entry(ventana)
E2.place(x=150, y=25)

# label
L2 = Label(ventana, text="Ingresa tu contraseña: ")
L2.place(x=150, y=2)
L2.config(bg="#C1B9B9")

# button
B1 = Button(ventana, text="Validar", command=Val)
B1.place(x=10,y=50)

# button
B2 = Button(ventana, text="reset", command=funcion_reset)
B2.place(x=10,y=100)


ventana.mainloop()
