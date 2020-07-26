"""
 Result:
   20 / 20 test cases passed.
   Status: Accepted
   Runtime: 124 ms
 Date:
    5/4/2016
 Basic idea:
    use hash table (dict) to count
    use priority queue (heapq) to select first k
    the standart library heapq use __lt__ to compare elements
 Reference:
    Source code of heapq: https://hg.python.org/cpython/file/2.7/Lib/heapq.py
""" 


import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic = {}
        for num in nums:
            if num in dic:
                dic[num]+=1
            else:
                dic[num]=1
    
        counter = [Pair(num,cnt) for num,cnt in dic.iteritems()]
        nlargest = heapq.nlargest(k,counter)
        return [pair.num for pair in nlargest]



class Pair(object):
    def __init__(self,num,cnt):
        self.num = num
        self.cnt = cnt
    
    #only __lt__ is used by heapq
    def __lt__(self,other):
        return self.cnt<other.cnt
