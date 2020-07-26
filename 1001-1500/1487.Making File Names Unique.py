from collections import defaultdict
class Solution(object):
    def getFolderNames(self, names):
        """
        :type names: List[str]
        :rtype: List[str]
        """
        
        counter = defaultdict(int)
        seen = set()
        res = []
        for name in names:
            if name not in seen:
                res.append(name)
                seen.add(name)
                continue
        
            v = counter[name] + 1
            while name + "(" + str(v) + ")" in seen:
                v += 1
            counter[name] = v
            res.append(name + "(" + str(v) + ")")
            seen.add(res[-1])
        return res
    
