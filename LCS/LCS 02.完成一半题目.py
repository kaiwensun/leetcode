from collections import Counter

class Solution(object):
    def halfQuestions(self, questions):
        """
        :type questions: List[int]
        :rtype: int
        """
        n = len(questions) // 2
        res = 0
        for _, cnt in Counter(questions).most_common():
            if n <= 0:
                break
            res += 1
            n -= cnt
        return res

