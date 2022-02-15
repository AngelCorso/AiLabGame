from tkinter import messagebox as ms

#showinfo()
#showwarning()
#showerror()

#askquestion()
#askyesno()
#askokcancel()
#askoknocancel()

#\n salto de linea
#messagebox.showinfo(message="Esto es una\nprueba de información",title="ventana")
#messagebox.showerror(message="Esto es una\nprueba de información",title="ventana")
#messagebox.showwarning(message="Esto es una\nprueba de información",title="ventana")

valor=ms.askokcancel(message="Desea continuar",title="Pregunta")
print(valor)
#if valor==True:

valor=ms.askyesno(message="Desea continuar",title="Pregunta")
print(valor)
#if valor==True:

#Realizar un programa que valide si en un archivo csv
#existe un usuario llamado "Cañedo"
#y la contraseña "Ailab"

#En caso de existir, enviar mensaje con showinfo("Bienvenido")
#Si se introducen los valores errones, indicar con un showerror
#datos incorrectos

#generar una base de datos con dos columnsa que sean
#usuario y contraseña
#Poner al menos 3 usuarios con su respectiva contraseña
#y en otro programa pedir nombre y contraseña


