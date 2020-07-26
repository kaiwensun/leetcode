#Result:
# 151 / 151 test cases passed.
# Status: Accepted
# Runtime: 68 ms
# Your runtime beats 63.83% of python submissions.
#Date:
# 10/16/2016

class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        cnt1 = {}
        cnt2 = {}
        bull = 0
        for c1,c2 in zip(secret,guess):
            if c1==c2:
                bull += 1
            else:
                if c1 in cnt1:
                    cnt1[c1]+=1
                else:
                    cnt1[c1]=1
                if c2 in cnt2:
                    cnt2[c2]+=1
                else:
                    cnt2[c2]=1
        cows = 0
        if len(cnt1)>len(cnt2):
            tmp = cnt1
            cnt1 = cnt2
            cnt2 = tmp
        for k in cnt1:
            if k in cnt2:
                cows += min(cnt1[k],cnt2[k])
        return str(bull)+'A'+str(cows)+'B'
            
            
