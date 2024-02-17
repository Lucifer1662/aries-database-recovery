

class Log:
    def __init__(self, lsn: int, prev_lsn: int, transaction_id:int, type:str, page_id:int, length:int, old:str, new:str, undo_lsn: int, undo_next_lsn: int):
        self.lsn = lsn
        self.prev_lsn = prev_lsn
        self.transaction_id = transaction_id
        self.type = type
        self.page_id = page_id
        self.length = length
        self.old = old
        self.new = new
        self.undo_next_lsn = undo_next_lsn
        self.undo_lsn = undo_lsn

    def __str__(self):
        s = str(self.lsn) + " " + str(self.type)
        if(self.type == "UPDATE"):
            return s + " T"+str(self.transaction_id) + " writes P" + str(self.page_id) + ", prev_lsn=" + str(self.prev_lsn) 
        if(self.type == "END"):
            return s + " T"+str(self.transaction_id)
        if(self.type == "ABORT"):
             return s + " T"+str(self.transaction_id)
        if(self.type == "CLR"):
            return s + " UNDO T"+str(self.transaction_id) + " lsn " + str(self.undo_lsn) + ", undo_next_lsn=" + str(self.undo_next_lsn) 
        return s