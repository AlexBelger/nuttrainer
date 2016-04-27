
import sys
from topic import Topic
import remBook_pb2
from importExport import ImportExport

class Collection(ImportExport):
    
    def __init__(self, dir):
        super(Collection, self).__init__(dir)
        self.topics = dict() #['German'] = Topic()

    def importTopic(self, book):
        if book.name in self.topics:
            self.topics[book.name].addCards(book.card)
        else:
            self.topics[book.name] = Topic(book.card)

    def modifyCollection(self, topic):
        while topic in self.topics:
            print("The topic already exists. r for rename, d for delete, q for quit") 
            self.selection = input()
            if self.selection == 'r' :
                topic = input()
                if len(topic) == 0:
                    print("An empty topic is invalid!")
                    return
            elif self.selection == 'd' :
                self.topics.pop(topic,None)
                return
            else:
                return

        self.topics[topic] = Topic()
        for key in self.topics:
            print(key)
        
