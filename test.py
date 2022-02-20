from tkinter import *
from PIL import ImageTk, Image
import time

vn = Tk()
vn.geometry("200x200")

#Abrimos imagen del directorio
#Dir= "C:\Users\eduar\Desktop\Practica"
Dir ="images/"
Im1 = Image.open(Dir + "aquarder.png")
Im2 = Image.open(Dir + "electder.png")
#Modificamos la imagen a un tamaño predeterminado
newsize = (100,100)
Im_1 = Im1.resize(newsize)
Im_2 = Im2.resize(newsize)

#Generar la imagen para Tk
im1 = ImageTk.PhotoImage(Im_1)
im2 = ImageTk.PhotoImage(Im_2)



def aceptar():
    pass
    #vn.destroy()
    #import Menu_2
    

def Ac():
    b1.config(image=im2)
    vn.update() #Tiene un tiempo muerto


b1=Button(vn, text="Aceptar",command=aceptar)
b1.pack()
b1.config(image=im1)


b2=Button(vn, text="Actualizar",command=Ac)
b2.pack()


vn.mainloop()