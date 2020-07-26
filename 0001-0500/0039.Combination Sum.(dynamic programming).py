"""
Basic idea:
	Dynamic programming / traceback
	Set
"""
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        self.removeDuplicate(candidates,target)
        dynam_table = {0:set([0])}
        for i in xrange(len(candidates)):
            newtable = {}
            for part_sum in dynam_table:
                part_sum = part_sum+candidates[i]
                while part_sum<=target:
                    if part_sum in newtable:
                        newtable[part_sum].add(candidates[i])
                    else:
                        newtable[part_sum]=set([candidates[i]])
                    part_sum = part_sum+candidates[i]
            for newsum,newset in newtable.iteritems():
                dynam_table[newsum] = dynam_table[newsum] | newtable[newsum] if newsum in dynam_table else newtable[newsum]
        result=[]
        self.traceback(result,dynam_table,target,[])
        return result
        
    def traceback(self,result,dynam_table,target,cur_path):
        if target==0:
            result.append(list(cur_path))
            return
        if target not in dynam_table:
            return
        cur_path.insert(0,-1)
        last = cur_path [1] if len(cur_path)>1 else float('inf')
        for x in dynam_table[target]:
            if x>last:
                continue
            cur_path[0]=x
            self.traceback(result,dynam_table,target-x,cur_path)
        del cur_path[0]
        
        
    def addNewTable(self,dynam_table,new_table):
        for part_sum,lst in new_table.iteritems():
            dynam_table[part_sum]=dynam_table[part_sum]+lst if part_sum in dynam_table else lst
        
        
        result_collector = []
        part_result=[]
        self.helper(result_collector,part_result,candidates,target,0)
        return result_collector

    def removeDuplicate(self,candidates,target):
        i=0
        while i<len(candidates)-1:
            if candidates[i]==candidates[i+1] or candidates[i+1]>target:
                del candidates[i+1]
            else:
                i=i+1

