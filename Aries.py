from DB import DB
from CheckPoint import CheckPoint
from Logs import Logs
from Log import Log

class Aries:
    def __init__(self, db : DB):
        self.db = db
    
    def analysis(self, checkpoint: CheckPoint):
        start = self.db.log.indexOfLogId(checkpoint.begin)

        for logIndex in range(start, self.db.log.length()):
            log = self.db.log.getLogFromIndex(logIndex)

            if log.type == "END":
                self.db.transactionTable.removeTransaction(log.transactionID)
            elif log.transactionID is not None:
                status = "RUNNING" if log.type != "COMMIT" else "COMMITED"
                self.db.transactionTable.updateTransction(log.transactionID, status, log.LSN)

            if log.type == "UPDATE":
                self.db.diryPageTable.dirtyPage(log.pageID, log.LSN)
            
        

    def redo(self):
        smallestLSN = self.db.diryPageTable.smallestRecLSN()
        start = self.db.log.indexOfLogId(smallestLSN)
        
        for logIndex in range(start, self.db.log.length()):
            log = self.db.log.getLogFromIndex(logIndex)
            if log.type == "UPDATE" or log.type == "CLR":
                if not (
                    not self.db.diryPageTable.exists(log.pageID) or
                    self.db.diryPageTable.getrecLSN(log.pageID) > log.LSN or
                    self.db.pages.getPageLSN(log.pageID) > log.LSN
                    ):
                    #reaply the log action
                    print("Re did LSN:" + str(log.LSN))
                    #set pageLSN to LSN
                    self.db.pages.writePageLSN(log.pageID, log.LSN)

    def undo(self):
        toUndo = self.db.transactionTable.listOfTransactionLSNs()
        
        while(len(toUndo) > 0):
            toUndo.sort()
            largestLSN = toUndo[len(toUndo)-1]
            log = self.db.log.getLogFromLSN(largestLSN)
            if log.type == "CLR" and log.undonextLSN == None:
                self.db.writeLog(log.LSN, log.transactionID, "END", None, None, None)
                toUndo.pop()
            elif log.type == "CLR" and log.undonextLSN != None:
                toUndo.pop()
                toUndo.append(log.undonextLSN)
            else:
                print("Undo LSN:" + str(log.LSN))
                self.db.writeLog(log.LSN, log.transactionID, "CLR", log.pageID, log.LSN, log.prevLSN)
                toUndo.pop()
                if(log.prevLSN != None):
                    toUndo.append(log.prevLSN) 
                else:
                    self.db.writeLog(log.LSN, log.transactionID, "END", None, None, None)

            



    def recover(self,checkpoint: CheckPoint):
        self.analysis(checkpoint)
        self.redo()
        self.undo()



    
