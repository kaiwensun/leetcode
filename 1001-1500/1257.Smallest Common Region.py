class Solution(object):
    def findSmallestRegion(self, regions, region1, region2):
        """
        :type regions: List[List[str]]
        :type region1: str
        :type region2: str
        :rtype: str
        """
        graph = {}
        for lst in regions:
            parent = lst[0]
            for child in lst[1:]:
                graph[child] = parent
        region1_ancestors = set()
        while region1:
            region1_ancestors.add(region1)
            region1 = graph.get(region1)
        while region2:
            if region2 in region1_ancestors:
                return region2
            region2 = graph[region2]
            
