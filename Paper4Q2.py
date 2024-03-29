class Character:
    def __init__(self, name, xposition, yposition):
        self.name = name
        self.XPosition =  xposition
        self.YPosition = yposition


    def GetX(self):
        return self.XPosition

    def GetY(self):
        return self.YPosition

    def SetXPosition(self, value):
        self.XPosition = self.XPosition + value
        if self.XPosition > 10000:
            self.XPosition = 10000
        elif self.XPosition < 0:
            self.XPosition = 0

    def SetYPosition(self, value):
        self.YPosition = self.YPosition + value
        if self.YPosition > 10000:
            self.YPosition = 10000
        elif self.YPosition < 0:
            self.YPosition = 0

    def Move(self, string):
        if string.lower() == "up":
            self.SetYPosition(10)
        elif string.lower() == "down":
            self.SetYPosition(-10)
        elif string.lower() == "right":
            self.SetXPosition(10)
        elif string.lower() == "left":
            self.SetXPosition(-10)

class BikeCharacter(Character):
    def __init__(self, name, XPosition, YPosition,):
        super().__init__(name, XPosition, YPosition)
    
    def Move(self, Direction):
        if Direction.lower() == "up":
            super().SetYPosition(20)
        if Direction.lower() == "down":
            super().SetYPosition(-20)
        if Direction.lower() == "right":
            super().SetXPosition(20)
        if Direction.lower() == "left":
            super().SetXPosition(-20)


Jack = Character("Jack", 50, 50)

Karla = BikeCharacter("Karla", 100, 50)

name = input("Would you like to move Jack or Karla?").lower()
while name not in ["jack", "karla"]:
    name = input("Invalid try again")

Direction = input("Which direction? Up, down, left or right?").lower()
while Direction not in ["up","down", "left", "right"]:
    Direction = input("Invalid try again: ").lower()

if name == "jack":
    Jack.Move(Direction)
    print(f"Jack's new position is X = {Jack.GetX()}, Y = {Jack.GetY()}")
else:
    Karla.Move(Direction)
    print(f"Karla's new position is X = {Karla.GetX()}, Y = {Karla.GetY()}")
    