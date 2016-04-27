
import unittest
import mock
from .context import Collection
from gProtocolBuffer import GProtocolBuffer
import remBook_pb2
import os

class TestTopics(unittest.TestCase):
  def setUp(self):
    self.collection = Collection('./tests/data/')
    self.list = []
    self.books = [remBook_pb2.Book(), remBook_pb2.Book()]
    self.books[0].name = "German";
    card = self.books[0].card.add()
    card.side.append('die Kueche')
    card.side.append('kitchen')
    card = self.books[0].card.add()
    card.side.append('das Wohnzimmer')
    card.side.append('livingroom')

    self.books[1].name = "German2";
    card = self.books[1].card.add()
    card.side.append('das Wohnzimmer')
    card.side.append('livingroom')
    card = self.books[1].card.add()
    card.side.append('das Schlafzimmer')
    card.side.append('bedroom')

  def tearDown(self):
    self.collection = None
    
  def testShouldAddFirstTopic(self):
    self.collection.modifyCollection("test")
    for key in self.collection.topics:
      self.list.append(key)
    self.assertCountEqual(["test"], self.list)

  def testShouldAddSeveralTopics(self):
    self.collection.modifyCollection("test2")
    self.collection.modifyCollection("test3")
    for key in self.collection.topics:
      self.list.append(key)
    self.assertCountEqual(["test3", "test2"], self.list)

  def testShouldNotAddExistingTopics(self):
    with mock.patch('builtins.input', return_value=''):
      self.collection.modifyCollection("test")
      self.collection.modifyCollection("test2")
      self.collection.modifyCollection("test")
      for key in self.collection.topics:
        self.list.append(key)
      self.assertCountEqual(["test2", "test"], self.list)

  def testShouldAddReenteredTopic(self):
    with mock.patch('builtins.input', side_effect=['r','test3']):
      self.collection.modifyCollection("test")
      self.collection.modifyCollection("test")
      for key in self.collection.topics:
        self.list.append(key)
      self.assertCountEqual(["test3", "test"], self.list)

  def testShouldDeleteTopic(self):
    with mock.patch('builtins.input', return_value='d'):
      self.collection.modifyCollection("test")
      self.collection.modifyCollection("test")
      self.assertEqual({}, self.collection.topics)
      
  def testShouldNotCallNoneTypeCallbackFunction(self):
    test = GProtocolBuffer('./tests/data/gProtoBuf')
    test.readBooks(None)

  def callbackFct(self,book):
    print(book.name)
    print("Here I am")
    i = 0
    for flashcard in book.card:
      self.assertTrue(len(flashcard.side[0]) != 0)
      self.assertTrue(len(flashcard.side[1]) != 0)
      i += 1
    self.assertEqual(2,i)

  def testShouldCallCallbackFunction(self):
    test = GProtocolBuffer('./tests/data/gProtoBuf')
    test.readBooks(self.callbackFct)

  def testShouldImportTopics(self):
    test = Collection('./tests/data/')
    test.importFromGProtocolBuffer('gProtoBuf')
    for topic in test.topics:
      self.list.append(topic)
    self.assertCountEqual(["German", "German2"], self.list)

  def testShouldSaveBooks(self):
    test = Collection('./tests/data/')
    test.exportTopics('gProtoBuf', self.books)
    self.existingFiles = [file for file in os.listdir('./tests/data/gProtoBuf') if file.endswith(".pb")]
    self.assertCountEqual(["German.pb", "German2.pb"], self.existingFiles)

if __name__ == '__main__':
    unittest.main()
