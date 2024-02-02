from datetime import datetime

class Character:
    def __init__(self, charactername, dateofbirth, intelligence, speed):
        self.CharacterName = charactername
        self.DateOfBirth = dateofbirth
        self.Intelligence =  intelligence
        self.Speed = speed
    
    def GetIntelligence(self):
        return self.Intelligence
    
    def GetName(self):
        return self.CharacterName
    
    def SetIntelligence(self, value):
        self.Intelligence = value

    def Learn(self):
        self.Intelligence = self.Intelligence*1.1
    
    def ReturnAge(self):
        birthyear = self.DateOfBirth.year
        currentyear = 2023
        age = currentyear - birthyear

        return age

