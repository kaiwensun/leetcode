class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        cnt = 0
        for typ, color, name in items:
            item = {
                "type": typ,
                "color": color,
                "name": name
            }
            cnt += int(item[ruleKey] == ruleValue)
        return cnt

