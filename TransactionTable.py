class TransactionTable:

    def __init__(self):
        self.transactions = {}

    def updateTransction(self, transactionID:int, status:str, LSN:int):
        self.transactions[transactionID] = (transactionID, status, LSN)
            
    
    def removeTransaction(self, transactionID:int):
        if transactionID in self.transactions :
            self.transactions.pop(transactionID)

    def listOfTransactionLSNs(self):
        lsns = []
        for transactionID in self.transactions:
            lsns.append(self.transactions[transactionID][2])
        return lsns

    
    def __str__(self):
        s = "Transaction Table\n"
        s += "(Transaction ID, Status, Last LSN)\n" 
        for transactionID in self.transactions:
            tran = self.transactions[transactionID]
            s += str(tran) + "\n"
        return s