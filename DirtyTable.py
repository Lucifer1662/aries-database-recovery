class DirtyTable:

    def __init__(self):
        self.pages = {}

    def dirtyPage(self, pageID:int, LSN:int):
        if not pageID in self.pages :
            self.pages[pageID] = LSN
    
    def unDirtyPage(self, pageID:int):
        if pageID in self.pages :
            self.pages.pop(pageID)

    def smallestRecLSN(self):
        smallestLSN = 100000000000

        for pageID in self.pages:
            LSN = self.pages[pageID]
            if LSN < smallestLSN :
                smallestLSN = LSN

        return smallestLSN

    def exists(self, pageID):
        return pageID in self.pages.keys()

    def getrecLSN(self, pageID):
        return self.pages[pageID]

    def __str__(self):
        s = "Dirty Page Table\n"
        s += "(Page ID, recLSN)\n" 
        for pageID in self.pages:
            LSN = self.pages[pageID]
            s += "("+str(pageID)+","+ str(LSN) + ")\n"
        return s