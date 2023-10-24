#Create a new Queue
EMPTY_STRING = ""
NULL_POINTER = -1
MAX_QUEUE_SIZE = 8

FrontOfQueuePointer = NULL_POINTER
EndOfQueuePointer = NULL_POINTER
NumberInQueue = 0

Queue = [EMPTY_STRING] * MAX_QUEUE_SIZE

def InitialiseQueue():
    global FrontOfQueuePointer, EndOfQueuePointer, NumberInQueue
    FrontOfQueuePointer = NULL_POINTER
    EndOfQueuePointer = NULL_POINTER
    NumberInQueue = 0

#Add Item to the Queue
def Enqueue(NewItem):
    if NumberInQueue < MAX_QUEUE_SIZE:
        EndOfQueuePointer = EndOfQueuePointer + 1

        if EndOfQueuePointer > MAX_QUEUE_SIZE - 1:
            EndOfQueuePointer = 0
        
        Queue[EndOfQueuePointer] = NewItem

        NumberInQueue = NumberInQueue + 1