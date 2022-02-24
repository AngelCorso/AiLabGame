#Based on practica_funciones_grafico.py
# imports
from cgitb import text
import csv
from fileinput import close
import random
import select
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

def ClosePreviousWindow():
    try:
        LoginWindow.destroy()
    except:
        pass
    try:
        RegisterWindow.destroy()
    except:
        pass
    try:
        CharacterSelectionWindow.destroy()
    except:
        pass
    try:
        InitialWindow.destroy()
    except:
        pass
    try:
        GamemodeWindow.destroy()
    except:
        pass
    try:
        DetailsWindow.destroy()
    except:
        pass
    try:
        TrainingSelectionWindow.destroy()
    except:
        pass
    try:
        HistorySelectionWindow.destroy()
    except:
        pass
    try:
        FightWindow.destroy()
    except:
        pass

def SetupWindow(tkInstance,size,title,bgcolor,icon):
    tkInstance.geometry(size)
    tkInstance.title("Juego Loco 3mil8mil") # editar el titulo
    tkInstance.config(bg="#C1B9B9") # editar el background
    tkInstance.iconbitmap("VamohIcon.ico") # editar el icono de la aplicacion

def OpenLoginWindow():
    ClosePreviousWindow()
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
    ClosePreviousWindow()
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
    ClosePreviousWindow()
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
    ClosePreviousWindow()
    global HistorySelectionWindow
    HistorySelectionWindow = Tk() # instanciar
    HistorySelectionWindow.geometry("400x300") # alterar el tamanio
    HistorySelectionWindow.title("Juego Loco 3mil8mil") # editar el titulo
    HistorySelectionWindow.config(bg="#C1B9B9") # editar el background
    HistorySelectionWindow.iconbitmap("VamohIcon.ico") # editar el icono de la aplicacion

    HistorySelectionWindow.mainloop()

def OpenTrainingSelectionWindow():
    ClosePreviousWindow()
    global TrainingSelectionWindow
    TrainingSelectionWindow = Tk() # instanciar
    TrainingSelectionWindow.geometry("400x300") # alterar el tamanio
    TrainingSelectionWindow.title("Juego Loco 3mil8mil") # editar el titulo
    TrainingSelectionWindow.config(bg="#C1B9B9") # editar el background
    TrainingSelectionWindow.iconbitmap("VamohIcon.ico") # editar el icono de la aplicacion

    TrainingSelectionWindow.mainloop()

