from collections import defaultdict
class ThroneInheritance(object):

    def __init__(self, kingName):
        """
        :type kingName: str
        """
        self.children = defaultdict(list)
        self.parent = {}
        self.king = kingName
        self.dead = set()
        
        

    def birth(self, parentName, childName):
        """
        :type parentName: str
        :type childName: str
        :rtype: None
        """
        self.children[parentName].append(childName)
        self.parent[childName] = parentName

    def death(self, name):
        """
        :type name: str
        :rtype: None
        """
        self.dead.add(name)

    def getInheritanceOrder(self, node=None, res=None):
        """
        :rtype: List[str]
        """
        res = []
        self.dfs(self.king, res)
        return res
        
    def dfs(self, node, res):
        if node not in self.dead:
            res.append(node)
        for child in self.children[node]:
            self.dfs(child, res)


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()

