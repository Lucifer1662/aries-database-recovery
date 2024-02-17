from LogFile import LogFile
from DirtyTable import DirtyTable
from TransactionTable import TransactionTable
from Page import Page
from CheckPoint import CheckPoint

class DB:
    def __init__(self):
        self.log = LogFile()
        self.dirty_page_table = DirtyTable()
        self.transaction_table = TransactionTable()
        self.pages = Page()
        

    def crash_recover(self):
        from Aries import Aries
        aries = Aries(self)
        aries.recover(self.last_checkpoint)


    def write_log(self, prev_lsn: int, transaction_id:int, type:str, page_id:int, undo_lsn:int, undo_next_lsn:int):
        self.log.add_log(prev_lsn, transaction_id, type, page_id, undo_lsn, undo_next_lsn)

    def __str__(self):
        return  "\n" + self.log.__str__() + "\n" + self.dirty_page_table.__str__() + "\n" + self.transaction_table.__str__()