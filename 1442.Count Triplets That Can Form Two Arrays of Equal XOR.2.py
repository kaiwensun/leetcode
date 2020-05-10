from collections import defaultdict
class Solution(object):
    def countTriplets(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        h = defaultdict(lambda: [0, 0]) # [cnt, sum]
        h[0] = [1, -1]
        res = xor = 0
        for i in xrange(len(arr)):
            xor ^= arr[i]
            res += h[xor][0] * (i - 1) - h[xor][1]
            h[xor][0] += 1
            h[xor][1] += i
        return res
    
### Idea is from this:
# from collections import defaultdict
# class Solution(object):
#     def countTriplets(self, arr):
#         """
#         :type arr: List[int]
#         :rtype: int
#         """
#         h = defaultdict(list) # [cnt, sum]
#         prefix = [0]
#         xor = 0
#         for num in arr:
#             xor ^= num
#             prefix.append(xor)
#         res = 0
#         for i in xrange(len(arr) + 1):
#             xor = prefix[i]
#             res += sum(i - index for index in h[xor]) - len(h[xor])
#             h[xor].append(i)
#         return res
