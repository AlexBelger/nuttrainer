

class TopicFileAccess:
    def __init__(self, dir):
        self.dir = dir
        
    def readBooks(self,callbackfunction):              
        raise NotImplementedError("Subclass must implement abstract method")

    def writeBooks(self, books):
        raise NotImplementedError("Subclass must implement abstract method")
    
