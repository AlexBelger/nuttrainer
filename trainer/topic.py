
import sys, getopt

class Topic:
  def __init__(self, cards = None):
    self.addCards(cards)

  def addCards(self, cards):
    self.cards = cards
        
  def getCardsToTrain(self):
    return self.cards

  def saveTrainingResult(self, result):
    print("To implement")
      
    def modifyTopics(self, topic):
        while topic in self.names:
            print("The topic already exists. r for rename, d for delete, q for quit") 
            self.selection = input()
            if self.selection == 'r' :
                topic = input()
                if len(topic) == 0:
                    print("An empty topic is invalid!")
                    return
            elif self.selection == 'd' :
                self.names.pop(topic,None)
                return
            else:
                return

        self.names[topic] = Topics()
        for key in self.names:
            print(key)
        
