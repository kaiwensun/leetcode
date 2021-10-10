class Solution:
    def twoOutOfThree(self, *nums_list) -> List[int]:
        s1, s2, s3 = sets = list(map(set, nums_list))
        all_nums = s1 | s2 | s3
        res = []
        for num in all_nums:
            if sum(num in s for s in sets) >= 2:
                res.append(num)
        return res

