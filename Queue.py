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