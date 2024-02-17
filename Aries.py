from DB import DB
from CheckPoint import CheckPoint
from LogFile import LogFile
from Log import Log

class Aries:
    def __init__(self, db : DB):
        self.db = db
    
    def analysis(self, checkpoint: CheckPoint):
        start = self.db.log.index_of_log_id(checkpoint.begin)

        for log_index in range(start, self.db.log.length()):
            log = self.db.log.get_log_from_index(log_index)
            if log.type == "END":
                self.db.transaction_table.remove_transaction(log.transaction_id)
            elif log.transaction_id is not None:
                status = "RUNNING" if log.type != "COMMIT" else "COMMITED"
                self.db.transaction_table.update_transaction(log.transaction_id, status, log.lsn)
            if log.type == "UPDATE":
                self.db.dirty_page_table.dirty_page(log.page_id, log.lsn)
            
        

    def redo(self):
        smallest_lsn = self.db.dirty_page_table.smallest_rec_lsn()
        start = self.db.log.index_of_log_id(smallest_lsn)
        
        for log_index in range(start, self.db.log.length()):
            log = self.db.log.get_log_from_index(log_index)
            if  (
                    (
                        log.type == "UPDATE" or log.type == "CLR"
                    ) and not (
                        not self.db.dirty_page_table.exists(log.page_id) or
                        self.db.dirty_page_table.get_rec_lsn(log.page_id) > log.lsn or
                        self.db.pages.get_page_lsn(log.page_id) > log.lsn
                    )
                ):

                #reaply the log action
                print("Re did lsn:" + str(log.lsn))
                #set pageLSN to lsn
                self.db.pages.write_page_lsn(log.page_id, log.lsn)

    def undo(self):
        to_undo = self.db.transaction_table.list_of_transaction_lsns()
        
        while(len(to_undo) > 0):
            to_undo.sort()
            largest_lsn = to_undo[len(to_undo)-1]
            log = self.db.log.get_log_from_lsn(largest_lsn)
            if log.type == "CLR" and log.undo_next_lsn == None:
                self.db.write_log(log.lsn, log.transaction_id, "END", None, None, None)
                to_undo.pop()
            elif log.type == "CLR" and log.undo_next_lsn != None:
                to_undo.pop()
                to_undo.append(log.undo_next_lsn)
            else:
                print("Undo lsn:" + str(log.lsn))
                self.db.write_log(log.lsn, log.transaction_id, "CLR", log.page_id, log.lsn, log.prev_lsn)
                to_undo.pop()
                if(log.prev_lsn != None):
                    to_undo.append(log.prev_lsn) 
                else:
                    self.db.write_log(log.lsn, log.transaction_id, "END", None, None, None)

            



    def recover(self,checkpoint: CheckPoint):
        self.analysis(checkpoint)
        self.redo()
        self.undo()



    
