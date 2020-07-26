class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
    	if s=="":
    		return 0
    	record=[[-1,0]]*256	#(index,this_len)
    	max_len = 0
    	for index,c in enumerate(s):
    	    o = ord(c)
            record[o]=[index,min(record[ord(s[index-1])][1]+1,index-record[o][0])]
            if max_len<record[o][1]:
                max_len = record[o][1]
    	return max_len