def OpenCharacterSelectionWindow():
    ClosePreviousWindow()
    global CharacterSelectionWindow
    CharacterSelectionWindow = Tk() # instanciar
    CharacterSelectionWindow.geometry("400x400") # alterar el tamanio
    CharacterSelectionWindow.title("Juego Loco 3mil8mil") # editar el titulo
    CharacterSelectionWindow.config(bg="#C1B9B9") # editar el background
    CharacterSelectionWindow.iconbitmap("VamohIcon.ico") # editar el icono de la aplicacion

    global characters
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
    # cuantityList = [0] * len(characters)

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
    
    cuantityList = [0,0,0,0,0,0]
    global charactersToFight
    charactersToFight = []


    Character1Label = Label(CharacterSelectionWindow,text="Aquarder",bg="#C1B9B9").grid(row=0,column=0)
    Character2Label = Label(CharacterSelectionWindow,text="Electder",bg="#C1B9B9").grid(row=0,column=1)
    Character3Label = Label(CharacterSelectionWindow,text="Firesor",bg="#C1B9B9").grid(row=0,column=2)
    Character1Button = Button(CharacterSelectionWindow,image=im1,command=partial(SelectCharacter,cuantityList,0))
    Character1Button.grid(row=1,column=0) #ipadx para acomodar tamaños
    Character2Button = Button(CharacterSelectionWindow,image=im2,command=partial(SelectCharacter,cuantityList,1))
    Character2Button.grid(row=1,column=1)
    # Character3Button = Button(CharacterSelectionWindow,image=im3,command=OpenLoginWindow).grid(row=1,column=2)
    Character3Button = Button(CharacterSelectionWindow,image=im3,command=partial(SelectCharacter,cuantityList,2))
    Character3Button.grid(row=1,column=2)

    Details1Button = Button(CharacterSelectionWindow,text="Detalle",command=partial(OpenDetailsWindow,characters[0])).grid(row=2,column=0)
    Details2Button = Button(CharacterSelectionWindow,text="Detalles",command=partial(OpenDetailsWindow,characters[1])).grid(row=2,column=1)
    Details3Button = Button(CharacterSelectionWindow,text="Detalle",command=partial(OpenDetailsWindow,characters[2])).grid(row=2,column=2)

    Character4Label = Label(CharacterSelectionWindow,text="Mousebug",bg="#C1B9B9").grid(row=3,column=0)
    Character5Label = Label(CharacterSelectionWindow,text="Splant",bg="#C1B9B9").grid(row=3,column=1)
    Character6Label = Label(CharacterSelectionWindow,text="Rockdog",bg="#C1B9B9").grid(row=3,column=2)
    Character4Button = Button(CharacterSelectionWindow,image=im4,command=partial(SelectCharacter,cuantityList,3))
    Character4Button.grid(row=4,column=0) #ipadx para acomodar tamaños
    Character5Button = Button(CharacterSelectionWindow,image=im5,command=partial(SelectCharacter,cuantityList,4))
    Character5Button.grid(row=4,column=1)
    Character6Button = Button(CharacterSelectionWindow,image=im6,command=partial(SelectCharacter,cuantityList,5))
    Character6Button.grid(row=4,column=2)
    Details4Button = Button(CharacterSelectionWindow,text="Detalle",command=partial(OpenDetailsWindow,characters[3])).grid(row=5,column=0)
    Details5Button = Button(CharacterSelectionWindow,text="Detalle",command=partial(OpenDetailsWindow,characters[4])).grid(row=5,column=1)
    Details6Button = Button(CharacterSelectionWindow,text="Detalle",command=partial(OpenDetailsWindow,characters[5])).grid(row=5,column=2)

    global ClearButton
    ClearButton = Button(CharacterSelectionWindow,text="Limpiar selecciones",command=partial(ClearSelections,cuantityList),state=tkinter.DISABLED)
    ClearButton.grid(row=7,column=2)
    StartButton = Button(CharacterSelectionWindow,text="Iniciar",command=OpenFightWindow).grid(row=6,column=1)

    global characterButtons
    characterButtons = [Character1Button,Character2Button,Character3Button,Character4Button,Character5Button,Character6Button]

    # Character1Label = Label(CharacterSelectionWindow,text="buenas").pack(side = TOP, pady = 0.5)
    # Character1Button = Button(CharacterSelectionWindow,text="buenas").pack(side = TOP, pady = 0.5)
    # Character1Button.place(relx=0.5,rely=0.6,anchor=CENTER)

    CharacterSelectionWindow.mainloop()

