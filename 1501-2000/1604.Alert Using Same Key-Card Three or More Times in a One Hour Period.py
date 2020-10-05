from collections import defaultdict
class Solution(object):
    def alertNames(self, keyName, keyTime):
        """
        :type keyName: List[str]
        :type keyTime: List[str]
        :rtype: List[str]
        """
        def time2minute(time):
            hr, mn = time.split(":")
            return int(hr) * 60 + int(mn)
        res = set()
        last = defaultdict(list)
        for time, name in sorted(zip(map(time2minute, keyTime), keyName)):
            last[name].append(time)
            if len(last[name]) >= 3:
                if last[name][-1] - last[name][-3] <= 60:
                    res.add(name)
        return list(sorted(res))

