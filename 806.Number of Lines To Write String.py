class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        line_cnt = 1
        cur_width = 0
        for c in S:
            width = widths[ord(c) - ord('a')]
            if cur_width + width <= 100:
                cur_width += width
            else:
                line_cnt += 1
                cur_width = width
        return line_cnt, cur_width
