#Based on practica_funciones_grafico.py
# imports
import csv
from tkinter import *
from tkinter import messagebox as ms
import time
from functools import partial
import tkinter
from urllib.parse import _NetlocResultMixinBase
from PIL import Image, ImageTk
import os
from os.path import exists
from Class import *

#hacer funcion que elimine todas las ventanas abiertas, asi no estar checando el flujo, con trys y excepts

def SetupWindow(tkInstance,size,title,bgcolor,icon):
    tkInstance.geometry(size)
    tkInstance.title("Juego Loco 3mil8mil") # editar el titulo
    tkInstance.config(bg="#C1B9B9") # editar el background
    tkInstance.iconbitmap("VamohIcon.ico") # editar el icono de la aplicacion

def OpenLoginWindow():
    AccountsWindow.destroy()
    global LoginWindow
    LoginWindow = Tk() # instanciar
    LoginWindow.geometry("400x300") # alterar el tamanio
    LoginWindow.title("Juego Loco 3mil8mil") # editar el titulo
    LoginWindow.config(bg="#C1B9B9") # editar el background
    LoginWindow.iconbitmap("VamohIcon.ico") # editar el icono de la aplicacion

    # label
    GameTitle = Label(LoginWindow, text="Juego Loco 3mil8mil")
    GameTitle.place(relx=0.5,rely=0.1,anchor=CENTER)
    GameTitle.config(bg="#C1B9B9")

    # label
    UsernameLabel = Label(LoginWindow, text="Usuario")
    UsernameLabel.place(relx=0.5,rely=0.3,anchor=CENTER)
    UsernameLabel.config(bg="#C1B9B9")

    # text box
    UsernameTextBox = Entry(LoginWindow)
    UsernameTextBox.place(relx=0.5,rely=0.4,anchor=CENTER)

    # label
    PasswordLabel = Label(LoginWindow, text="Contraseña")
    PasswordLabel.place(relx=0.5,rely=0.6,anchor=CENTER)
    PasswordLabel.config(bg="#C1B9B9") 

    # text box
    PasswordTextBox = Entry(LoginWindow)
    PasswordTextBox.place(relx=0.5,rely=0.7,anchor=CENTER)

    # button
    StartButton = Button(LoginWindow, text="Iniciar", command=partial(LoginValidation,UsernameTextBox,PasswordTextBox))
    # StartButton = Button(LoginWindow, text="Iniciar", command=OpenGamemodeWindow)
    StartButton.place(relx=0.5,rely=0.9,anchor=CENTER)

    LoginWindow.mainloop()

def OpenRegisterWindow():
    try:
        LoginWindow.destroy()
    except:
        AccountsWindow.destroy()
    global RegisterWindow
    RegisterWindow = Tk() # instanciar
    RegisterWindow.geometry("400x300") # alterar el tamanio
    RegisterWindow.title("Juego Loco 3mil8mil") # editar el titulo
    RegisterWindow.config(bg="#C1B9B9") # editar el background
    RegisterWindow.iconbitmap("VamohIcon.ico") # editar el icono de la aplicacion

    # label
    GameTitle = Label(RegisterWindow, text="Juego Loco 3mil8mil")
    GameTitle.place(relx=0.5,rely=0.1,anchor=CENTER)
    GameTitle.config(bg="#C1B9B9")

    # label
    UsernameLabel = Label(RegisterWindow, text="Usuario")
    UsernameLabel.place(relx=0.5,rely=0.2,anchor=CENTER)
    UsernameLabel.config(bg="#C1B9B9")

    # text box
    UsernameTextBox = Entry(RegisterWindow)
    UsernameTextBox.place(relx=0.5,rely=0.3,anchor=CENTER)

    # label
    PasswordLabel = Label(RegisterWindow, text="Contraseña")
    PasswordLabel.place(relx=0.5,rely=0.4,anchor=CENTER)
    PasswordLabel.config(bg="#C1B9B9") 

    # text box
    PasswordTextBox = Entry(RegisterWindow)
    PasswordTextBox.place(relx=0.5,rely=0.5,anchor=CENTER)

    # label
    RePasswordLabel = Label(RegisterWindow, text="Confirmar contraseña")
    RePasswordLabel.place(relx=0.5,rely=0.6,anchor=CENTER)
    RePasswordLabel.config(bg="#C1B9B9") 

    # text box
    RePasswordTextBox = Entry(RegisterWindow)
    RePasswordTextBox.place(relx=0.5,rely=0.7,anchor=CENTER)

    # button
    # RegisterButton = Button(RegisterWindow, text="Registrar", command=RegisterValidation(UsernameTextBox,PasswordTextBox,RePasswordTextBox))
    RegisterButton = Button(RegisterWindow, text="Registrar", command=partial(RegisterValidation,UsernameTextBox,PasswordTextBox,RePasswordTextBox))
    RegisterButton.place(relx=0.5,rely=0.9,anchor=CENTER)

    RegisterWindow.mainloop()

