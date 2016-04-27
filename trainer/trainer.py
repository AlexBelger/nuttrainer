import sys
import readchar

class Trainer(object):

  def __init__(self):
    self.result = {}
    
  def start(self, topic):
    self.cards = topic.getCardsToTrain()[:]
    while self.cards:
      card = self.cards.pop()
      print(card.side[0])
      usrInput = input()
      if card.side[0] in self.result:
        self.result[card.side[0]] += int(usrInput == card.side[1]) + 1
      else:
        self.result[card.side[0]] = int(usrInput == card.side[1]) + 1
      if usrInput != card.side[1]:
        self.cards.insert(0,card)
        print(usrInput + " == " + card.side[0] + " = " + str(usrInput == card.side[1]))
        print("Continue by pressing a key")
        key = readchar.readchar();
        if key == '\x03' or key == '\x04' or key == '\x1A':
          sys.exit()
        print(repr(key))
    print(self.result)
    topic.saveTrainingResult(self.result)
