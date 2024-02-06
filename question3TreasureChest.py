arrayTreasure = []

class TreasureChest:
    def __init__(self, question, answer, points):
        self.__question = question #string
        self.__answer = answer #integer
        self.__points = points #integer

  # arrayTreasure(5) as treasureChest

    def readData():

        filename = "treasureChestData.txt"
        try:
            file= open(filename,"r")
            dataFetched = (file.readline()).strip()
            while(dataFetched != "" ):
                question = dataFetched
                answer = (file.readline()).strip()

                points = (file.readline()).strip()
                arrayTreasure.append(TreasureChest(question, answer, points))
                dataFetched = (file.readline()).strip()
            file.close()
        except IOError:
            print("Could not find file")
    
    def getQuestion(self):
        return self.__question
    
    def CheckAnswer(self, ans):
        if int(self.__answer) == ans:
            return True
        else:
            return False
        
    def getPoints(self, attempts):
        if attempts == 1:
            return int(self.__points)
        elif attempts == 2:
            return int(self.__points)// 2
        elif attempts == 3 or attempts == 4:
            return int(self.__points) // 4
        else:
            return 0
        
    readData()
    choice = int("Select a treasure chest to open")
    if choice > 0 and choice < 6:
        result = False 
        attempts = 0
        while result == False:
            answer = int(input(arrayTreasure[choice-1].getQuestion()))
            result = arrayTreasure[choice-1].CheckAnswer(answer)
            attempts += 1
        print(int(arrayTreasure[choice-1].getPoints(attempts)))
            