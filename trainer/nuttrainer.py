
import sys, getopt
from collection import Collection
from trainer import Trainer

class NutTrainer(object):

    def __init__(self):
        self.collection = Collection('./data/')
        self.collection.importFromGProtocolBuffer('gProtoBuf')

    def command(self, argv):
        try:
            opts, args = getopt.getopt(argv,"mt:",["topic="])
        except getopt.GetoptError as err:
            print(err)
            self.usage()
            sys.exit(2)
        for opt, arg in opts:
            if opt == "-m":
                self.modify = True;
            elif opt in ("-t", "--topic"):
                if hasattr(self, 'modify'):
                    self.collection.modifyCollection(arg)
                else:
                  self.trainer = Trainer()
                  if arg in self.collection.topics:
                    self.trainer.start(self.collection.topics[arg])
                  else:
                    print("Error")
            elif o in ("-h", "--help"):
                self.usage()
                sys.exit()
            else:
                assert False, "unhandled option"
        if len(args) == 1 and hasattr(self,'topic'):
            print(args)

    def usage():
        print('remtrainer.py -t <topic>')
        
if __name__ == '__main__':
    NutTrainer().command(sys.argv[1:])

