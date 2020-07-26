import copy
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        self.removeImpossible(candidates,target)
        result_collector = []
        part_result=[]
        self.helper(result_collector,part_result,candidates,target,0)
        return result_collector

    def removeImpossible(self,candidates,target):
        i=0
        while i<len(candidates):
            if candidates[i]>target:
                del candidates[i]
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
		    if i>startfrom and candidates[i]==candidates[i-1]:
		        continue
		    newtarget=target-candidates[i]
		    part_result[-1]=candidates[i]
		    if newtarget<0:
		        break
		    if newtarget==0:
		        result_collector.append(copy.deepcopy(part_result))
		        break
		    self.helper(result_collector,part_result,candidates,newtarget,i+1)
		del part_result[-1]

