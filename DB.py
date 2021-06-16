from Logs import Logs
from DirtyTable import DirtyTable
from TransactionTable import TransactionTable
from Pages import Pages
from CheckPoint import CheckPoint

class DB:
    def __init__(self):
        self.log = Logs()
        self.diryPageTable = DirtyTable()
        self.transactionTable = TransactionTable()
        self.pages = Pages()
        

    def crachReocover(self):
        from Aries import Aries
        aries = Aries(self)
        aries.recover(self.lastCheckPoint)


    def writeLog(self, prevLSN: int, transactionID:int, type:str, pageID:int, undoLSN:int, undonextLSN:int):
        self.log.addLog(prevLSN, transactionID, type, pageID, undoLSN, undonextLSN)

    def __str__(self):
        return  "\n" + self.log.__str__() + "\n" + self.diryPageTable.__str__() + "\n" + self.transactionTable.__str__()