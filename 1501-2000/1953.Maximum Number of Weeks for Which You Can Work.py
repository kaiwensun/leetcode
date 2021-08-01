class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        mx = max(milestones)
        sm = sum(milestones)
        return (sm - mx) * 2 + 1 if mx > sm - mx else sm