def OpenFightWindow():
    ClosePreviousWindow()
    global FightWindow
    global displayText
    FightWindow = Tk() # instanciar
    FightWindow.geometry("400x300") # alterar el tamanio
    FightWindow.title("Juego Loco 3mil8mil") # editar el titulo
    FightWindow.config(bg="#C1B9B9") # editar el background
    FightWindow.iconbitmap("VamohIcon.ico") # editar el icono de la aplicacion

    displayText = tkinter.StringVar()
    displayText.set("")
    global changeTurn
    changeTurn = tkinter.BooleanVar()
    changeTurn.set(False)

    characters = initCharacters()

    character1 = characters[0]
    character2 = characters[1]

    character1.isPlayer = True
    character2.isPlayer = False

    Ac = Label(FightWindow,textvariable=displayText)
    Ac.grid(row=7,column=0,columnspan=7,rowspan=4)

    attackNames = list(character1.attacks)

    Attack1Button = Button(FightWindow,text=attackNames[0],command=partial(UseAbility,character1,character2,attackNames[0]))
    Attack1Button.grid(row=0,column=0,ipadx=20)
    Attack2Button = Button(FightWindow,text=attackNames[1],command=partial(UseAbility,character1,character2,attackNames[1]))
    Attack2Button.grid(row=1,column=0)
    Attack3Button = Button(FightWindow,text=attackNames[2],command=partial(UseAbility,character1,character2,attackNames[2]))
    Attack3Button.grid(row=2,column=0)
    global powerUpButton
    global attackButtons
    global character1HP
    global character2HP
    character1HP = tkinter.IntVar()
    character1HP.set(25)
    character2HP = tkinter.IntVar()
    character2HP.set(25)
    attackButtons = [Attack1Button,Attack2Button,Attack3Button]
    powerUpButton = Button(FightWindow,text=character1.powerUpName,command=partial(activatePowerUp,character1))
    powerUpButton.grid(row=3,column=0)

    Im1 = Image.open(character1.imagePath)
    Im2 = Image.open(character2.imagePath)
    #Modificamos la imagen a un tamaño predeterminado
    newsize = (100,100)
    Im_1 = Im1.resize(newsize)
    Im_2 = Im2.resize(newsize)
    #Generar la imagen para Tk
    im1 = ImageTk.PhotoImage(Im_1)
    im2 = ImageTk.PhotoImage(Im_2)

    # characterImages = [im1,im2,im3,im4,im5,im6]
    Label(FightWindow,image=im1).grid(row=0,column=1, rowspan=4)
    Label(FightWindow,image=im2).grid(row=0,column=2, rowspan=4)
    Label(FightWindow,text="HP").grid(row=5,column=1)
    Label(FightWindow,text="HP").grid(row=5,column=2)
    Label(FightWindow,textvariable=character1HP).grid(row=6,column=1)
    Label(FightWindow,textvariable=character2HP).grid(row=6,column=2)
    # while character1.HP > 0 and character2.HP > 0:

    
    # FightWindow.after(2000,partial(FirstTurn,changeTurn,Ac))

    #probar si hacer el while dentro de first turn jala, a la vez calar el while con una condicion posible de cambiar
    StartFight(character1,character2)
            
    FightWindow.mainloop()

def activatePowerUp(character):
    character.activatePowerUp()
    displayText.set(character.name + " ha utilizado " + character.powerUpName +"\nQuedan 2 movimientos")
    if character.isPlayer:
        powerUpButton.config(state=DISABLED)
        changeTurn.set(not changeTurn.get())
        for button in attackButtons:
            button.config(state=DISABLED)
 
def updatePowerUp(character):
    character.updatePowerUp()
    if character.isPlayer and character.isPowerUpAvailable:
        powerUpButton.config(state=NORMAL)

def StartFight(player,cpu):

    FightWindow.update_idletasks()
    t=random.randint(1,2)
    if cpu.isPowerUpAvailable:
        randomAttack = random.randint(0,3)
    else:
        randomAttack = random.randint(0,2)

    cpuAttacksNames = list(cpu.attacks)
    print("primer turno" + str(t))
    if (t==1):
        # Ac.config(text="Primer movimiento es tuyo\n¡¡Piensa bien!!\n")
        displayText.set("Primer movimiento es tuyo\n¡¡Piensa bien!!\n")
        FightWindow.wait_variable(changeTurn) #Esto al cambiar esto significa que el prota ataca
        FightWindow.update()
        print(str(player.powerUpTurnsCounter) + " counter")
        updatePowerUp(player)
        print(str(player.powerUpTurnsCounter) + " counter")
        time.sleep(2)

    else:
        displayText.set("Primer movimiento es del CPU\n¡¡Cuidado!!\n")
        disableButtons(attackButtons)
        powerUpButton.config(state=DISABLED)
        FightWindow.update()
        time.sleep(2)
        if randomAttack < 3:
            UseAbility(cpu,player,cpuAttacksNames[randomAttack])
        else:
            activatePowerUp(cpu)
        FightWindow.update()
        updatePowerUp(cpu)
        time.sleep(2)
    print("ya fue primer turno")
    powerUpButton.config(state=DISABLED)
    # Turns(changeTurn,Ac)
    life = 25
    life2 = 25
    #primer turno fue el del jugador, sigue el cpu
    while (player.HP > 0 and cpu.HP > 0):
        if cpu.isPowerUpAvailable:
            randomAttack = random.randint(0,3)
        else:
            randomAttack = random.randint(0,2)

        if changeTurn.get():
            changeTurn.set(not changeTurn.get()) 

            displayText.set("Turno del CPU...")
            print("turno de cpu")   
            disableButtons(attackButtons)
            powerUpButton.config(state=DISABLED)

            FightWindow.update()
            
            time.sleep(2)

            if randomAttack < 3:
                UseAbility(cpu,player,cpuAttacksNames[randomAttack])
            else:
                activatePowerUp(cpu)

            FightWindow.update()

            updatePowerUp(cpu)

            time.sleep(2)

        #primer movimiento fue del cpu
        else:
            displayText.set("¡¡¡Tu turno!!!")

            print("turno de jugador")

            enableButtons(attackButtons)
            if (player.isPowerUpAvailable):
                powerUpButton.config(state=NORMAL)

            FightWindow.wait_variable(changeTurn) #Esto al cambiar esto significa que el prota ataca
            FightWindow.update()

            print(str(player.powerUpTurnsCounter) + " counter")

            updatePowerUp(player)

            print(str(player.powerUpTurnsCounter) + " counter")
            time.sleep(2)
    
    print("se termino")
    '''
    winner = True if cpu.HP <= 0 else False
    historyMode =True
    if historyMode:
        if winner:
            pass
        else:
            pass
        OpenCharacterSelectionWindow()
    else:
        if winner:
            pass
        else:
            pass
        OpenCharacterSelectionWindow()
    '''
            
