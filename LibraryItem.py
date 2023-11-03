import datetime
class LibraryItem:
    def __init__(self, t, a, i):
        self.__Title = t
        self.__Author_Artist = a
        self.__ItemID = i
        self.__OnLoan = False
        self.__DueDate = datetime.date.today()

    @property
    def Title(self,):
        return self.__Title
    
    @property
    def AuthorArtist(self):
         return self.__Author_Artist
    
    @property
    def ItemID(self):
         return self.__ItemID
    
    @property
    def OnLoan(self):
         return self.__OnLoan
    
    @property
    def DueDate(self):
         return self.__DueDate
    
    def Borrowing(self):
         self.__OnLoan = True
         self.__DueDate = self.__DueDate + datetime.timedelta(weeks=3)

    def Returning(self):
         self.__OnLoan = False
         self.__DueDate = datetime.date.today()

    def PrintDetails(self):
        print ("Title: " + self.__Title)
        print ("Author: " + self.__Author_Artist)
        print ("Item ID: " + str(self.__ItemID))
        print ("On Loan: " + str(self.__OnLoan))
        print ("Due Date: " + str(self.__DueDate))

   
class Book(LibraryItem):

     def __init__(self, t, a, i):
          LibraryItem.__init__(self, t, a, i)    
          self.__IsRequested = False
          self.__RequestedBy = 0
    
     def GetIsRequested(self):
        return self.__IsRequested
     
     def GetRequestedBy(self):
          return self.__RequestedBy
     
     def Requesting(self, user_id):
          self.__IsRequested = True
          self.__RequestedBy = user_id
     
     def PrintDetails(self):
          LibraryItem.PrintDetails()
          print("Is requested" + str(self.__IsRequested))
          print("Requested by" + str(self.__RequestedBy))
     
class CD(LibraryItem):
     def __init__(self, t, a, i):
          LibraryItem.__init__(self, t, a, i)
          self.__Genre = ""
          
     def GetGenre(self):
          return self.__Genre
     
     def SetGenre(self, g):
          self.__Genre = g

     def PrintDetails(self):
          LibraryItem.PrintDetails(self)
          print("Genre:" + self.__Genre)


favourite_book = Book("No longer at ease", "Chinue Archebe", "001")

print(favourite_book.Title)



