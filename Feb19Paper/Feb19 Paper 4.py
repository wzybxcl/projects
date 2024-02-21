#Question 1
TheData = [20, 3, 4, 8, 12, 99, 4, 26, 4]

def InsertionSort(TheData):
    for i in range(0, len(TheData)):
        DataToInsert = TheData[i]
        Inserted = 0
        NextValue = i - 1
        while(NextValue >= 0 and Inserted != 1):
            if(DataToInsert < TheData[NextValue]):
                TheData[NextValue+1] = TheData[NextValue]
                NextValue = NextValue - 1
                TheData[NextValue+1] = DataToInsert
            else:
                Inserted = 1

def PrintArray(TheData):
    for count in range(0, len(TheData)):
        print(TheData[count])

'''
print("Before sorting:")
PrintArray(TheData)
InsertionSort(TheData)
print("After sorting:")
PrintArray(TheData)
'''

def Search(TheData):
    NumberInput = int(input("Enter a whole number"))
    for count in range(0, len(TheData)):
        if(TheData[count] == NumberInput):
            print("Found")
            return True
    print("Not found")
    return False

#Question 2

class HiddenBox:
    # __BoxName String
    # __Creator String
    # __DateHidden String
    # __GameLocation String
    # __LastFinds [10][2] String
    # __Active String
    def __init__(self, NewBoxName, NewCreator, NewDateHidden, NewLocation):
        self.__BoxName = NewBoxName
        self.__Creator = NewCreator
        self.__DateHidden = NewDateHidden
        self.__GameLocation = NewLocation
        self.__LastFinds = [["" for j in range(0,2)] for i in range (0,10)]
        self.__Active = False

    