def UseAbility(attackingCharacter,attackedCharacter,attackName):

    damage = attackingCharacter.attack(attackedCharacter.type,attackName)
    print(str(damage) + " damage con " + attackName)
    attackedCharacter.receiveDamage(damage)

    if attackingCharacter.isPlayer:
        changeTurn.set(not changeTurn.get())
        for button in attackButtons:
            button.config(state=DISABLED)
        character2HP.set(character2HP.get()-damage)
    else:
        character1HP.set(character1HP.get()-damage)

    displayText.set(attackingCharacter.name + " ha utilizado " + attackName)

def disableButtons(buttons):
    for button in buttons:
        button.config(state=DISABLED)

def enableButtons(buttons):
    for button in buttons:
        button.config(state=NORMAL)

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
    else:
        ms.showerror(message="Contraseña incorrecta",title="No fue posible iniciar sesión")
        password.delete(0,END)
                
def OpenInitialWindow():


    # --- window
    global InitialWindow
    InitialWindow = Tk() # instanciar
    InitialWindow.geometry("400x300") # alterar el tamanio
    InitialWindow.title("Juego Loco 3mil8mil") # editar el titulo
    InitialWindow.config(bg="#C1B9B9") # editar el background
    InitialWindow.iconbitmap("VamohIcon.ico") # editar el icono de la aplicacion


    # button
    LoginButton = Button(InitialWindow, text="Iniciar sesión", command=OpenLoginWindow) #cambiar a openloginwindow
    LoginButton.place(relx=0.5,rely=0.4,anchor=CENTER)


    # button
    RegisterButton = Button(InitialWindow, text="Usuario nuevo", command=OpenRegisterWindow)
    RegisterButton.place(relx=0.5,rely=0.6,anchor=CENTER)

    # label
    GameTitle = Label(InitialWindow, text="Juego Loco 3mil8mil")
    GameTitle.place(relx=0.5,rely=0.1,anchor=CENTER)
    GameTitle.config(bg="#C1B9B9")

    InitialWindow.mainloop()

def SelectCharacter(cuantityList, index):

    cuantityList[index] += 1

    charactersToFight.append(characters[index])

    if sum(cuantityList) >= 2:
        for button in characterButtons:
            button.config(state=DISABLED)
        ClearButton.config(state=NORMAL)


    if cuantityList[index] != 1 or sum(cuantityList) > 1:
        characterButtons[index].config(bg="#2596be")
    else:
        characterButtons[index].config(bg="#873e23")

def ClearSelections(cuantityList):
    for button in characterButtons:
        button.config(state=NORMAL,bg="SystemButtonFace")

    for i in range(len(cuantityList)):
        cuantityList[i] = 0

    ClearButton.config(state=DISABLED)
    charactersToFight.clear()


OpenFightWindow()

# Bindear botno a tecla y detectar cierre de ventana
'''
#hay que ver cómo guardamos el usuario actualmente en la sesión. tal vez un arreglo global con toda la info, 
#misma que usaría para guardar la partida en caso de que se cierre la ventana
boton.bind("<Return>", saludar_enter)

#Llamar funcion al cerrar ventana, ayudara para guardar partidas
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
def on_closing():
if messagebox.askokcancel("Quit", "Do you want to quit?"):
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)
'''