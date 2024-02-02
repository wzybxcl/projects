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
        if self.XPosition < 0:
            self.XPosition = 0

    def SetYPosition(self, value):
        self.YPosition = self.YPosition + value
        if self.YPosition > 10000:
            self.YPosition = 10000
        if self.YPosition < 0:
            self.YPosition = 0

    def Move(self, string):
        if string == "up":
            SetYPosition(self, 10)
        if string == "down:"
            SetYPosition(self, -10)