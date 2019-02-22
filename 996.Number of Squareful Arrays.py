class Solution(object):
    def numSquarefulPerms(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        self.neighbor = {}
        self.A = A
        self.getGraph()
        # print (self.neighbor)
        self.paths = set()
        self.result = set()
        for start in range(len(A)):
            if start in self.neighbor:
                self.dfs(start, [])
        # print self.result
        # uniq = set()
        # for res in self.result:
        #     vals = tuple([self.A[index] for index in res])
        #     uniq.add(vals)
        # print uniq
        return len(self.result)
        
    def index2val(self, indices):
        return tuple([self.A[index] for index in indices])
    
    def getGraph(self):
        for i in xrange(len(self.A)):
            a = self.A[i]
            for j in xrange(i + 1, len(self.A)):
                b = self.A[j]
                if self.isAdjacent(a, b):
                    # print i, j
                    # print a, b, 'is adjacent'
                    self.neighbor.setdefault(i, [])
                    self.neighbor.setdefault(j, [])
                    self.neighbor[i].append(j)
                    self.neighbor[j].append(i)
        
        
    def isAdjacent(self, a, b):
        s = a + b
        root = int(math.sqrt(a + b))
        return root * root == s
            
    def dfs(self, start, visited):
        if start in visited:
            return
        # print start, visited
        visited.append(start)
        if len(self.A) == len(visited):
            # print visited
            vals = self.index2val(visited)
            if vals not in self.result:
                self.result.add(vals)
            visited.pop(-1)
            return
        neighbors = self.neighbor[start]
        vals = set()
        uniq_neighbor_indices = set()
        for index in self.neighbor[start]:
            if self.A[index] not in vals and index not in visited:
                vals.add(self.A[index])
                uniq_neighbor_indices.add(index)
        for n in uniq_neighbor_indices:
            # print n, 'in', start, 'neighbors', self.neighbor[start]
            self.dfs(n, visited)
        visited.pop(-1)
            
        
            
