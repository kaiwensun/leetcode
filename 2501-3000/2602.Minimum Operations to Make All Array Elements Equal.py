import bisect

class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
        answer = []
        for q in queries:
            pivot = bisect.bisect_left(nums, q)
            res = (q * (pivot) - prefix[pivot]) + (prefix[-1] - prefix[pivot] - q * (len(nums) - pivot))
            answer.append(res)
        return answer

