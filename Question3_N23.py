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
        birthyear = int(self.DateOfBirth.split()[-1])
        currentyear = 2023
        age = currentyear - birthyear

        return age

FirstCharacter = Character("Royal", "1 January 2019", 70, 30)

FirstCharacter.Learn()
print(f"The name of the character is {FirstCharacter.GetName()}, their age is {FirstCharacter.ReturnAge()}, their intelligence is {FirstCharacter.GetIntelligence()}")



