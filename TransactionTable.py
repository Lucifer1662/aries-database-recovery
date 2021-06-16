class TransactionTable:

    def __init__(self):
        self.transactions = {}

    def updateTransction(self, transactionID:int, status:str, LSN:int):
        self.transactions[transactionID] = (transactionID, status, LSN)
            
    
    def removeTransaction(self, transactionID:int):
        if transactionID in self.transactions :
            self.transactions.pop(transactionID)

    def __str__(self):
        return ""

    def listOfTransactionLSNs(self):
        lsns = []
        for transactionID in self.transactions:
            lsns.append(self.transactions[transactionID][2])
        return lsns