class Character:
    def __init__(self,name,HP,type,powerUp,imagepath,attacks,advantage,disadvantage,normal):
        self.name = name
        self.HP = HP
        self.type = type
        self.attacks = attacks
        self.powerUp = powerUp
        self.imagepath=imagepath
        self.advantage = advantage
        self.disadvantage = disadvantage
        self.normal = normal

    def attack(self,attackedCharacter,attackIndex):
        # Si el ataque es el primero
        if attackIndex == 0:
            attackedCharacter.HP -= self.checkCorrectDamage(attackedCharacter.type)
            #damage = checkAdvantage(type) + powerUpDamage()
        else:
        # Si no solo se hace el daño
            attackedCharacter.HP -= self.attacks[attackIndex]



    def checkCorrectDamage(self,enemyType):
        #ventaja
        if self.hasAdvantage(enemyType):
            if self.powerUp:
                return self.attacks[4]
            else:
                return 5
        #desventaja
        elif self.hasDisadvantage(self,enemyType):
            if self.powerUp:
                return 4
            else:
                return 2
        #normal
        else:
            if self.powerUp:
                return 5
            else:
                return 3

    def hasAdvantage(self,enemyType):
        if self.type == "Agua" and (enemyType == "Roca" or enemyType == "Fuego"):
            return True
        elif self.type == "Fuego" and (enemyType == "Planta" or enemyType == "Escarabajo"):
            return True
        elif self.type == "Electrico" and (enemyType == "Agua" or enemyType == "Escarabajo"):
            return True
        elif self.type == "Escarabajo" and (enemyType == "Planta" or enemyType == "Roca"):
            return True
        elif self.type == "Planta" and (enemyType == "Agua" or enemyType == "Eléctrico" or enemyType == "Roca"):
            return True
        elif self.type == "Roca" and (enemyType == "Fuego" or enemyType == "Electrico"):
            return True
        else:
            return False

    def hasDisadvantage(self,enemyType):
        if self.type == "Agua" and (enemyType == "Electrico" or enemyType == "Planta"):
            return True
        elif self.type == "Fuego" and (enemyType == "Agua" or enemyType == "Roca"):
            return True
        elif self.type == "Electrico" and (enemyType == "Roca" or enemyType == "Planta"):
            return True
        elif self.type == "Escarabajo" and (enemyType == "Fuego" or enemyType == "Electrico"):
            return True
        elif self.type == "Planta" and (enemyType == "Fuego" or enemyType == "Escarabajo"):
            return True
        elif self.type == "Roca" and (enemyType == "Agua" or enemyType == "Planta"):
            return True
        else:
            return False

def initCharacters():
    characters = [
    Character("Aquarder",25,"Agua",False,"images/aquarder.png",{"Aqua-jet":[3,5,2,5,7,4],"Cola férrea":2,"Cabezazo":2,"Lluvia":None},["Roca","Fuego"],["Eléctrico","Planta"],["Agua","Escarabajo"]),
    Character("Electder",25,"Eléctrico",False,"images/electder.png",{"Trueno":[3,5,2,5,7,4],"Arañazo":3,"Mordisco":3,"Campo magnético":None},["Agua","Escarabajo"],["Roca","Planta"],["Eléctrico","Fuego"]),
    Character("Firesor",25,"Fuego",False,"images/firesor.png",{"Llamarada":[3,5,2,5,7,4],"Embestida":2,"Mordisco":2,"Día soleado":None},["Planta","Escarabajo"],["Agua","Roca"],["Eléctrico","Fuego"]),
    Character("Mousebug",25,"Escarabajo",False,"images/mousebug.png",{"Picotazo":[3,5,2,5,7,4],"Embestida":2,"Cabezazo":2,"Esporas":None},["Planta","Roca"],["Fuego","Electrico"],["Escarabajo","Agua"]),
    Character("Splant",25,"Planta",False,"images/splant.png",{"Hoja navaja":[3,5,2,5,7,4],"Mordisco":2,"Cabezazo":2,"Rayo solar":None},["Roca","Agua","Eléctrico"],["Fuego","Escarabajo"],["Planta"]),
    Character("Rockdog",25,"Roca",False,"images/rockdog.png",{"Roca afilado":[3,5,2,5,7,4],"Velocidad":2,"Cola ferrea":2,"Campo rocoso":None},["Fuego","Electrico"],["Agua","Planta"],["Roca","Escarabajo"])
    ]
    return characters


directory = {"Roca afilado":[3,5,2,5,7,4],"Velocidad":2,"Cola ferrea":2,"Campo rocoso":None}
print(["hola", "mamas"])