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
    def __init__(self, XPosition, YPosition, NameP):
        super().__init__(XPosition, YPosition, NameP)
    
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
    