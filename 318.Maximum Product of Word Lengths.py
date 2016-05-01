class Solution(object):
    def maxProduct(self, words):
        #(length, mask) sorted according to decreasing length
        s = sorted(map(lambda w:(len(w),reduce(lambda x,y: x|1<<(ord(y)-ord('a')),w,0)),words) , lambda a,b:b[0]-a[0])
        mx ,mx_j_index = 0,len(words)
        for i in xrange(len(words)):
            for j in xrange(i+1,mx_j_index):
                if s[i][1]&s[j][1]==0 and s[i][0]*s[j][0]>=mx:
                    mx,mx_j_index = s[i][0]*s[j][0],min(mx_j_index,j)
                    break
        return mx
#The idea of truncating is that if the previous hit is s[mx_i_index][1]*s[mx_j_index][1], then for i>=mx_i_index and j>=mx_j_index we have s[mx_i_index][1]>s[i][1] and s[mx_j_index][1]>s[j][0].