def OpenGamemodeWindow():
    LoginWindow.destroy()
    global GamemodeWindow
    GamemodeWindow = Tk() # instanciar
    GamemodeWindow.geometry("400x300") # alterar el tamanio
    GamemodeWindow.title("Select mode") # editar el titulo
    GamemodeWindow.config(bg="#C1B9B9") # editar el background
    GamemodeWindow.iconbitmap("VamohIcon.ico") # editar el icono de la aplicacion

    # button
    TrainingButton = Button(GamemodeWindow, text="Modo entrenamiento", command=OpenCharacterSelectionWindow)
    TrainingButton.place(relx=0.5,rely=0.4,anchor=CENTER)

    # button
    HistoryButton = Button(GamemodeWindow, text="Modo historia", command=OpenLoginWindow)
    HistoryButton.place(relx=0.5,rely=0.6,anchor=CENTER)

def OpenDetailsWindow(character):
    
    
    global DetailsWindow
    # DetailsWindow = Tk() # instanciar
    DetailsWindow = Toplevel(CharacterSelectionWindow) # instanciar
    DetailsWindow.geometry("400x400") # alterar el tamanio
    DetailsWindow.title("Juego Loco 3mil8mil") # editar el titulo
    DetailsWindow.config(bg="#C1B9B9") # editar el background
    DetailsWindow.iconbitmap("VamohIcon.ico") # editar el icono de la aplicacion

    Im1 = Image.open(character.imagepath)
    newsize = (100,100)
    Im_1 = Im1.resize(newsize)
    im1 = ImageTk.PhotoImage(Im_1)

    #grid de 11x7
    attacksNames = list(character.attacks)
    attacks = character.attacks

    advantageText = "Ventaja con: " + ", ".join(character.advantage)
    disadvantageText = "Desventaja con: " + ", ".join(character.disadvantage)
    normalText = "Normal con: " + ", ".join(character.normal)

    Label(DetailsWindow,image=im1,bg="#C1B9B9").grid(row=0,column=0, columnspan = 7)
    Label(DetailsWindow,text=character.name + ": Tipo " + character.type,bg="#C1B9B9").grid(row=1,column=0, columnspan = 7)
    Label(DetailsWindow,text=advantageText,bg="#C1B9B9").grid(row=2,column=0, columnspan = 7)
    Label(DetailsWindow,text=disadvantageText,bg="#C1B9B9").grid(row=3,column=0, columnspan = 7)
    Label(DetailsWindow,text=normalText,bg="#C1B9B9").grid(row=4,column=0, columnspan = 7)

    Label(DetailsWindow,text="Habilidad",bg="#C1B9B9").grid(row=5,column=0,sticky=W)
    Label(DetailsWindow,text="norm",bg="#C1B9B9").grid(row=5,column=1,sticky=W)
    Label(DetailsWindow,text="At vent",bg="#C1B9B9").grid(row=5,column=2,sticky=W)
    Label(DetailsWindow,text="At desv",bg="#C1B9B9").grid(row=5,column=3,sticky=W)
    Label(DetailsWindow,text="pot norm",bg="#C1B9B9").grid(row=5,column=4,sticky=W)
    Label(DetailsWindow,text="pot vent",bg="#C1B9B9").grid(row=5,column=5,sticky=W)
    Label(DetailsWindow,text="pot desv",bg="#C1B9B9").grid(row=5,column=6,sticky=W)

    # Nombres de ataques
    Label(DetailsWindow,text=attacksNames[0],bg="#C1B9B9").grid(row=6,column=0,sticky=W)
    Label(DetailsWindow,text=attacksNames[1],bg="#C1B9B9").grid(row=7,column=0,sticky=W)
    Label(DetailsWindow,text=attacksNames[2],bg="#C1B9B9").grid(row=8,column=0,sticky=W)
    Label(DetailsWindow,text=attacksNames[3],bg="#C1B9B9").grid(row=9,column=0,sticky=W)

    #Daños de ataques
    Label(DetailsWindow,text=str(attacks[attacksNames[0]][0]) + "pt",bg="#C1B9B9").grid(row=6,column=1)
    Label(DetailsWindow,text=str(attacks[attacksNames[0]][1]) + "pt",bg="#C1B9B9").grid(row=6,column=2)
    Label(DetailsWindow,text=str(attacks[attacksNames[0]][2]) + "pt",bg="#C1B9B9").grid(row=6,column=3)
    Label(DetailsWindow,text=str(attacks[attacksNames[0]][3]) + "pt",bg="#C1B9B9").grid(row=6,column=4)
    Label(DetailsWindow,text=str(attacks[attacksNames[0]][4]) + "pt",bg="#C1B9B9").grid(row=6,column=5)
    Label(DetailsWindow,text=str(attacks[attacksNames[0]][5]) + "pt",bg="#C1B9B9").grid(row=6,column=6)

    Label(DetailsWindow,text=str(attacks[attacksNames[1]]) + "pt",bg="#C1B9B9").grid(row=7,column=1)
    Label(DetailsWindow,text=str(attacks[attacksNames[2]]) + "pt",bg="#C1B9B9").grid(row=8,column=1)

    Label(DetailsWindow,text="Potenciador de campo, 1 vez cada 3 turnos\n tiene una duración de 2 turnos",bg="#C1B9B9").grid(row=9,column=1, columnspan=6)
    
    DetailsWindow.mainloop()

