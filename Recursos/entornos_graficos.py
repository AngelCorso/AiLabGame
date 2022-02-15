# Practica de entornos graficos de python
# -------------------------------------------

# Kivy, qt, tkinter, pygame // principales librearias de entorno grafico
from tkinter import *
from tkinter import messagebox as mss   # para arrojar ventanas emergentes
import time

ventana = Tk() # instanciar
ventana.geometry("400x300") # alterar el tamanio
ventana.title("Mi programa") # editar el titulo
ventana.config(bg="#f5f5f5") # editar el background
#ventana.iconbitmap("icon.ico") # editar el icono de la aplicacion


# ---- funciones ----
def Val():
    resp = mss.askyesno(message="Desea continuar?", title="continuar")
    if resp == True:
        T = E1.get() # obtiene los caracteres del E1
        try:
            x = float(T)
            mss.showinfo(message="conversion realizada", title="info")
            print("Es un numero")
            time.sleep(1)
            E1.delete(0, END) # limpiar el text box
        except:
            mss.showerror(message="dato incorrecto", title="error")
            print("Valor incorrecto")
        
        print("Se presiono el boton")


# ---- entrada de datos ----

# E1.pack() # coloca en un lugar al azar
# E1.grid() # divide la ventana en reng. y colum.
# E1.place() # coloca el objeto segun x & y

# text box
E1 = Entry(ventana)
E1.place(x=10, y=25)

# label
L1 = Label(ventana, text="Ingresa tu nombre: ")
L1.place(x=10, y=2)
L1.config(bg="#f5f5f5")
L1 = Label(ventana, text="Goku")

# button
B1 = Button(ventana, text="Validar", command=Val)
B1.place(x=10,y=50)


ventana.mainloop()
