from Log import Log
from typing import List


class Logs:
    def __init__(self):
        self.logs  : List[Log]() = list()


    def getPrevLSN(self, transactionID):
        for i in range(len(self.logs)-1, -1,-1):
            if(self.logs[i].transactionID == transactionID):
                return self.logs[i].LSN
        return None

    def log(self, LSN:int, prevLSN: int, transactionID:int, type:str, pageID:int, undoLSN:int, undonextLSN:int):
        self.logs.append(Log(LSN, prevLSN, transactionID, type, pageID, 0, "", "", undoLSN, undonextLSN))

    def addLog(self, prevLSN: int, transactionID:int, type:str, pageID:int, undoLSN:int, undonextLSN:int):
        self.addLogData(prevLSN, transactionID, type, pageID, 0, "", "", undoLSN, undonextLSN)
    
    def addLogData(self, prevLSN: int, transactionID:int, type:str, pageID:int, length:int, old:str, new:str, undoLSN: int, undonextLSN: int):
        lastLSN = self.logs[len(self.logs) - 1].LSN

        LSN = lastLSN + 1

        self.logs.append(Log(LSN, prevLSN, transactionID, type, pageID, length, old, new, undoLSN, undonextLSN))

    def addLogs(self, logs):
        self.logs.extend(logs) 

    def indexOfLogId(self, LSN):
        index = 0
        for log in self.logs:
            if(log.LSN == LSN):
                return index
            index = index + 1
        return -1

    def getLogFromIndex(self, logIndex) -> Log:
        return self.logs[logIndex]

    def length(self):
        return self.logs.__len__()

    def getLogFromLSN(self, LSN) -> Log:
        return self.getLogFromIndex(self.indexOfLogId(LSN))

    def __str__(self):
        s = str("")
        for log in self.logs:
            s += log.__str__()
            s += "\n"
        return s