def OpenHistorySelectionWindow():
    global DetailsWindow
    HistorySelectionWindow = Tk() # instanciar
    HistorySelectionWindow.geometry("400x300") # alterar el tamanio
    HistorySelectionWindow.title("Juego Loco 3mil8mil") # editar el titulo
    HistorySelectionWindow.config(bg="#C1B9B9") # editar el background
    HistorySelectionWindow.iconbitmap("VamohIcon.ico") # editar el icono de la aplicacion

def OpenTrainingSelectionWindow():
    global TrainingSelectionWindow
    TrainingSelectionWindow = Tk() # instanciar
    TrainingSelectionWindow.geometry("400x300") # alterar el tamanio
    TrainingSelectionWindow.title("Juego Loco 3mil8mil") # editar el titulo
    TrainingSelectionWindow.config(bg="#C1B9B9") # editar el background
    TrainingSelectionWindow.iconbitmap("VamohIcon.ico") # editar el icono de la aplicacion

def OpenCharacterSelectionWindow():
    try:
        GamemodeWindow.destroy()
    except:
        pass
    try:
        AccountsWindow.destroy()
    except:
        pass
    try:
        LoginWindow.destroy()
    except:
        pass
    global CharacterSelectionWindow
    CharacterSelectionWindow = Tk() # instanciar
    CharacterSelectionWindow.geometry("400x400") # alterar el tamanio
    CharacterSelectionWindow.title("Juego Loco 3mil8mil") # editar el titulo
    CharacterSelectionWindow.config(bg="#C1B9B9") # editar el background
    CharacterSelectionWindow.iconbitmap("VamohIcon.ico") # editar el icono de la aplicacion

    characters = initCharacters()

    Dir ="images/"
    Im1 = Image.open(Dir + "aquarder.png")
    Im2 = Image.open(Dir + "electder.png")
    Im3 = Image.open(Dir + "firesor.png")
    Im4 = Image.open(Dir + "mousebug.png")
    Im5 = Image.open(Dir + "splant.png")
    Im6 = Image.open(Dir + "rockdog.png")

    #Modificamos la imagen a un tamaño predeterminado
    newsize = (100,100)
    Im_1 = Im1.resize(newsize)
    Im_2 = Im2.resize(newsize)
    Im_3 = Im3.resize(newsize)
    Im_4 = Im4.resize(newsize)
    Im_5 = Im5.resize(newsize)
    Im_6 = Im6.resize(newsize)

    #Generar la imagen para Tk
    im1 = ImageTk.PhotoImage(Im_1)
    im2 = ImageTk.PhotoImage(Im_2)
    im3 = ImageTk.PhotoImage(Im_3)
    im4 = ImageTk.PhotoImage(Im_4)
    im5 = ImageTk.PhotoImage(Im_5)
    im6 = ImageTk.PhotoImage(Im_6)
    characterImages = [im1,im2,im3,im4,im5,im6]

    #podria hacer un arreglo de personajes, asi con dos for anidados inicializo cada una de todas estas cosas sin tener tanta linea
    #haciendo 6 fors me parece, en vez de 6 anidados en pares
    '''
    for i in range(0,4,3):
        for j in range(3):
            Label(CharacterSelectionWindow,text=characters[j].name,bg="#C1B9B9").grid(row=i,column=j)

    for i in range(1,5,3):
        for j in range(3):
            Button(CharacterSelectionWindow,image = characterImages[j],bg="#C1B9B9").grid(row=i,column=j)

    for i in range(2,6,3):
        for j in range(3):
            Button(CharacterSelectionWindow,text="Detalle",command=OpenDetailsWindow).grid(row=i,column=j)
    '''
    
    Character1Label = Label(CharacterSelectionWindow,text="Aquarder",bg="#C1B9B9").grid(row=0,column=0)
    Character2Label = Label(CharacterSelectionWindow,text="Electder",bg="#C1B9B9").grid(row=0,column=1)
    Character3Label = Label(CharacterSelectionWindow,text="Firesor",bg="#C1B9B9").grid(row=0,column=2)
    Character1Button = Button(CharacterSelectionWindow,image=im1,command=OpenLoginWindow).grid(row=1,column=0) #ipadx para acomodar tamaños
    Character2Button = Button(CharacterSelectionWindow,image=im2,command=OpenLoginWindow).grid(row=1,column=1)
    Character3Button = Button(CharacterSelectionWindow,image=im3,command=OpenLoginWindow).grid(row=1,column=2)
    Details1Button = Button(CharacterSelectionWindow,text="Detalle",command=partial(OpenDetailsWindow,characters[0])).grid(row=2,column=0)
    Details2Button = Button(CharacterSelectionWindow,text="Detalles",command=partial(OpenDetailsWindow,characters[1])).grid(row=2,column=1)
    Details3Button = Button(CharacterSelectionWindow,text="Detalle",command=partial(OpenDetailsWindow,characters[2])).grid(row=2,column=2)

    Character4Label = Label(CharacterSelectionWindow,text="Mousebug",bg="#C1B9B9").grid(row=3,column=0)
    Character5Label = Label(CharacterSelectionWindow,text="Splant",bg="#C1B9B9").grid(row=3,column=1)
    Character6Label = Label(CharacterSelectionWindow,text="Rockdog",bg="#C1B9B9").grid(row=3,column=2)
    Character4Button = Button(CharacterSelectionWindow,image=im4,command=OpenLoginWindow).grid(row=4,column=0) #ipadx para acomodar tamaños
    Character5Button = Button(CharacterSelectionWindow,image=im5,command=OpenLoginWindow).grid(row=4,column=1)
    Character6Button = Button(CharacterSelectionWindow,image=im6,command=OpenLoginWindow).grid(row=4,column=2)
    Details4Button = Button(CharacterSelectionWindow,text="Detalle",command=partial(OpenDetailsWindow,characters[3])).grid(row=5,column=0)
    Details5Button = Button(CharacterSelectionWindow,text="Detalle",command=partial(OpenDetailsWindow,characters[4])).grid(row=5,column=1)
    Details6Button = Button(CharacterSelectionWindow,text="Detalle",command=partial(OpenDetailsWindow,characters[5])).grid(row=5,column=2)

    StartButton = Button(CharacterSelectionWindow,text="Iniciar",command=OpenFightWindow).grid(row=6,column=1)

    # Character1Label = Label(CharacterSelectionWindow,text="buenas").pack(side = TOP, pady = 0.5)
    # Character1Button = Button(CharacterSelectionWindow,text="buenas").pack(side = TOP, pady = 0.5)
    # Character1Button.place(relx=0.5,rely=0.6,anchor=CENTER)
    CharacterSelectionWindow.mainloop()

