class Character:
    def __init__(self, charactername, dateofbirth, intelligence, speed):
        self.CharacterName = charactername #string
        self.DateOfBirth = dateofbirth #string
        self.Intelligence =  intelligence #real number
        self.Speed = speed #integer
    
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

class MagicCharacter(Character):
    def __init__(self, element, charactername, dateofbirth, intelligence, speed):
        super().__init__(charactername, dateofbirth, intelligence, speed)
        self.Element = element

    def Learn(self):
        if self.Element in ["water", "fire"]:
            intelligenceincrease = 1.2
        elif self.Element == "earth":
            intelligenceincrease = 1.3
        else:
            intelligenceincrease = 1.1
        
        self.Intelligence = self.Intelligence * intelligenceincrease

FirstMagic = MagicCharacter("fire", "Light", "28 January 2018", 70, 22)

FirstMagic.Learn()
print(f"The name of the character is {FirstMagic.GetName()}, their age is {FirstMagic.ReturnAge()}, their intelligence is {FirstMagic.GetIntelligence()}")
