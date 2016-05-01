import copy
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        self.removeDuplicate(candidates)
        result_collector = []
        part_result=[]
        self.helper(result_collector,part_result,candidates,target,0)
        return result_collector

    def removeDuplicate(self,candidates):
        i=0
        while i<len(candidates)-1:
            if candidates[i]==candidates[i+1]:
                del candidates[i+1]
            else:
                i=i+1

    def helper(self,result_collector,part_result,candidates,target,startfrom):
		"""
		the role of startfrom is to make sure a result is in non-descending order, and thus unique
		"""
        if target==0:
            return part_result
        if target<0:
            return []
        part_result.append(-1)
        for i in xrange(startfrom,len(candidates)):
            newtarget = target-candidates[i]
            part_result[-1]=candidates[i]
            if newtarget<0:
                break
            if newtarget==0:
                result_collector.append(copy.deepcopy(part_result))
                break
            self.helper(result_collector,part_result,candidates,newtarget,i)
        del part_result[-1]