def OpenFightWindow():
    CharacterSelectionWindow.destroy()
    global FightWindow
    FightWindow = Tk() # instanciar
    FightWindow.geometry("400x300") # alterar el tamanio
    FightWindow.title("Juego Loco 3mil8mil") # editar el titulo
    FightWindow.config(bg="#C1B9B9") # editar el background
    FightWindow.iconbitmap("VamohIcon.ico") # editar el icono de la aplicacion

    Attack1Button = Button(FightWindow,text="Ataque1",command=OpenLoginWindow).grid(row=0,column=0,ipadx=20)
    Attack2Button = Button(FightWindow,text="Ataque2",command=OpenLoginWindow).grid(row=1,column=0)
    Attack3Button = Button(FightWindow,text="Ataque3",command=OpenLoginWindow).grid(row=2,column=0)
    Attack3Button = Button(FightWindow,text="Potenciador",command=OpenLoginWindow).grid(row=3,column=0)
    # Attack4Button = Button(CharacterSelectionWindow,text="Detalle",command=OpenLoginWindow).grid(row=5,column=2)

def RegisterValidation(UsernameTextBox,PasswordTextBox,RePasswordTextBox):
    username = UsernameTextBox.get()
    password = PasswordTextBox.get()
    rePassword = RePasswordTextBox.get()
    usernamePath = username + ".csv"

    # Si ya existe el usuario
    if exists(usernamePath):
        ms.showinfo(message="Ese nombre de usuario ya está registrado, prueba con otro",title="Usuario ya existente")
        return

    if username == "" or password == "" or rePassword == "":
        ms.showwarning(message="Completa todos los campos",title="Campos requeridos")
        return
     
    if password != rePassword:
        ms.showinfo(message="Las contraseñas no coinciden",title="Contraseña inválida")
        return

    datos=[["Contraseña","Personaje","Nivel","HP", "HP enemigo", "Turno"]]
    dbName = UsernameTextBox.get() + ".csv"
    datos.append([PasswordTextBox.get(),0,0,0,0,False])
    archivo=open(dbName,"w")
    with archivo:
        escritor=csv.writer(archivo)
        escritor.writerows(datos)
    
