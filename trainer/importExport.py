import abc
from gProtocolBuffer import GProtocolBuffer

class ImportExport(object):
    __metaclass__ = abc.ABCMeta
    
    def __init__(self, root = "./data/"):
        self.root = root 
        self.gProtoBuf = None

    def importFromGProtocolBuffer(self, dir = "gProtoBuf"):
      self.gProtoBuf = GProtocolBuffer( self.root + dir)
      self.gProtoBuf.readBooks(self.importTopic)

    @abc.abstractmethod
    def importTopic(self, book):
        """Copy the book content"""

    def exportTopics(self, dir, books):
      self.gProtoBuf = GProtocolBuffer( self.root + dir)
      self.gProtoBuf.writeBooks(books)
