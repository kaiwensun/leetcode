from collections import Counter

class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.counter = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        num = self.nums2[index]
        self.counter[num] -= 1
        if self.counter[num] == 0:
            del self.counter[num]
        self.nums2[index] += val
        self.counter[self.nums2[index]] += 1


    def count(self, tot: int) -> int:
        res = 0
        for num1 in self.nums1:
            target = tot - num1
            if target in self.counter:
                res += self.counter[target]
        return res



# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)

