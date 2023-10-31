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
    ReturnData = None
    global AnimalTopPointer
    if AnimalTopPointer == 0:
        return ReturnData
    else:
        ReturnData = Animal[AnimalTopPointer - 1]
        AnimalTopPointer -= 1
        return ReturnData

def ReadData():
    try:
        AnimelFile = open("AnimalData.txt", "r")
        for line in AnimelFile:
            PushAnimal(line)
        AnimelFile.close
    except IOError:
        print("Please check if the file exists")
    
def PushColour(DataToPush):
    global ColourTopPointer