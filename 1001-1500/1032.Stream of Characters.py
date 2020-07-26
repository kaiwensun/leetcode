class StreamChecker(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        T = lambda: collections.defaultdict(T)
        self.root = T()
        for word in words:
            node = self.root
            for c in word:
                node = node.setdefault(c, T())
            node['$'] = True
        self.active_searches = []
        print self.root
        

    def query(self, c):
        """
        :type letter: str
        :rtype: bool
        """
        self.active_searches = [node[c] for node in self.active_searches if c in node]
        if c in self.root:
            self.active_searches.append(self.root[c])
        return any('$' in node for node in self.active_searches)
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
