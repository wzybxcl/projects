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
            arrayTreasure.append(treasureChest(question, answer, points))
            dataFetched = (file.readline()).strip()
            file.close()
        except IOError:
            print("Could not find file")
                