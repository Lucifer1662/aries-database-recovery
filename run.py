from DB import DB
from CheckPoint import CheckPoint
from DirtyTable import DirtyTable
from TransactionTable import TransactionTable
 
def main():
    db = DB()
    db.log.log(0,  None, None, "BEGIN_CHECKPOINT", None, None, None)
    db.log.log(5,  None, None, "END_CHECKPOINT", None, None, None)
    db.log.log(10, None, 1, "UPDATE", 5, None, None)
    db.log.log(20, None, 2, "UPDATE", 3, None, None)
    db.log.log(30, None, 1, "ABORT",  5, None, None)
    db.log.log(40, None, 1, "CLR",    5,    1, None)
    db.log.log(45, None, 1, "END", None, None, None)
    db.log.log(50, None, 3, "UPDATE", 1, None, None)
    db.log.log(60, 20, 2, "UPDATE", 1, None, None)
    
    db.lastCheckPoint = CheckPoint(0,1, DirtyTable(), TransactionTable())
    db.crash_recover()

    print(db)



main()