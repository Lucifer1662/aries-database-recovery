class DirtyTable:

    def __init__(self):
        self.page_object = {}

    def dirty_page(self, page_id:int, lsn:int):
        if page_id not in self.page_object :
            self.page_object[page_id] = lsn
    
    def undirty_page(self, page_id:int):
        if page_id in self.page_object :
            self.page_object.pop(page_id)

    def smallest_rec_lsn(self):
        smallest_lsn = 100000000000

        for page_id in self.page_object:
            lsn = self.page_object[page_id]
            if lsn < smallest_lsn :
                smallest_lsn = lsn

        return smallest_lsn

    def exists(self, page_id):
        return page_id in self.page_object.keys()

    def get_rec_lsn(self, page_id):
        return self.page_object[page_id]

    def __str__(self):
        s = "Dirty Page Table\n"
        s += "(Page ID, recLSN)\n" 
        for page_id in self.page_object:
            lsn = self.page_object[page_id]
            s += "("+"P"+str(page_id)+","+ str(lsn) + ")\n"
        return s