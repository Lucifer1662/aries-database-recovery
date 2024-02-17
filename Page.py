

class Page:
    def __init__(self):
        self.page_object = {}


    def get_page_lsn(self, page_id):
        if(page_id in self.page_object.keys()):
            return self.page_object[page_id]
        return -1

    def write_page_lsn(self, page_id, page_lsn):
        self.page_object[page_id] = page_lsn

    def __str__(self):
        return ""