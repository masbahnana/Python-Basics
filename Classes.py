# Classes and objects
# Properties
# Behaviours
# Initializers and instances
# Inheritance

class GameCharacter:
    name = ""
    maxHP = 0
    currentHP = 0
    xPos = 0
    lives = 1

    def __init__(self,name,maxHP,xPos):
        self.name = name
        self.maxHP = maxHP
        self.currentHP = maxHP
        self.xPos = xPos

    def changeHP(self,changeInHP):
        self.currentHP += changeInHP
        if self.currentHP > self.maxHP:
            self.currentHP = self.maxHP
        elif self.currentHP < 0:
            self.currentHP = 0

    def changeXPos(self,changeInXPos):
        self.xPos += changeInXPos

class PlayerCharacter(GameCharacter):
    lives = 0
    inventory = []

    def __init__(self, name, maxHP, xPos):
        super(PlayerCharacter, self).__init__(name, maxHP, xPos)
        self.lives = 3
        self.inventory = ["shirt","pants"]

    def addInventoryItem(self, newItem):
        self.inventory.append(newItem)

    def changeHP(self,changeInHP):
        super(PlayerCharacter, self).changeHP(changeInHP)
        if self.currentHP <= 0:
            self.lives -= 1
            if self.lives < 0:
                self.lives = 0
            self.currentHP = self.maxHP

newGameCharacter = GameCharacter("Nimish",100,1)
newGameCharacter.changeHP(-200)
print(newGameCharacter.currentHP)
print(newGameCharacter.lives)

newPlayerCharacter = PlayerCharacter("Katie",150,10)
newPlayerCharacter.addInventoryItem("axe")
newPlayerCharacter.changeHP(-200)
print(newPlayerCharacter.currentHP)
print(newPlayerCharacter.lives)