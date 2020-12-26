from collections import defaultdict
class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        T = lambda: defaultdict(T)
        self.trie = T()


    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: None
        """
        def insert(p, i):
            if i == len(key):
                diff = val - p.get("$", 0)
                p["$"] = val
            else:
                diff = insert(p[key[i]], i + 1)
            p["#"] = p.get("#", 0) + diff
            return diff
        insert(self.trie, 0)

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        p = self.trie
        for c in prefix:
            if c not in p:
                return 0
            p = p[c]
        return p["#"]



# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)

