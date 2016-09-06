#Basic idea:
#   DFS and hashtable
#Result:
#   30 / 30 test cases passed.
#   Status: Accepted
#   Runtime: 99 ms
#   Your runtime beats 100.00% of pythonsubmissions
#Date:
#   9/6/2016

class Solution(object):
    lst = []
    dic = {}
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums==None or len(nums)==0:
            return []
        self.lst = []
        self.dic = {}
        for e in nums:
            if e in self.dic:
                self.dic[e]+=1
            else:
                self.dic[e]=1
        self.dfs([],len(nums))
        return self.lst
        
    def dfs(self, permut,length):
        if length==len(permut):
            self.lst.append(list(permut))
        else:
            for k,v in self.dic.items():
                if v==0:
                    continue
                else:
                    permut.append(k)
                    self.dic[k]-=1
                    self.dfs(permut,length)
                    permut.pop()
                    self.dic[k]+=1
        
