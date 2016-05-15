"""
Result:
  15 / 15 test cases passed.
  Status: Accepted
  Runtime: 299 ms
  Date: 5/14/2016
Idea: 
  Divide the elements to itervals [0][1][2 3][4 5 6 7][8 9 10 11 12 13 14 15]...
  The number of 1's in each intervals is a copy of all previous intervials but plus 1.
"""
class Solution(object):
    def recursive_countBits(self, num, cnt):
        if num==0:
            return
        mid = num/2
        self.recursive_countBits(mid,cnt)
        size = min(mid,len(cnt)-mid)
        cnt[mid:mid+size] = [x+1 for x in cnt[:size]]
        
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        cnt = [0 for i in xrange(num+1)]
        v = num
        num-=1;
        num |= num >> 1;
        num |= num >> 2;
        num |= num >> 4;
        num |= num >> 8;
        num |= num >> 16;
        num+=1;
        self.recursive_countBits(num, cnt)
        if v==num and v>0:
            cnt[-1]=1
        return cnt
