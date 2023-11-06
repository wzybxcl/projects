Animal = [] #20 elements
Colour = [] #10 elements
global AnimalTopPointer
global ColourTopPointer
AnimalTopPointer = 0 
ColourTopPointer = 0

def PushAnimal(DataToPush):
    global AnimalTopPointer
    global ColourTopPointer
    if AnimalTopPointer == 20:
        return False
    else:
        Animal.append(DataToPush)
        AnimalTopPointer += 1
        return True

def PopAnimal():
    global AnimalTopPointer
    if AnimalTopPointer == 0:
        return ""
    else:
        ReturnData = Animal[AnimalTopPointer - 1]
        AnimalTopPointer -= 1
        return ReturnData
def ReadData():
    global AnimalTopPointer
    global ColourTopPointer
    try:
        AnimelFile = open("AnimalData.txt", "r")
        for line in AnimelFile:
            PushAnimal(line.strip())
        AnimelFile.close()
    except IOError:
        print("Please check if the file exists")
    
def PushColour(DataToPush):
    global ColourTopPointer
    if ColourTopPointer == 10:
        return False
    else:
        ColourTopPointer.append(DataToPush)
        ColourTopPointer += 1
        return True
    
def PopColour():
    global ColourTopPointer
    if ColourTopPointer == 0:
        return ""
    else:
        ReturnData = Colour[ColourTopPointer - 1]
        ColourTopPointer -= 1
        return ReturnData
    
def OutputItem():
    global AnimalTopPointer
    global ColourTopPointer
    IsAnimalThere = PopAnimal()
    IsColourThere = PopColour()
    if IsColourThere == 
