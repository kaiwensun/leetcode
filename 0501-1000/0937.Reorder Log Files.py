class Solution(object):
    def isLetterLog(self, log):
        l = log.split(' ', 1)[1][0]
        return 'a' <= l

    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        letter_logs = []
        digit_logs = []
        for log in logs:
            if self.isLetterLog(log):
                letter_logs.append(log)
            else:
                digit_logs.append(log)
        letter_logs = sorted(letter_logs, cmp=lambda l1, l2: cmp(l1.split(' ', 1)[1], l2.split(' ', 1)[1]))
        return letter_logs + digit_logs
    
