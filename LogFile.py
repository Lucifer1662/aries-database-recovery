from Log import Log
from typing import List


class LogFile:
    def __init__(self):
        self.log_object  : List[Log]() = list() # type: ignore


    def get_prev_lsn(self, transaction_id):
        for i in range(len(self.log_object)-1, -1,-1):
            if(self.log_object[i].transaction_id == transaction_id):
                return self.log_object[i].lsn
        return None

    def log(self, lsn:int, prev_lsn: int, transaction_id:int, type:str, page_id:int, undo_lsn:int, undo_next_lsn:int):
        self.log_object.append(Log(lsn, prev_lsn, transaction_id, type, page_id, 0, "", "", undo_lsn, undo_next_lsn))

    def add_log(self, prev_lsn: int, transaction_id:int, type:str, page_id:int, undo_lsn:int, undo_next_lsn:int):
        self.add_log_data(prev_lsn, transaction_id, type, page_id, 0, "", "", undo_lsn, undo_next_lsn)
    
    def add_log_data(self, prev_lsn: int, transaction_id:int, type:str, page_id:int, length:int, old:str, new:str, undo_lsn: int, undo_next_lsn: int):
        last_lsn = self.log_object[len(self.log_object) - 1].lsn

        lsn = last_lsn + 1

        self.log_object.append(Log(lsn, prev_lsn, transaction_id, type, page_id, length, old, new, undo_lsn, undo_next_lsn))

    def add_logs(self, log_object):
        self.log_object.extend(log_object) 

    def index_of_log_id(self, lsn):
        index = 0
        for log in self.log_object:
            if(log.lsn == lsn):
                return index
            index = index + 1
        return -1

    def get_log_from_index(self, log_index) -> Log:
        return self.log_object[log_index]

    def length(self):
        return self.log_object.__len__()

    def get_log_from_lsn(self, lsn) -> Log:
        return self.get_log_from_index(self.index_of_log_id(lsn))

    def __str__(self):
        s = str("")
        for log in self.log_object:
            s += log.__str__()
            s += "\n"
        return s