class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        data = {}
        def find(x):
            if x not in data:
                data[x] = x
            if data[x] != x:
                data[x] = find(data[x])
            return data[x]

        def union(x, y):
            data[find(x)] = find(y)
            
        for stone in stones:
            union(*enumerate(stone))
        for key in data.keys():
            find(key)
        return len(stones) - len(set(data.values()))
