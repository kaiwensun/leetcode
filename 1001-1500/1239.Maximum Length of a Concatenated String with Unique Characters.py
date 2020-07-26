class Solution(object):
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        set_group = {frozenset("")}
        for string in arr:
            string_set = frozenset(string)
            if len(string_set) != len(string):
                continue
            set_group = set_group | {s | string_set for s in set_group if len(s & string_set) == 0}
        return reduce(max, map(len, set_group), 0)
