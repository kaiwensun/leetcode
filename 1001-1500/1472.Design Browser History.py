class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.stack = [homepage]
        self.index = 0

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        if self.index != len(self.stack) - 1:
            self.stack = self.stack[:self.index + 1]
        self.stack.append(url)
        self.index += 1
        

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        self.index -= steps
        self.index = max(self.index, 0)
        return self.stack[self.index]
        

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        self.index += steps
        self.index = min(self.index, len(self.stack) - 1)
        return self.stack[self.index]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
