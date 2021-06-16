

class Pages:
    def __init__(self):
        self.pages = {}


    def getPageLSN(self, pageID):
        if(pageID in self.pages.keys()):
            return self.pages[pageID]
        return -1

    def writePageLSN(self, pageID, pageLSN):
        self.pages[pageID] = pageLSN

    def __str__(self):
        return ""