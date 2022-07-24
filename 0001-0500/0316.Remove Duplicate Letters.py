"""
Given the string s, the greedy choice (i.e., the leftmost letter in the answer) is the smallest s[i], s.t. the suffix s[i .. ] contains all the unique letters. (Note that, when there are more than one smallest s[i]'s, we choose the leftmost one. Why? Simply consider the example: "abcacb".)

After determining the greedy choice s[i], we get a new string s' from s by

removing all letters to the left of s[i],
removing all s[i]'s from s.
We then recursively solve the problem w.r.t. s'.

The runtime is O(26 * n) = O(n).

Referenfe: 
https://leetcode.com/discuss/73761/a-short-o-n-recursive-greedy-solution
"""

class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s=='':
            return ''
        bitmap = [0]*(len(s)+1)
        for i in xrange(len(s)-1,-1,-1):
            bitmap[i]=bitmap[i+1]|(1<<ord(s[i])-ord('a'))
        pair = map(lambda x,y:(x,y),s,bitmap[:len(s)])  #(char,bitmap)
        result = ''
        target = pair[0][1]
        start = 0
        end = len(s)
        while start<end:
            mi_chr = '{'
            mi_ind = 0
            for i in range(start,end):
                if target^pair[i][1]==0:
                    if pair[i][0]<mi_chr:
                        mi_chr=pair[i][0]
                        mi_ind = i
                else:
                    break
            result = result+mi_chr
            target = target&~(1<<(ord(mi_chr)-ord('a')))
            pair = [item for item in pair[mi_ind:] if item[0]!=mi_chr]
            pair = map(lambda x:(x[0],x[1]&target),pair)
            end = len(pair)
        return result

sol = Solution()
s = 'cbacdcbc'
print sol.removeDuplicateLetters(s)
