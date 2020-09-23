class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        cnts = []
        for num in nums:
            for cnt in cnts:
                if cnt[1] == num:
                    cnt[0] += 1
                    break
            else:
                if len(cnts) < 2:
                    cnts.append([1, num])
                else:
                    for cnt in cnts:
                        cnt[0] -= 1
                while cnts and cnts[-1][0] == 0:
                    cnts.pop()
            cnts.sort(reverse=True)
        return [n for _, n in cnts if len(filter(lambda num: num == n, nums)) > len(nums) // 3]

