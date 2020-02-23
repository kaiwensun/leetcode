from datetime import date
class Solution(object):
    def daysBetweenDates(self, date1, date2):
        """
        :type date1: str
        :type date2: str
        :rtype: int
        """
        return abs((date(*map(int, date1.split("-"))) - date(*map(int, date2.split("-")))).days)