def LoginValidation(username, password):
    usernamePath = username.get() + ".csv"
    Data = [[]]

    if username.get() == "" or password.get() == "":
        ms.showinfo(message="Completa todos los campos",title="Campos requeridos")
        return

    # Si no existe el usuario
    if not exists(usernamePath):
        valor=ms.askokcancel(message="No se encontró el usuario\n¿Deseas registrar un usuario nuevo?",title="Usuario no encontrado")
        if valor:
            OpenRegisterWindow()
        else:
            username.delete(0,END)
            password.delete(0,END)
        return

    # Si existe
    with open(usernamePath) as archivo:
        lector = csv.reader(archivo,delimiter=",",
                            quotechar=",",
                            quoting=csv.QUOTE_MINIMAL)
        for renglon in lector:
            if(len(renglon)!=0):
                Data.append(renglon)
    
    #Comprobar contraseña
    if Data[2][0] == password.get():
        OpenCharacterSelectionWindow()
                
    #hay que ver cómo guardamos el usuario actualmente en la sesión. tal vez un arreglo global con toda la info, 
    #misma que usaría para guardar la partida en caso de que se cierre la ventana

    #Llamar funcion al cerrar ventana, ayudara para guardar partidas
    '''
    import tkinter as tk
    from tkinter import messagebox

    root = tk.Tk()
    def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)
    '''

# --- window
AccountsWindow = Tk() # instanciar
AccountsWindow.geometry("400x300") # alterar el tamanio
AccountsWindow.title("Juego Loco 3mil8mil") # editar el titulo
AccountsWindow.config(bg="#C1B9B9") # editar el background
AccountsWindow.iconbitmap("VamohIcon.ico") # editar el icono de la aplicacion


# button
LoginButton = Button(AccountsWindow, text="Iniciar sesión", command=OpenCharacterSelectionWindow) #cambiar a openloginwindow
LoginButton.place(relx=0.5,rely=0.4,anchor=CENTER)


# button
RegisterButton = Button(AccountsWindow, text="Usuario nuevo", command=OpenRegisterWindow)
RegisterButton.place(relx=0.5,rely=0.6,anchor=CENTER)

# label
GameTitle = Label(AccountsWindow, text="Juego Loco 3mil8mil")
GameTitle.place(relx=0.5,rely=0.1,anchor=CENTER)
GameTitle.config(bg="#C1B9B9")


AccountsWindow.mainloop()

