class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        def find(x):
            if group[x] != x:
                group[x] = find(group[x])
            return group[x]
        
        def union(x, y):
            rx = find(x)
            ry = find(y)
            
            group[rx] = ry
            groupSize[ry] += groupSize[rx]
            return ry
            
        cnt = len(bloomDay)
        groupSize = [1] * cnt
        group = range(cnt)
        bloomed = [False] * cnt
        
        
        for day, flower in sorted(map(lambda x: list(reversed(x)) , enumerate(bloomDay))):
            bloomed[flower] = True
            leftsize = rightsize = 0
            if flower > 0 and bloomed[flower - 1]:
                leftsize = groupSize[find(flower - 1)]
                union(flower, flower - 1)
            if flower < cnt - 1 and bloomed[flower + 1]:
                rightsize = groupSize[find(flower + 1)]
                union(flower, flower + 1)
            m -= (leftsize + 1 + rightsize) / k - leftsize / k - rightsize / k
            if m <= 0:
                return day
        return -1
            
        
