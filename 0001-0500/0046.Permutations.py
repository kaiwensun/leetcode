#Basic idea:
# DFS
#Result:
# 25 / 25 test cases passed.
# Status: Accepted
# Runtime: 69 ms
# Your runtime beats 80.43% of python submissions.
#Date:
# 10/2/2016

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        collector = []
        path = []
        remainder = set(nums)
        self.dfs(nums,path,collector,remainder)
        return collector
        
        
    def dfs(self,nums,path,collector,remainder):
        if len(remainder)==0:
            collector.append(list(path))
            return
        for ele in list(remainder): #keep current remainder
            remainder.remove(ele)
            path.append(ele)
            self.dfs(nums,path,collector,remainder)
            path.pop()
            remainder.add(ele)
