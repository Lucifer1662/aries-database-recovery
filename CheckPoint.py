

class CheckPoint:
    def __init__(self, begin, end, dirty_page_table, transaction_table):
        self.dirty_page_table = dirty_page_table
        self.transaction_table = transaction_table
        self.begin = begin
        self.end = end
