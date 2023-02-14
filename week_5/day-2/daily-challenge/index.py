# class Pagination():
#     def __init__(self, items = [], pageSize = 10):
#         self.item = items
#         self.pageSize = pageSize

#     def getVisibleItems(self):
#         alphabetList = "abcdefghijklmnopqrstuvwxyz".split('')
        

class Pagination:
    def __init__(self, items=None, pageSize=10):
        self.items = []
        self.pageSize = pageSize
        self.totalPages = (len(self.items) + self.pageSize - 1)
        self.currentPage = 1
        self._set_visible_items()

    def getVisibleItems(self):
        return self.visibleItems

    def prevPage(self):
        self.currentPage -= 1
        self._set_visible_items()
        return self

    def nextPage(self):
        self.currentPage += 1
        self._set_visible_items()
        return self

    def firstPage(self):
        self.currentPage = 1
        self._set_visible_items()
        return self

    def lastPage(self):
        self.currentPage = self.totalPages
        self._set_visible_items()
        return self

    def goToPage(self, pageNum):
        self.currentPage = max(min(int(pageNum), self.totalPages), 1)
        self._set_visible_items()
        return self

    def _set_visible_items(self):
        startIndex = (self.currentPage - 1) * self.pageSize
        endIndex = startIndex + self.pageSize
        self.visibleItems = self.items[startIndex:endIndex]



alphabetList = "abcdefghijklmnopqrstuvwxyz".split(" ")
p = Pagination(alphabetList, 4)

print(p.getVisibleItems()) 

p.nextPage().nextPage()

print(p.getVisibleItems()) 

p.lastPage()

print(p.getVisibleItems()) 

p.goToPage(10)

print(p.getVisibleItems()) 
