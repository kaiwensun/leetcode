class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [pair[1] for pair in sorted(zip(heights, names), reverse=True)]

