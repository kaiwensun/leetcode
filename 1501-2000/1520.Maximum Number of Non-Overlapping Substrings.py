import string
class Solution(object):
    def maxNumOfSubstrings(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
        def isConflicting(start, end, existing_intervals):
            for ex_start, ex_end in existing_intervals:
                if start <= ex_start and ex_end <= end:
                    return True
            return False
        
        first = {}
        last = {}
        substring_range = {}
        for i, c in enumerate(s):
            first.setdefault(c, i)
            last[c] = i
        
        for c in first.keys():
            l_target = first[c]
            r_target = last[c]
            l = r = l_target
            while l_target < l or r < r_target:
                if l_target < l:
                    l -= 1
                    l_target = min(l_target, first[s[l]])
                    r_target = max(r_target, last[s[l]])
                if r < r_target:
                    r += 1
                    l_target = min(l_target, first[s[r]])
                    r_target = max(r_target, last[s[r]])
            substring_range[c] = (r_target - l_target, l_target, r_target)
        res_intervals = []
        all_intervals = sorted(substring_range.values())
        
        for _, start, end in all_intervals:
            if not isConflicting(start, end, res_intervals):
                res_intervals.append((start, end))
        return map(lambda (start, end): s[start: end + 1], res_intervals)
