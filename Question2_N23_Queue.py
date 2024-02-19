global Queue #50 string elements
global Headpointer
global Tailpointer

Queue = []
Headpointer = -1
Tailpointer = 0

def Enqueue(Data):
    global Headpointer
    global Tailpointer
    global Queue

    if Tailpointer == 50:
        print("The queue is full")
    else:
        Queue.append(Data)
        Tailpointer += 1
        if Headpointer == -1:
            Headpointer = 0

def Dequeue():
    global Queue
    global Headpointer
    global Tailpointer
    if Headpointer == -1 or Headpointer == Tailpointer:
        print("Queue is empty")
        return "Empty"
    else:
        Headpointer += 1
        return Queue[Headpointer-1]
    
def ReadData():
    try:
        DataFile = open("QueueData.txt")
        for Line in DataFile:
            Enqueue(Line.strip())
        DataFile.close()
    except IOError:
        print("The File is not found")

class RecordData:
    def __init__(self, id, total):
        self.__ID = id   # string
        self.__Total =  total  #integer
    #stuff is private so create set/get methods
    def SetID(self, v):
        self.__ID = v
    def GetID(self):
        return self.__ID
    def SetTotal(self, v):
        self.__Total = v
    def GetTotal(self):
        return self.__Total
    

global NumberRecords
Records = [] #50 elements  of type RecordData 
NumberRecords = 0

def TotalData():
    global Records
    global NumberRecords
    DataAccessed = Dequeue()
    Flag = False

    if NumberRecords == 0:
        Records.append(RecordData(DataAccessed, 1))