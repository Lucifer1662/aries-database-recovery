

class CheckPoint:
    def __init__(self, begin, end, diryPageTable, transactionTable):
        self.diryPageTable = diryPageTable
        self.transactionTable = transactionTable
        self.begin = begin
        self.end = end
