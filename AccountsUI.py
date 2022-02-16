#Based on practica_funciones_grafico.py
# imports
import csv
from tkinter import *
from tkinter import messagebox as mss
import time



def SetupWindow(tkInstance,size,title,bgcolor,icon):
    tkInstance.geometry(size)
    tkInstance.title("Juego Loco 3mil8mil") # editar el titulo
    tkInstance.config(bg="#C1B9B9") # editar el background
    tkInstance.iconbitmap("VamohIcon.ico") # editar el icono de la aplicacion

def LoginWindow():
    AccountsWindow.destroy()
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
    StartButton = Button(LoginWindow, text="Iniciar", command=LoginWindow)
    StartButton.place(relx=0.5,rely=0.9,anchor=CENTER)

    LoginWindow.mainloop()

def RegisterWindow():
    AccountsWindow.destroy()
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
    RegisterButton = Button(RegisterWindow, text="Regitrar", command=RegisterWindow)
    RegisterButton.place(relx=0.5,rely=0.9,anchor=CENTER)

    RegisterWindow.mainloop()

def GamemodeWindow():
    GamemodeWindow = Tk() # instanciar
    GamemodeWindow.geometry("400x300") # alterar el tamanio
    GamemodeWindow.title("Juego Loco 3mil8mil") # editar el titulo
    GamemodeWindow.config(bg="#C1B9B9") # editar el background
    GamemodeWindow.iconbitmap("VamohIcon.ico") # editar el icono de la aplicacion

def DetailsWindow():
    DetailsWindow = Tk() # instanciar
    DetailsWindow.geometry("400x300") # alterar el tamanio
    DetailsWindow.title("Juego Loco 3mil8mil") # editar el titulo
    DetailsWindow.config(bg="#C1B9B9") # editar el background
    DetailsWindow.iconbitmap("VamohIcon.ico") # editar el icono de la aplicacion

def HistorySelectionWindow():
    HistorySelectionWindow = Tk() # instanciar
    HistorySelectionWindow.geometry("400x300") # alterar el tamanio
    HistorySelectionWindow.title("Juego Loco 3mil8mil") # editar el titulo
    HistorySelectionWindow.config(bg="#C1B9B9") # editar el background
    HistorySelectionWindow.iconbitmap("VamohIcon.ico") # editar el icono de la aplicacion

def TrainingSelectionWindow():
    TrainingSelectionWindow = Tk() # instanciar
    TrainingSelectionWindow.geometry("400x300") # alterar el tamanio
    TrainingSelectionWindow.title("Juego Loco 3mil8mil") # editar el titulo
    TrainingSelectionWindow.config(bg="#C1B9B9") # editar el background
    TrainingSelectionWindow.iconbitmap("VamohIcon.ico") # editar el icono de la aplicacion

def FightWindow():
    FightWindow = Tk() # instanciar
    FightWindow.geometry("400x300") # alterar el tamanio
    FightWindow.title("Juego Loco 3mil8mil") # editar el titulo
    FightWindow.config(bg="#C1B9B9") # editar el background
    FightWindow.iconbitmap("VamohIcon.ico") # editar el icono de la aplicacion

# --- window
AccountsWindow = Tk() # instanciar
AccountsWindow.geometry("400x300") # alterar el tamanio
AccountsWindow.title("Juego Loco 3mil8mil") # editar el titulo
AccountsWindow.config(bg="#C1B9B9") # editar el background
AccountsWindow.iconbitmap("VamohIcon.ico") # editar el icono de la aplicacion


# button
LoginButton = Button(AccountsWindow, text="Iniciar sesión", command=LoginWindow)
LoginButton.place(relx=0.5,rely=0.4,anchor=CENTER)


# button
RegisterButton = Button(AccountsWindow, text="Usuario nuevo", command=RegisterWindow)
RegisterButton.place(relx=0.5,rely=0.6,anchor=CENTER)

# label
GameTitle = Label(AccountsWindow, text="Juego Loco 3mil8mil")
GameTitle.place(relx=0.5,rely=0.1,anchor=CENTER)
GameTitle.config(bg="#C1B9B9")


AccountsWindow.mainloop()

