class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        counter = collections.Counter(tasks)
        common = counter.most_common()
        max_cnt = 0
        for key_cnt in common:
            if common[0][1] != key_cnt[1]:
                break
            max_cnt += 1
        if max_cnt >= n + 1:
            return len(tasks)
        result = (common[0][1] - 1) * (n + 1) + max_cnt
        if len(tasks) <= result:
            return result
        else:
            return len(tasks)
