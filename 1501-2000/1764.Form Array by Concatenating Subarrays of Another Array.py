class Solution(object):
    def canChoose(self, groups, nums):
        """
        :type groups: List[List[int]]
        :type nums: List[int]
        :rtype: bool
        """
        group_hashes = [0] * len(groups)
        for i, group in enumerate(groups):
            group_hashes[i] = reduce(lambda a, b: a ^ b, group)
        num_hashes = [0] * (len(nums) + 1)
        for i, num in enumerate(nums):
            num_hashes[i + 1] = num_hashes[i] ^ num
        
        p = i = 0
        while i < len(groups) and p <= len(nums) - len(groups[i]):
            if group_hashes[i] == num_hashes[p + len(groups[i])] ^ num_hashes[p] and groups[i] == nums[p : p + len(groups[i])]:
                p += len(groups[i])
                i += 1
            else:
                p += 1
        return i == len(groups)

