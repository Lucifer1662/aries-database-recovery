class TransactionTable:

    def __init__(self):
        self.transactions = {}

    def update_transaction(self, transaction_id:int, status:str, lsn:int):
        self.transactions[transaction_id] = (transaction_id, status, lsn)
            
    
    def remove_transaction(self, transaction_id:int):
        if transaction_id in self.transactions :
            self.transactions.pop(transaction_id)

    def list_of_transaction_lsns(self):
        lsns = []
        for transaction_id in self.transactions:
            lsns.append(self.transactions[transaction_id][2])
        return lsns

    
    def __str__(self):
        s = "Transaction Table\n"
        s += "(Transaction ID, Status, Last lsn)\n" 
        for transaction_id in self.transactions:
            tran = self.transactions[transaction_id]
            s += "(" + "T" +str(tran[0])+ "," + str(tran[1]) + "," + str(tran[2])+ ")" + "\n"
        return s