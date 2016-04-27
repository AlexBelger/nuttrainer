import os
import shutil

import remBook_pb2
from topicFileAccess import TopicFileAccess

class GProtocolBuffer(TopicFileAccess):
    def readBooks(self,callbackFunction):              
        self.existingFiles = [file for file in os.listdir(self.dir) if file.endswith(".pb")]
        book = remBook_pb2.Book()
        for fileName in self.existingFiles:
            file = open(os.path.join(self.dir,fileName), "rb")
            book.ParseFromString(file.read())
            file.close()
            if callbackFunction is not None:
                callbackFunction(book)

    def writeBooks(self, books):
        os.rename(self.dir, self.dir + "tmp")
        os.makedirs(self.dir)
        for book in books:
            f = open(self.dir + "/" + book.name + ".pb", "wb")
            f.write(book.SerializeToString())
            f.close()
        shutil.rmtree(self.dir + "tmp")
