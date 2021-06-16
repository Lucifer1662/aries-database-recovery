class Log:
    def __init__(self, LSN: int,prevLSN: int, transactionID:int, type:str, pageID:int, length:int, old:str, new:str, undoLSN: int, undonextLSN: int):
        self.LSN = LSN
        self.prevLSN = prevLSN
        self.transactionID = transactionID
        self.type = type
        self.pageID = pageID
        self.length = length
        self.old = old
        self.new = new
        self.undonextLSN = undonextLSN
        self.undoLSN = undoLSN

    def __str__(self):
        s = str(self.LSN) + " " + str(self.type)
        if(self.type == "UPDATE"):
            return s + " T"+str(self.transactionID) + " writes P" + str(self.pageID) + ", prevLSN=" + str(self.prevLSN) 
        if(self.type == "ABORT"):
             return s + " T"+str(self.transactionID)
        if(self.type == "CLR"):
            return s + " UNDO T"+str(self.transactionID) + " LSN " + str(self.undoLSN) + ", undonextLSN=" + str(self.undonextLSN) 
        return s